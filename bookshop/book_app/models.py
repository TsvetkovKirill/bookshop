from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinLengthValidator, MaxValueValidator#указать минимальную длину ввода от пользователя


class Feedback(models.Model):
    name = models.CharField(max_length=30, validators=[MinLengthValidator(3)])
    surname = models.CharField(max_length=60)
    feedback = models.TextField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
class Writer(models.Model):
    full_name = models.CharField(max_length=100, default='not known')
    first_name = models.CharField(max_length=100, default='not known')
    last_name = models.CharField(max_length=100, default='not known')
    writer_birthday = models.IntegerField(blank=True)
    writer_email = models.EmailField(blank=True)
    slug = models.SlugField(default='', null=False)  # запретили хранить Null

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_url_writers(self):  # выносим создание ссылки из шаблона в models с помощью функции reverce
        return reverse('writer-one', args=[self.slug])

    def save(self, *args, **kwargs):  # слаггифицировать таблицу в БД
        self.slug = slugify(self.full_name)
        super(Writer, self).save(*args, **kwargs)


class Character(models.Model):
    first = 'main'
    others = 'others'
    all_characters = [
        (first, 'Главный'),
        (others, 'Второстепенный'),
    ]

    name = models.CharField(max_length=100, default='not known')
    age = models.IntegerField(blank='')
    gender = models.CharField(max_length=10, default='not known')
    status = models.CharField(max_length=10, choices=all_characters, default=others)
    slug = models.SlugField(blank='')

    def __str__(self):
        if self.status == self.first and self.gender:
            return f'Персонаж {self.name} является главным и ему {self.age}'
        else:
            return f'Персонаж {self.name} является второстепенным и ему {self.age}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)  # превращаем значение строки title в slug
        super(Character, self).save(*args, **kwargs)

    def get_url_characters(self):  # выносим создание ссылки из шаблона в models с помощью функции reverce
        return reverse('character-one', args=[self.slug])


class PublisherHouse(models.Model):
    title = models.CharField(max_length=100, default='not known')
    country = models.CharField(max_length=50, default='USA')

    def __str__(self):
        return f'{self.title}'


class Book(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollars'),
        (RUB, 'Rubles'),
    ]
    title = models.CharField(max_length=70)
    rating = models.IntegerField()
    year = models.IntegerField(null=True,
                               blank=True)  # blank means we can save empty values, Null means we can save 0-value
    budjet = models.IntegerField(default=1000)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='RUB')
    author = models.CharField(max_length=100, null=True)
    genre = models.CharField(max_length=20, blank=True, null=True)
    is_best_selling = models.CharField(max_length=100, default='NO')
    slug = models.SlugField(default='', null=False)  # запретили хранить Null
    writer = models.ForeignKey(Writer, on_delete=models.PROTECT,
                               null=True)  # создаем внешний ключ, связь один ко многим, один писатель, много книг
    publisher_house = models.ForeignKey(PublisherHouse, on_delete=models.CASCADE, null=True, blank=True)
    characters = models.ManyToManyField(Character)#многие ко многим, прописано в шаблоне one_book. список персонажей, прописанных в админке, для конкретной книги

    def save(self, *args, **kwargs):

        self.slug = slugify(self.title)  # превращаем значение строки title в slug
        super(Book, self).save(*args, **kwargs)

    def get_url(self):  # выносим создание ссылки из шаблона в models с помощью функции reverce
        return reverse('book-detail', args=[self.slug])

    def __str__(self):
        return f'{self.title}, {self.rating}, {self.year}, {self.budjet}, {self.author}'
