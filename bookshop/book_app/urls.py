from django.urls import path
from . import views as book_views
from .views import DoneView, ListFeedBack, DetailFeedBack


urlpatterns = [
    path("", book_views.show_all_books),
    path("book/<slug:slug_book>", book_views.get_info_about_one_book, name='book-detail'),
    path("writers/", book_views.ListWriter.as_view(), name='writers-detail'),
    path("characters/", book_views.get_info_about_all_characters, name='characters-detail'),
    path("writers/<slug:slug_writer>", book_views.get_info_about_one_writer, name='writer-one'),
    path("characters/<slug:slug_character>", book_views.get_info_about_one_character, name='character-one'),
    path("done/", DoneView.as_view(), name='get-done'),
    path("detail/<int:pk>/", DetailFeedBack.as_view(), name='get-detailfeedback'),
    path("list/", ListFeedBack.as_view(), name='get-ListFeedBack'),
    path("feedback/", book_views.FeedBackView.as_view(), name='send-review'),
    path("<int:id_feedback>/", book_views.update_feedback, name='update_feedback'),
    path("<int:id_feedback>/", book_views.FeedBackView.as_view(), name='update_feedback'),
]
