from django.shortcuts import render
from sistema.models import Prueba

def home(request):
    nombre = "Elias"
    edad = 25

    #if request.method == 'POST':
        #nombreForm = request.POST.get('nombreForm')
        #apellidoForm = request.POST.get('apellidoForm')

        #prueba = Prueba(nombre=nombreForm, apellido=apellidoForm)
        #prueba.save()

    #return render(request, 'index.html', {'nombre': nombre, 'edad': edad})