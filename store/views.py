import stripe
from django.conf import settings
from django.urls import reverse
from django.db.models import Q 
from django.shortcuts import render, get_object_or_404 
from django.contrib.auth.decorators import login_required
from .models import Product, Category


stripe.api_key = settings.STRIPE_SECRET_KEY



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
    
# def cart(request):
#     customer = request.user.customer
#     order, created = Order.objects.get_or_create(customer=customer, is_complete=False)
#     items = order.orderitem_set.all() 
#     items_count = order.get_cart_item
#     context = {'items': items, 'items_count': items_count, 'order': order }
#     return render(request, 'store/cart.html', context)

 



