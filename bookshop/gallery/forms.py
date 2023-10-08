from django.forms import forms

class GalleryUploadForm(forms.Form):
    image = forms.FileField()#открыть окно проводника для загрузки