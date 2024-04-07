from django.http import HttpResponse
from django.shortcuts import render

from stuff.models import Categories

from jinja2 import Template


# Create your views here.
def index(request):
    
    
    context = {
    
    'title': "Kompik - Главная",
    'content': "Kompik",
        
    }   
    return render(request, 'main/index.html', context)

def about(request):
    context = {
    
    'title': "Kompik - Информация",
    'content': "Информация о мазазине",
    'text_on_page': "Описанаие магазина ссылки и контакты" 
    }   
    return render(request, 'main/about.html', context)