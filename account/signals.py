from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db.models.signals import post_save, post_delete
from django.conf import settings
from django.dispatch import receiver
from .models import User, Customer


@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created and instance.email:
        Customer.objects.create(user=instance)

        message = render_to_string('account/accountmail.html', {'name': instance.get_full_name()})

        send_mail(
            'Welcome to join ShopY',
            message,
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            fail_silently= False,
        )


        

@receiver(post_save, sender=Customer)
def update_customer(sender, instance, created, **kwargs):
    if not created:
        customer = instance
        user = customer.user
        user.name = customer.name
        user.save()
    

# @receiver(post_delete, sender=Customer)
# def delete_customer(sender, instance, created, **kwargs):
#     if created:
#         user = instance.user
#         user.delete()
    