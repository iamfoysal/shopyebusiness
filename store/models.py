import uuid
from django.db import models


class Category (models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural= 'Categories'

class Product (models.Model):
    title = models.CharField(max_length=200, null= True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, null= True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models. ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
