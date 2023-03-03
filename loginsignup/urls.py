from django.urls import path
from .views import login, signup, handlesignup
appname = 'main_app'

urlpatterns = [

    path('login',login, name="login"),
    path('signup',signup, name="signup"),
    path('handleSignup', handlesignup, name="handleSignup")
]