from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomRegisterFrom, CustomerForm 
from django.contrib import messages

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password= password)

        if user is not None:
            login (request, user)
            messages.success(request, "login successfully complete!!")
            return redirect('index')

        else:
            messages.error(request, "Wrong password or user name! Please try Again")

    return render(request, 'account/signin.html')



def signup(request):
    form = CustomRegisterFrom ()
    if request.method == 'POST':
        form = CustomRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
            return redirect("signin")
        

    return render(request, 'account/signup.html',{'form':form} )


def signout(request):
    logout(request)
    messages.success(request, "logout successfully.")
    return redirect("signin")


def account(request):
     customer = request.user.customer
     return render(request, 'account/account.html', {
          'customer': customer
     })


def account_update(request):
    form = CustomerForm()
    customer = request.user.customer

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated.')

    return render(request, 'account/update.html', {
            'form': form,
            'customer': customer
    })

