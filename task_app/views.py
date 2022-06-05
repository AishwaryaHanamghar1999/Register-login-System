from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from task_app.forms import login_form, signup_form
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def user_login(request):
    if not request.user is authenticate:
        if request.method=="POST":
            fm=login_form(request=request,data=request.POST)
            if fm.is_valid():
                username=fm.cleaned_data['username']
                passwd=fm.cleaned_data['password']
                em=fm.cleaned_data['email']
                user=authenticate(username=username,password=passwd,email=em)
                if user is not None:
                    login(request,user)
                    
                    return render(request,'welcome.html')
        else:
            fm=login_form()
        return render(request,'login.html',{'form':fm})
    else:
        messages.error(request,'Login Failed')
    
def welcome(request):
    return render(request,'welcome.html')

def user_signup(request):
    if request.method=="POST":
        form=signup_form(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/login/')
    else:
        form=signup_form()
    return render(request,'register.html',{'form':form})

def user_logout(request):
    return HttpResponseRedirect('/signup.html')


# Create your views here.
