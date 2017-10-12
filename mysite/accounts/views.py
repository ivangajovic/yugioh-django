# from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']

        User.objects.create(
            username = username,
            email = email,
            password1 = password1,
        )
        return HttpResponse('')
