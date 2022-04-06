from django.shortcuts import render
from .models import Product, Category
from django.contrib.auth.decorators import login_required

@login_required(login_url='signin')
def index(request):
    categories = Category.objects.all()
    products = Product.objects.order_by('-created_at')
    return render (request, 'store/index.html', {
        'products' : products, 
        'categories' : categories,
    })
    