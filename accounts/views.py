import uuid, sys
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from accounts.models import Token

def send_login_email(request):
    email = request.POST['email']
    send_mail(
        'Your login link for Superlists',
        'body text tbc',
        'noreply@superlists',
        [email],
    )
    return redirect('/')

def login(request):
    print('login view', file=sys.stderr)
    uid = request.GET.get('uid')
    user = authenticate(uid=uid)
    if user is not None:
        auth_login(request, user)
    return redirect('/')

def logout(request):
    auth_logout(request)
    return redirect('/')
