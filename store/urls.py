from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:slug>/', views.product_by_category, name='product_by_category'),
    # path('cart/', views.cart, name='cart'),
    
]
