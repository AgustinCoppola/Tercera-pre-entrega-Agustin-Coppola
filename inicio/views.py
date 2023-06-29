from django.shortcuts import render
from inicio.forms import CrearDjuserForm
from inicio.models import DjUser

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def crear_djuser(request):
    mensaje = ''

    if request.method == 'POST':
        formulario = CrearDjuserForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            djuser = DjUser(nombre=info['nombre'],edad=info['edad'],fecha_nacimiento=info['fecha_nacimiento'])
            djuser.save()
            mensaje = f'Se creó el DjUser {djuser.nombre}'
        else:
            return render(request, 'inicio/crear_djuser.html', {'formulario': formulario})  

    formulario = CrearDjuserForm()
    return render(request, 'inicio/crear_djuser.html', {'formulario': formulario, 'mensaje': mensaje})
