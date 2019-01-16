from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def register(request):
    if request.method=='POST':
        form1=userform(request.POST)
        if form1.is_valid():
            username=form1.cleaned_data['username']
            first_name = form1.cleaned_data['first_name']
            last_name = form1.cleaned_data['last_name']
            email = form1.cleaned_data['email']
            password = form1.cleaned_data['password']
            User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            messages.success(request,f'Hello {username} Your Request Has been Posted.')
            notify(request, username)
            return redirect('login')
    else:
        form1=userform()	
    context = {'form':form1}
    return render(request,'registration.html',context)

def logoutuser(request):
    logout(request)
    return render(request,'login.html')

def profile(request):
    return render(request,'profile.html')


def loginuser(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method=='POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                if  user.is_staff:
                    login(request,user)
                    return redirect('index')
                else:
                    return HttpResponse("<h1>Wait for Permissions.</h1>")
            else:
                return HttpResponse('<h1>invalid</h1>')
        else:
            return render(request,'login.html')


def changepass(request):
    user=request.user
    if request.method=="POST":
        form=ChangePasswordForm(request.POST)
        p=request.POST['old_password']
        u=authenticate(username=user,password=p)
        if u is not None:
            if form.is_valid():
                new_password=form.cleaned_data['new_password']
                user.set_password(new_password)
                user.save()
                return redirect('/login')
        else:
            message='Incorrect value of Old Password'
            return render(request,'changepass.html',{'message':message,'form':form})
    else:
        form=ChangePasswordForm()
    return render(request,'changepass.html',{'form':form})


def notify(request,username):
    superuser=User.objects.get(is_superuser=True)
    print("super user  ==== ",superuser)
    super_email=superuser.email
    print('email==========', super_email,type(super_email))
    messages.add_message(request, messages.INFO, '=====New User request=====')
    subject = "Notification"
    msg = f"New user authentication request!!!! \n {username} wants staff permission "
    send_mail(subject, msg, settings.EMAIL_HOST_USER, [super_email])
    print('email==========',super_email)
    print('user name ++++',username)
    return

def index(request):
    return render(request,'index.html')