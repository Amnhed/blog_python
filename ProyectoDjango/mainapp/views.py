from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request,'mainapp/index.html',{'title':'Inicio'})

def about(request):
    return render(request,'mainapp/about.html',{'title':'Sobre Nosotros'})

def register_page(request):

    register_form = RegisterForm()

    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Usario creado correctamente')

            #va el nombre que asigne en view
            return redirect('index')

    return render(request,'users/register.html',{
        'title': 'Registro',
        'register_form': register_form
    })

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Bienvenido has iniciado sesion')
            return redirect('index')

        else:
            messages.warning(request, 'Password o usuario incorrecto!')


    return render(request, 'users/login.html',{
        'title': 'Login'
    })