from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages


def login(request):
    return render(request, 'loginsignup/login.html')

