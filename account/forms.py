from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class CustomRegisterFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',  'password1']
        #fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class CustomerForm(ModelForm):
    class Meta:
        model = Customer

        fields = ['name', 'phone', 'location', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})