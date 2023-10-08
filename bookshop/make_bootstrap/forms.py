"""
Создаем формы без html
"""
from django import forms
from .models import Bootstrap


class BootstrapForm(forms.ModelForm):  # прописать класс для форм
    class Meta:
        model = Bootstrap
        # fields = ['name', 'rating', 'surname']
        fields = '__all__'  # прописать все поля
        # exclude = ['rating']
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'feedback': 'Отзыв',
            'rating': 'Рейтинг',
        }
