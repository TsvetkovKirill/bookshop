from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinLengthValidator, MaxValueValidator#указать минимальную длину ввода от пользователя


class Bootstrap(models.Model):
    name = models.CharField(max_length=30, validators=[MinLengthValidator(3)])
    surname = models.CharField(max_length=60)
    feedback = models.TextField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
