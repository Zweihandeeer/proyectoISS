from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from importlib.resources import path
from django.shortcuts import render
from iss.models import Cartas, Observaciones
from iss.forms import ObservacionesForm, LoginForm
import sys

def home(request):    
    # Validación de la sesión inexistente.
    if not request.session.has_key('username'):
        # Si la sesión no existe, entonces me lleva de vuelta al login.
        return HttpResponseRedirect('/login')
    # Captura del usuario que actualmente levantó la sesión.
    username = request.session['username']
    # Variables que almacenan los datos a utilizar en el historial de chats.
    context = {
        "username": username
    }  
    return render(request, 'proyectoiss/coachview.html', context=context)


# Método de inicio de sesión al sistema.
def login(request):
    # Verificar que no exista la sesión
    if request.session.has_key('username'):
        # Si la sesión existe, entonces me lleva al home
        return HttpResponseRedirect('/coach')
    else:
        # Si la sesión no existe, verifica el formulario
        if request.method == 'POST':
            # Si se recibe el formulario
            usuario = LoginForm(request.POST)
            if usuario.is_valid():
                # Si el formulario es válido, se verifican los datos
                username = usuario.cleaned_data['email']
                password = usuario.cleaned_data['password']
                # Usa la función authenticate de django.contrib.auth
                usuario = authenticate(username=username, password=password)
                if usuario is not None:
                    # Si los datos son válidos, crea la sesión
                    request.session['username'] = usuario.username
                    return HttpResponseRedirect('/coach')
        else:
            # Si no estamos recibiendo el formulario, entonces envíamos uno vacío
            usuario = LoginForm()
    return render(request, 'iss/login.html', {'usuario': usuario})

# Método de ingreso de chats al sistema y a la BD.
def nuevas_observaciones(request):
    # Verificar que no exista la sesión
    if not request.session.has_key('username'):
        # Si la sesión no existe, entonces me lleva al login
        return HttpResponseRedirect('/coach')
    # Captura del actual usuario en la sesión.
    username = request.session['username']
    # Uso del método POST para rellenar el form de chat.
    if request.method == 'POST':
        observaciones = ObservacionesForm(request.POST)
        if observaciones.is_valid: 
            observaciones.save()
            return HttpResponseRedirect('/coachobservaciones')
    else:
        observaciones = ObservacionesForm()

    return render(request, 'iss/coachingresarobservacionesview.html', {'observaciones': observaciones, 'username': username,})

def coach(request):
    cartas = Cartas.objects.all()
    return render(request, "coachview.html", { 'cartas': cartas })

def observaciones(request):
    observaciones = Observaciones.objects.all()
    return render(request, "coachobservacionesview.html", { 'observaciones': observaciones })

def player(request):
    return render(request, "playerview.html")

def cmatchup(request):
    return render(request, "coachmatchup.html")

def coachview2(request):
    return render(request, "coachview2.html")