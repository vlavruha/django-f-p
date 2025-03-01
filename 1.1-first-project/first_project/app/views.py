from django.http import HttpResponse
from django.shortcuts import render, reverse
import os
from django.utils import timezone


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = timezone.now()
    msg = f'Текущее время: {current_time.strftime('%d-%m-%Y %H:%M:%S')}'
    return HttpResponse(msg)


def workdir_view(request):
    directory = 'C:/Users/User/dj-homeworks'
    files = os.listdir(directory)
    msg = f'Список файлов: {files}'
    return HttpResponse(msg)
    raise NotImplemented
