from django.urls import path
from . import views as book_views



urlpatterns = [
    path("load_image/", book_views.GalleryView.as_view()),
]
