from django.urls import path
from .views import *

urlpatterns = [
    path('',register,name='register'),
    path('login/',loginuser,name='login'),
    path('logout/',logoutuser,name='logout'),
    path('profile/',profile,name='profile'),
    path('index/',index,name='index'),
    path('changepassword/',changepass,name='changepass'),
]