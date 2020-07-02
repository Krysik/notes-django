from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings

def index_view(request):
    return render(request, 'index.html', {})

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Dj-Notes - Aktywuj swoje konto'
            message = render_to_string('accounts/confirm_an_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject,
                message,
                to=[to_email],
                headers={ 'Reply To': settings.EMAIL_HOST_USER }
            )
            email.send()
            return render(request, 'accounts/confirm_an_email_msg.html')
    return render(request, 'accounts/register.html', {'form': form})

def activate_an_email(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    return render(request, 'accounts/confirm_an_email_succeed.html')


def login_view(request):
    form = LoginForm()
    error = None
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard') # notekeeper app
        else:
            error = '<span style="color: red;">Dane logowania nie są poprawne</span>'

    return render(request, 'accounts/login.html', {'form': form, 'error': error})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Wylogowano poprawnie')
    return redirect('login_view')