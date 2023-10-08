"""
Создаем формы без html
"""
from django import forms
from .models import Feedback

# class FeedbackForm(forms.Form):
#     name = forms.CharField(label='Name', max_length=10, min_length=1, error_messages={
#         'max_length': 'Too many symbols',
#         'min_length': 'Too few symbols',
#         'required': 'Set minimum one symbol',
#     })
#     surname = forms.CharField()
#     feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}))
#     rating = forms.IntegerField(label='Rating', max_value=10, min_value=1)
class FeedbackForm(forms.ModelForm):# прописать класс для форм
    class Meta:
        model = Feedback
        # fields = ['name', 'rating', 'surname']
        fields = '__all__'#прописать все поля
        # exclude = ['rating']
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'feedback': 'Отзыв',
            'rating': 'Рейтинг',
        }
        error_messages = {
            'name': {
                'max_length': 'дохуя',
                'min_length': 'нихуя',
                'required': 'ваще похуям',
            },
            'surname': {
                'max_length': 'дохуя',
                'min_length': 'нихуя',
                'required': 'ваще похуям',
            },
            'feedback': {
                'max_length': 'дохуя',
                'min_length': 'нихуя',
                'required': 'ваще похуям',
            },
            'rating': {
                'max_length': 'дохуя',
                'min_length': 'нихуя',
                'required': 'ваще похуям',
            }
        }
