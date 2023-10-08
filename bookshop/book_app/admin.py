from django.contrib import admin
from .models import Book, PublisherHouse, Character, Writer, Feedback
from django.db.models import QuerySet  # импортировали модуль, чтобы потом анонсировать


@admin.register(PublisherHouse)
class PublisherHouseAdmin(admin.ModelAdmin):
    list_display = ['title', 'country']
    list_editable = ['country']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'feedback', 'rating']
    list_editable = ['surname', 'feedback', 'rating']

@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'first_name', 'last_name', 'writer_birthday', 'writer_email', 'slug']
    list_editable = ['first_name', 'last_name', 'writer_birthday', 'writer_email', 'slug']


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'status', 'slug', 'gender']
    list_editable = ['age', 'status', 'slug', 'gender']


"""
В этом классе регистрируются переменные и методы.
"""


@admin.register(Book)  # второй способ, то же самое, но через декоратор
class BookAdmin(
    admin.ModelAdmin):  # добавляем новые колонки в таблице. Название класса соответствует приложению, плюс Admin
    list_display = ['title', 'rating', 'year', 'genre', 'currency', 'is_best_selling', 'rating_status', 'writer',
                    'publisher_house']
    list_editable = ['rating', 'year', 'currency', 'genre', 'is_best_selling',
                     'writer',
                     'publisher_house']  # нужно, чтобы редактировать поля в админке (не прописывать первое поле, это ссылка!)
    ordering = ['-rating',
                'title']  # позволяет сортировать. второй аргумент дополнительная сортировка. - обратная сортировка
    list_per_page = 10
    filter_horizontal = ['characters']
    actions = ['set_dollars']

    # admin.site.register(Book, BookAdmin)#регистрация классов из моделей в админке для их отображения
    @admin.display(ordering='rating')
    def rating_status(self, book: Book):  # вычисляемое поле
        if book.rating < 50:
            return 'No'
        elif 51 <= book.rating <= 70:
            return 'May be'
        elif 71 <= book.rating <= 90:
            return 'Must-see'
        return 'masterpiece'

    """
    Следующая функция создает действие-виджет в админке,
     чтобы сразу быстро поменять значения в соответствующей колонке
    """

    @admin.action(
        description='Установить валюту как доллар')  # на сайте в админке добавляет виджет-действие с соответствующим названием
    def set_dollars(self, request, queryset: QuerySet):  # анонсировали переменную, чтобы высветились подсказки
        queryset.update(currency=Book.USD)  # обращение к константе класса Book
