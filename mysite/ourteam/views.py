from django.shortcuts import render, redirect

from django.http import HttpResponse

from ourteam.forms import UserForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout



def index(request):
   return render(request, 'ourteam/index.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registrasiya boldunyz')
            return redirect('login')
        else:
            messages.error(request, 'Error Register')
    else:
        form = UserForm()
    return render(request, 'ourteam/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'ourteam/login.html', {'form': form})

def staff_page(request):
    return render(request, 'ourteam/staff_page.html')

def user_logout(request):
    logout(request)
    return redirect('login')