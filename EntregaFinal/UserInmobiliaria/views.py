from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from UserInmobiliaria.forms import UserRegisterForm, AvatarForm
from UserInmobiliaria.models import Avatar

def upload_avatar(request):
    if request.method == "POST":

        formulario = AvatarForm(request.POST, request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data
            avatar = Avatar.objects.filter(user=data.get("usuario"))

            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data["imagen"]
                avatar.save()

            else:
                avatar = Avatar(user=data.get("user"), imagen=data.get("imagen"))
                avatar.save()

        return redirect("Inicio")

    contexto = {
        "form": AvatarForm(),
        'boton_envio': 'Crear'
    }
    return render(request, "base_formulario.html", contexto)

@login_required
def editar_usuario(request):
    usuario = request.user

    if request.method == 'POST':

        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            usuario.username = data.get('username')
            usuario.email = data.get('email')
            usuario.last_name = data.get('last_name')

            usuario.save()

            messages.info(request, 'Tu usuario fue registrado satisfactoriamente!')
            
        else:
            messages.info(request, 'Tu usuario no puso ser registrado!')

        return redirect('Inicio')

    contexto = {
        #'form': UserCreationForm(),
        'form': UserRegisterForm(
            initial={
                'username': usuario.username,
                'email': usuario.email,
                'last_name': usuario.last_name
            }
            ),
        'nombre_form': 'Registro'
    }

    return render(request, 'UserInmobiliaria/login.html', contexto)

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data #dict(username :'asd', password: 'asd')

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)
                messages.info(request, 'Inicio de sesion satisfactorio!')

            else:
                messages.info(request, 'Verificar usuario o contrasenia!')
        else:
            messages.info(request, 'Inicio de sesion fallido!')

        return redirect('Inicio')

    contexto = {
        'form': AuthenticationForm(),
        'nombre_form': 'Login'
    }
    return render(request, 'UserInmobiliaria/login.html', contexto)

def register(request):
    if request.method == 'POST':

        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()

            messages.info(request, 'Tu usuario fue registrado satisfactoriamente!')
        else:
            messages.info(request, 'Tu usuario no puso ser registrado!')
        return redirect('Inicio')

    contexto = {
        #'form': UserCreationForm(),
        'form': UserRegisterForm(),
        'nombre_form': 'Registro'
    }

    return render(request, 'UserInmobiliaria/login.html', contexto)