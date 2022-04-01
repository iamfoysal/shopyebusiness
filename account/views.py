from django.shortcuts import render


def signup(request):
    return render(request, 'account/signup.html')


def signin(request):
    return render(request, 'account/signin.html')


def signout(request):
    pass
