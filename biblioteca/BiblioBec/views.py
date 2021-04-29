from django.shortcuts import render
from .forms import DocumentoForm , EjemplarForm
from django.http import HttpResponse
from .models import Libro
from django.db import connection
import cx_Oracle
import base64
from django.core.files.base import ContentFile
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

def form_doc(request):
    data = {
        'form': DocumentoForm(),
        "doc": lista_doc()

    }
    return render(request, 'documento/create_doc.html', data)

def create_doc(request):
    #return HttpResponse(request.POST.get('autor',''))
    #return HttpResponse(request.FILES['imagen'])
    if request.method == 'POST':
        isbn = request.POST.get('isbn','')
        titulo = request.POST.get('titulo','')
        autor = request.POST.get('autor','')
        editorial = request.POST.get('editorial','')
        fecha = request.POST.get('fecha_publicacion','')
        categoria = request.POST.get('categoria_id_cate','')
        tipo_doc = request.POST.get('tipo_documento_id_tipo_doc','')
        tipo_me = request.POST.get('tipo_medio','')
        edi = request.POST.get('edicion','')
        imagen = request.FILES['imagen'].read()

        """
        isbn = HttpResponse(request.POST.get('isbn',''))
        titulo = HttpResponse(request.POST.get('titulo',''))
        autor = HttpResponse(request.POST.get('autor',''))
        editorial = HttpResponse(request.POST.get('editorial',''))
        fecha = HttpResponse(request.POST.get('fecha_publicacion',''))
        categoria = HttpResponse(request.POST.get('categoria_id_cate',''))
        tipo_doc = HttpResponse(request.POST.get('tipo_documento_id_tipo_doc',''))
        tipo_me = HttpResponse(request.POST.get('tipo_medio',''))
        edi = HttpResponse(request.POST.get('edicion',''))
        """
    
        agregar_documento(isbn,titulo,autor,editorial,fecha,categoria,tipo_doc,tipo_me,edi,imagen)
        data = {
            'form': DocumentoForm(),
            "doc": lista_doc()

        }
    return render(request,'documento/create_doc.html',data)


def agregar_documento(isbn,titulo,autor,editorial,fecha,categoria,tipo_doc,tipo_me,edi,imagen):
    cursor_dj = connection.cursor()
    cursor_ex = cursor_dj.connection.cursor() 
    salida = cursor_ex.var(cx_Oracle.NUMBER)
    cursor_ex.callproc('P_AGREGAR_DOCUMENTO',[isbn,titulo,autor,editorial,fecha,categoria,tipo_doc,tipo_me,edi,imagen,salida])


def lista_doc():

    cursor_dj = connection.cursor()
    cursor_ex = cursor_dj.connection.cursor() 
    cursor_out= cursor_dj.connection.cursor() 
    cursor_ex.callproc('P_LISTA_DOCUMENTOS',[cursor_out])

    documentos = []
    for i in cursor_out:
        documentos.append(        {
            'data':i,
            'imagen':str(base64.b64encode(i[9].read()),'utf-8')
        })
    
    return documentos


