from django.shortcuts import render, redirect
from .models import Termino

def agregar_termino(request):
    if request.method == 'POST':
        term = request.POST.get('term')
        definition = request.POST.get('definition')
        Termino.objects.create(term=term, definition=definition)
        return redirect('lista_terminos')
    return render(request, 'diccionario/agregar_termino.html')

def home(request):
    return render(request, 'home.html')

def dictionary(request):
    # Lógica para interactuar con el diccionario
    return render(request, 'dictionary.html')
