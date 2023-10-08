from django.urls import path
from . import views as girls_views



urlpatterns = [
    path("girls_list/", girls_views.get_girls_list, name="girls"),
    path("girls_list/girl_1/", girls_views.get_first_girl, name="girl_1"),
]
