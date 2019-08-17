from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm

def index_view(request):
    return render(request, 'index.html', {})

def register_view(request):
    form = RegisterForm()
    error = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = '<span style="color: red;">Coś poszło nie tak :(<span>'
    return render(request, 'accounts/register.html', {'form': form, 'error': error})
