from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomRegisterFrom
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
            messages.error(request, "Ei tor bhul hoiche!! Bal Thik kor")

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

