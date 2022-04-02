from django.shortcuts import render


def signin(request):
    return render(request, 'account/signin.html')


def signup(request):
    return render(request, 'account/singup.html')


