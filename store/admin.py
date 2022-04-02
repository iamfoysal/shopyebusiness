from django.contrib import admin
from .models import Category, Product

class CatagoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CatagoryAdmin) 
admin.site.register(Product, ProductAdmin)
