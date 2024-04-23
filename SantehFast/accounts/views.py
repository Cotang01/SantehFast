from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from orders.models import Order


def register_user(request) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register_form.html', {'form': form})


def login_user(request) -> HttpResponse:
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login_form.html', {'form': form})


def user_profile(request) -> HttpResponse:
    user = request.user
    orders = Order.objects.filter(phone=user.phone)
    return render(request, 'profile.html', {'user': user, 'orders': orders})
