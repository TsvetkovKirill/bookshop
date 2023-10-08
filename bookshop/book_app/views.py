from django.shortcuts import render, get_object_or_404
from .models import Book, Writer, Character, Feedback
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from django.db.models import F, Sum, Max, Min, Count, Avg, \
    Value  # F - применить к объекту различные свойства. Манипулировать местоположением на сайте None.
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

class FeedBackView(FormView):#создаем форму с помощью класса
    form_class = FeedbackForm
    template_name = 'book_app/feedback.html'
    success_url = '/done'

    def form_valid(self, form):
        form.save()
        return super(FeedBackView, self).form_valid(form)

# class FeedBackView(View):#создаем форму с помощью функции
#     def get(self, request):
#         form = FeedbackForm()
#         return render(request, 'book_app/feedback.html', context={'form': form})
#
#     def post(self, request):
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/done')
#         return render(request, 'feedback/feedback.html', context={'form': form})


class DoneView(TemplateView):  # рендерим шаблон с помощью CBV TemplateView
    template_name = 'book_app/done.html'

    def get_context_data(self, **kwargs):  # переопределяем метод для передачи данных в шаблон через контекст
        context = super().get_context_data(**kwargs)  # вызов через родителя (super) возвращает контекст
        context['name'] = 'Ivan'  # может положить значения в переменную context. Это словарь. Можно вывести в шаблон {{}}
        context['surname'] = 'Ivanov'
        return context


# class ListFeedBack(TemplateView):  # выводим все отзывы из модели
#     template_name = 'book_app/list_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['all_feed'] = Feedback.objects.all()
#         return context

class ListFeedBack(ListView):  # выводим данные из модели с помощью CBV ListViews
    template_name = 'book_app/list_feedback.html'
    model = Feedback
    context_object_name = "feedbacks"#переопределяем переменную, итерируемся в шаблоне по "feedbacks"
    def get_queryset(self):#возвращаем фильтрованные данные из формы
        queryset = super().get_queryset()#переопределяем родительский метод
        filter_gs = queryset.filter(rating__gt=3)#фильтруем по рейтингу, райтинг больше 3
        return filter_gs

class ListWriter(ListView):  # выводим данные из модели с помощью CBV ListViews
    template_name = 'book_app/all_writers.html'
    model = Feedback
    context_object_name = "writers"
    def get_queryset(self):#возвращаем фильтрованные данные из формы
        queryset = super().get_queryset()#переопределяем родительский метод
        # filter_gs = queryset.filter(rating__gt=3)#фильтруем по рейтингу, райтинг больше 3
        return queryset

# class DetailFeedBack(TemplateView):  # выводим по отзыву из модели
#     template_name = 'book_app/detail_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['current'] = get_object_or_404(Feedback, id=kwargs['id_feedback'])
#         return context
class DetailFeedBack(DetailView):  # с помощью данного класса можно вывести конкретную ячейку из модели по id.
    template_name = 'book_app/detail_feedback.html'
    model = Feedback

# def send_review(request):  # записываем данные из POST-запроса в таблицу.
#     if request.method == 'POST':  # if get POST
#         form = FeedbackForm(
#             request.POST)  # создаем переменную form и заполняем ее данными. Если создать форму через модель, это произойдет автоматически,
#         # потому мы и закомментили внизу.
#         if form.is_valid():
#             # feed = Feedback(
#             #     name=form.cleaned_data['name'],
#             #     surname=form.cleaned_data['surname'],
#             #     feedback=form.cleaned_data['feedback'],
#             #     rating=form.cleaned_data['rating'],
#             # )
#             form.save()
#             return HttpResponseRedirect('/done')
#     else:
#         form = FeedbackForm()
#     return render(request, 'book_app/feedback.html', context={'form': form})


def update_feedback(request, id_feedback):  # функция редактирования записей в БД с помощью форм
    feed = Feedback.objects.get(id=id_feedback)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
    else:
        form = FeedbackForm(instance=feed)
    return render(request, 'book_app/feedback.html', context={'form': form})


def show_all_books(request):
    # books = Book.objects.all()#выводим весь список книг
    # books = Book.objects.order_by(F('year').desc(nulls_last=True), '-title', '-rating')#с помощью это функции сортируем. - значит обратную сортировку. Срезом выбираем несколько.
    books = Book.objects.annotate(
        # true_bool=Value(True),
        # false_bool=Value(True),
        str_field=Value(True),
        int_field=Value(True),
    )
    agg = books.aggregate(Avg('budjet'), Max('rating'), Min('rating'), Avg('rating'))
    # for book in books:#добавить slug в каждую колонку
    #     book.save()
    context = {'books': books, 'budjet_avg': agg['budjet__avg'], 'rating_avg': agg['rating__avg'],
               'rating_min': agg['rating__min'], 'rating_max': agg['rating__max'], 'total': books.count()}
    return render(request, 'book_app/all_books.html', context=context)


def get_info_about_one_book(request, slug_book: str):  # получаем информацию о фильме по slug или id
    book = get_object_or_404(Book, slug=slug_book)  # если значения нет, вернется ошибка 404
    return render(request, 'book_app/one_book.html', {"book": book})


def get_info_about_all_writers(request):  # получаем информацию об писателе по slug или id
    writers = Writer.objects.all()  # выводим весь список писателей
    for writer in writers: #слаггификация
        writer.save()
    return render(request, 'book_app/all_writers.html', {'writers': writers})


def get_info_about_one_writer(request, slug_writer: str):  # получаем информацию о фильме по slug или id
    writers_list = get_object_or_404(Writer, slug=slug_writer)  # если значения нет, вернется ошибка 404
    return render(request, 'book_app/one_writer.html', {"writers_list": writers_list})


def get_info_about_all_characters(request):
    characters = Character.objects.all()
    for character in characters:  # слаггификация
        character.save()
    return render(request, 'book_app/all_characters.html', {'characters': characters})


def get_info_about_one_character(request, slug_character: str):  # получаем информацию о персонаже по slug
    characters_list = get_object_or_404(Character, slug=slug_character)  # если значения нет, вернется ошибка 404
    return render(request, 'book_app/one_character.html', {"characters_list": characters_list})
