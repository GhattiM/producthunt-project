from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html',{'error':'Username already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'accounts/signup.html',{'error':'Passwords must match'})
    else:

        return render(request,'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        if user.is_active:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error':'username or password is incorrect'})
    return render(request,'accounts/login.html')


def user_logout(request):
    if request.method == 'POST':

        auth.logout(request)
        return render(request,'accounts/signup.html')
