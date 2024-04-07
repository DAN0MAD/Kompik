
from django.urls import path
from stuff import views

from django.conf.urls.static import static

app_name = 'stuff'

urlpatterns = [
    path('search/', views.catalog, name='search'),   
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
   
]
