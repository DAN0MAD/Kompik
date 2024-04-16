from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

from stuff.models import Products
from stuff.utils import q_search

# Create your views here.
def catalog(request, category_slug=None):
    
    page= request.GET.get('page', 1)
    on_sale= request.GET.get('on_sale', None)
    order_by= request.GET.get('order_by', None)
    query= request.GET.get('q', None)
    
    if category_slug == 'all':
        stuff = Products.objects.all()   
        
    elif query:
        stuff = q_search(query)    
        
    else:
        stuff = get_list_or_404(Products.objects.filter(category__slug=category_slug))
        
    if on_sale:
        stuff = stuff.filter(discount__gt=0)
            
    if order_by and order_by != "default":
        stuff = stuff.order_by(order_by)
   
    paginator = Paginator(stuff,3)      
    current_page = paginator.page(int(page))
         
    context = {
        "title": "Kompik - Каталог",
        "stuff": current_page,
        "slug_url": category_slug,
     
    }
    return render(request, "stuff/catalog.html", context)

# контроллер поиска товаров
def product(request, product_slug): 
    
    product: Products = Products.objects.get(slug=product_slug) # получение slug продукта
    
    context={ #передача контекстных переменных
      'product': product  
    }
    
    return render(request, "stuff/product.html", context=context) #отображение необходимого контента
