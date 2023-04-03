from django.contrib import auth
from django.contrib.auth import login
from django.shortcuts import render

from users.forms import LoginForm, RegistrationForm, ChangeForm


def login_1(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return render(request, 'products/index.html', )
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'products/index.html', )
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


def profile(request):
    if request.method == 'POST':
        form = ChangeForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            form = ChangeForm(instance=request.user)
            return render(request, 'users/profile.html', {'form': form})
    else:
        form = ChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'users/profile.html', context)
