from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.http import HttpResponse


def get_girls_list(request):
    return render(request, 'girls/girls.html', context={'slut': "https://stepik.org/lesson/730393/step/1?unit=731895"})

def get_first_girl(request):
    name = 'girls_list/girl_1/'
    return render(request, 'girls/girl_1.html', context={'slut': name})


