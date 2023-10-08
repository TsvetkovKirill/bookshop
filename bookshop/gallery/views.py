from django.shortcuts import render
from django.views import View
from .forms import GalleryUploadForm
from django.http import HttpResponseRedirect
from .models import Gallery
# def storage_file(file): #не нужно, поскольку используем класс из модели для сохранения данных.
#     with open("gallery_tmp/new_image.jpg", 'wb+') as new_file:
#         for chunk in file.chunks():
#             new_file.write(chunk)
class GalleryView(View):
    def get(self, request):
        form = GalleryUploadForm()#пробрасываем форму загрузки файла в шаблон
        return render(request, 'gallery/load_file.html', {'form': form})

    def post(self, request):
        form = GalleryUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = Gallery(image=form.cleaned_data['image'])#берем данные из класса Gallery models
            new_image.save()#сохраняем данные в нужную папку
            return HttpResponseRedirect('load_image')
        return render(request, 'gallery/load_file.html', {'form': form})