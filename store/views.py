from django.shortcuts import render
from .models import Product, Category
from django.contrib.auth.decorators import login_required
from django.db.models import Q 

# @login_required(login_url='signin')
def index(request):
    products = Product.objects.order_by('-created_at')
    categories = Category.objects.all()
    search = Product.objects.all()
    if request.method =='POST':
        search = request.POST.get('search')
        results = Product.objects.filter(Q(title__icontains=search))                                                     
        context =  { 'results': results, 'search': search}
        return render(request, 'store/search-result.html', context) 
    # else:
    #     print("Search not found")

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
    