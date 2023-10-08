from django.shortcuts import render, get_object_or_404
# from .models import Book, Writer, Character, Feedback
from django.http import HttpResponseRedirect
from .forms import BootstrapForm
from django.db.models import F, Sum, Max, Min, Count, Avg, \
    Value  # F - применить к объекту различные свойства. Манипулировать местоположением на сайте None.
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView


class BootstrapView(FormView):  # создаем форму с помощью класса
    form_class = BootstrapForm
    template_name = 'make_bootstrap/bootstrap_page.html'

    def bootstrap_page_handler(request):
        return render(request, 'make_bootstrap/bootstrap_page.html', context={'form': BootstrapView.form_class,
                                                                              'template': BootstrapView.template_name, })


def get_index(request):
    return render(request, 'make_bootstrap/index.html')
