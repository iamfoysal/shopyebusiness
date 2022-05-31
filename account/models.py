from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null = True, blank= True)
    phone = models.CharField(max_length=15, null = True, blank= True)
    location = models.CharField(max_length=255, null = True, blank= True)
    image = models.ImageField(upload_to = 'avatar/', null = True, blank = True)


    def __str__(self):
        return str(self.user)
        
   











