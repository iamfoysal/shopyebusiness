from django.contrib import admin
from .models import Category, Product

class CatagoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'discount_price','price','category','created_at')



admin.site.register(Category, CatagoryAdmin) 
admin.site.register(Product, ProductAdmin)
