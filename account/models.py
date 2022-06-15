from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null = True, blank= False)
    phone = models.CharField(max_length=15, null = True, blank= False)
    location = models.CharField(max_length=255, null = True, blank= False)
    image = models.ImageField(upload_to = 'avatar/', null = True, blank= False)


    def __str__(self):
        return str(self.user)
        
   











