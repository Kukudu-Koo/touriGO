from asyncio.windows_events import NULL
from xmlrpc.client import boolean
from django.forms import formset_factory
# from django import forms
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method =='POST':
        username=request.POST['Username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['Email']
        contact_number=request.POST['contact_number']
        password1=request.POST['Password1']
        password2=request.POST['Password2']
        service_provider=request.POST.get('service_provider',False)
        if service_provider=='on':
            service_provider=True 
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'This Username Already exists, Please try again')
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'This Email Id Already exists, Please try again')
                return redirect('/')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name,is_staff=service_provider)
                user.save()
                messages.success(request,'User Created Successfully!!!, Please login')
                return redirect('/')
        else:
            messages.error(request,'Passwords didn\'t matched, Please try again')
            return redirect('/')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['Password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            # messages.error(request,'Invalid Credentials')
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials ,Please Try Again')
            return redirect('/')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')