from django.shortcuts import redirect, render
from .forms import RegisterForm
from .models import Account
#from .forms import SignUpForm


def start(request):
    return render(request, 'account/start.html', {})


def login(request):
    return render(request, 'account/login.html', {})


def register(request):
    data = RegisterForm()
    return render(request, 'account/register.html', {'data': data})


def mypage(request):
    return render(request, "account/mypage.html", {})
