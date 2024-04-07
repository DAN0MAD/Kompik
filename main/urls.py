
from django.urls import path
from main import views

from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    
]
