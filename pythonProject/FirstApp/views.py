from django.shortcuts import render, redirect

from FirstApp.forms import FirstAppForm, RegisterForm
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request, 'login.html')

def index(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        form = RegisterForm()
        messages.success(request, 'Student registered successfully!')
        return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'index.html', {"form":form})

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        form = RegisterForm()
        messages.success(request, 'Student registered successfully!')
        return redirect('register')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {"form":form})
def aboutus(request):
    form = FirstAppForm()
    return render(request, 'aboutus.html', {"form":form})
