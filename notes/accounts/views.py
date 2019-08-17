from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def index_view(request):
    return render(request, 'index.html', {})

def register_view(request):
    form = RegisterForm()
    error = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
        else:
            error = '<span style="color: red;">Coś poszło nie tak :(<span>'
    return render(request, 'accounts/register.html', {'form': form, 'error': error})

def login_view(request):
    form = LoginForm()
    error = None
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            error = '<span style="color: red;">Dane logowania nie są poprawne</span>'

    return render(request, 'accounts/login.html', {'form': form, 'error': error})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login_view')