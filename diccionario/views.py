from django.shortcuts import render, redirect
from .models import Termino

def home(request):
    return render(request, 'home.html')

def lista_terminos(request):
    terminos = Termino.objects.all()
    return render(request, 'diccionario_list.html', {'termino': terminos})

#def agregar_termino(request):
    if request.method == 'POST':
        term = request.POST.get('term')
        definition = request.POST.get('definicion')
        Termino.objects.create(term=term, definition=definition)
        return redirect('lista_terminos')
    return render(request, 'agregar_termino.html')