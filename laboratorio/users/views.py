from django.shortcuts import render, redirect
from django.contrib.auth import authenticate  # se importa del paquete registration por defecto de django
from django.contrib.auth.forms import AuthenticationForm # se importa del paquete registration por defecto de django
from django.contrib.auth.forms import UserCreationForm  # se importa del paquete registration por defecto de django
from django.contrib.auth import login as do_login   # se importa del paquete registration por defecto de django
from django.contrib.auth import logout as do_logout # se importa del paquete registration por defecto de django
# Create your views here.



def login(request):
    form = AuthenticationForm()
    if request.method == "POST":    #Empieza a verificar los datos del usuario si es igual a POST en el template
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.clean_data['username']  #con esto recuperamos las credenciales dadas por el usuario
            password = form.clean_data['password']

            user = authenticate(username, password)

            if user is not None:
                do_login(request, user)
                return redirect('login')

    return render(request, 'users/login.html', {'form':form})

def welcome(request):       #primero verificamos si esta autenticado se va a weolcome si no a login
    if request.user.is_authenticated:
        return render(request, 'users/welcome.html')

    return redirect('users/register.html')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            user.form.save()

        if user is not None:
            do_login(request, user)
            return redirect('users/login.hmtl')

    return render(request, 'users/register.html', {'form':form})



def logout(request):
    do_logout(request)
    return redirect('users/login.hmtl')