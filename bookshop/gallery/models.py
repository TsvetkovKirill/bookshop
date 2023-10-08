from django.db import models


class Gallery(models.Model):#в DB записывается ссылка, сам файл в папке uploads
    image = models.FileField(upload_to='my_gallery')#сохраняем изображения от юзера в папку my_data
# Create your models here.
