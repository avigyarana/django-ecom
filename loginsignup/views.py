from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User

from django.contrib import messages

from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer



# Create your views here.


def login(request):
    return render(request, 'loginsignup/login.html')

def signup(request):
    return render(request, 'loginsignup/signup.html')


def handlesignup(request):
    if (request.method == "POST"):
        uname = request.POST.get("username")
        em = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        cpass = request.POST.get("pass2")
        print(uname, em, pass1, cpass)

        if pass1 != cpass:

            messages.warning(request, "password incorrect")
            return redirect("signup")

        try:
            if User.objects.get(username = uname):
                messages.info(request, "username taken")
                return redirect(signup)

            if User.objects.get(email=em):
                messages.info("email taken")
                return redirect("signup")

        except:
            pass

        myuser = User.objects.create_user(uname, em, pass1)

        myuser.save()

        messages.success(request, "signup success")
        return redirect("loginsignup/login.html")
    return render(request, 'loginsignup/signup.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date-joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('-date-joined')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

