from django.shortcuts import render
from .models import Product, Category
from django.contrib.auth.decorators import login_required

@login_required(login_url='signin')
def index(request):
    products = Product.objects.order_by('-created_at')
    categories = Category.objects.all()
    context = {
                'categories': categories, 
                'products' : products,
                
                }

    return render (request, 'store/index.html', context)

def product_by_category(request, slug):
    products = Product.objects.filter(category__slug=slug)
    categories = Category.objects.all()
    context =  { 'products': products,
                'categories': categories,
                }
    return render (request, 'store/index.html', context)
    