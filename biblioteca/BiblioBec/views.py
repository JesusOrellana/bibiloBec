from django.shortcuts import render
from .forms import CategoriaForm
# Create your views here.

def index(request):
   
    return render(
        request,
        'index.html',
    )

def catalogo(request):
   
    return render(
        request,
        'catalogo.html',
    )

def solicitudes(request):
   
    return render(
        request,
        'solicitudes.html',
    )

# vistas de documentos

def create_doc(request):
    data = {
        'form': CategoriaForm
    }
    return render(request, 'documento/create_doc.html', data)