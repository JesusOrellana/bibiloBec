from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import DocumentoForm , EjemplarForm, UsuarioForm, ReservaForm
from django.http import HttpResponse
from .models import Libro, Usuario
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
    data = { 
        'libros': lista_doc()
    }
    return render(
        request,
        'catalogo.html',
        data,
    )

def catalogo_audio(request):
    data = { 
        'audios': listado_audios()
    }
    return render(
        request,
        'libros/catalogo_audio.html',
        data
    )

def catalogo_video(request):
    data = { 
        'videos': listado_videos()
    }
    return render(
        request,
        'libros/catalogo_videos.html',
        data
    )

def catalogo_libro(request):
    data = { 
        'libro': listado_libro()
    }
    return render(
        request,
        'libros/catalogo_libros.html',
        data
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
        'form2':EjemplarForm(),
        "doc": lista_doc(),
        "msj": "sin mensaje"

    }
    return render(request, 'documento/create_doc.html', data)

def create_doc(request):
    #return HttpResponse(request.POST.get('autor',''))
    #return HttpResponse(request.FILES['imagen'])
    try:
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
            ubi = request.POST.get('ubicacion')
            estado = request.POST.get('estado')
            stock = request.POST.get('stock')
            

            agregar_documento(isbn,titulo,autor,editorial,fecha,categoria,tipo_doc,tipo_me,edi,imagen,estado,ubi,stock)
            data = {
                'form': DocumentoForm(),
                "doc": lista_doc(),
                "msj": "exi_create",

            }
            return render(request,'documento/create_doc.html',data)
    except:
        data = {
                'form': DocumentoForm(),
                "doc": lista_doc(),
                "msj": "error_create",

            }
        return render(request,'documento/create_doc.html',data)

def agregar_documento(isbn,titulo,autor,editorial,fecha,categoria,tipo_doc,tipo_me,edi,imagen,estado,ubi,stock):
    cursor_dj = connection.cursor()
    cursor_ex = cursor_dj.connection.cursor() 
    salida = cursor_ex.var(cx_Oracle.NUMBER)
    cursor_ex.callproc('P_AGREGAR_DOCUMENTO',[isbn,titulo,autor,editorial,fecha,categoria,tipo_doc,tipo_me,edi,imagen,estado,ubi,stock,salida])


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

def form_up_doc(request,isbn):
    data = {
        'form': DocumentoForm(),
        'doc': filtro_doc(isbn)
    }
    return render(request, 'documento/update_doc.html', data)

# Listado de libros - catalogo
def listado_audios():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_AUDIOS", [out_cur])

    lista = []

    for i in out_cur:
        lista.append(        {
            'data':i,
            'imagen':str(base64.b64encode(i[9].read()),'utf-8')
        })
    
    return lista

def listado_videos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_VIDEOS", [out_cur])

    lista = []

    for i in out_cur:
        lista.append(        {
            'data':i,
            'imagen':str(base64.b64encode(i[9].read()),'utf-8')
        })
    
    return lista

def listado_libro():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_LIBRO", [out_cur])

    lista = []

    for i in out_cur:
        lista.append(        {
            'data':i,
            'imagen':str(base64.b64encode(i[9].read()),'utf-8')
        })
    
    return lista

def filtro_doc(isbn):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("P_FITRO_DOC", [isbn,out_cur])

    lista = []

    for i in out_cur:
        lista.append({
            'data':i,
            'imagen':str(base64.b64encode(i[9].read()),'utf-8')
        })
    
    return lista

# Usuario
def usuarios(request):
    lista = lista_usuarios()
    if request.method == 'GET':
        paginator = Paginator(lista, 6) 
        page_number = request.GET.get('page')
        usuario_filtrado = paginator.get_page(page_number)
        data = { 
                'page_obj': usuario_filtrado
            }
        return render(
            request,
            'Bibliobec/usuario_list.html',
            data
        )
    else:
        rut_usr_a_buscar = request.POST.get('rut_usr')
        usuario_encontrado = []
        for u in lista:
            if u['data'][0] == rut_usr_a_buscar:
                usuario_encontrado.append(u)
                break   
        return render(
            request,
            'Bibliobec/usuario_list.html',
            {'page_obj': usuario_encontrado}
        )

def form_usuario(request):
    data = {
        'form': UsuarioForm(),
        'usuarios': lista_usuarios()
    }
    if request.method == "POST":
        rut_usr = request.POST.get('rut_usr')
        nombre = request.POST.get('nombre')
        apellido_p = request.POST.get('apellido_p')
        apellido_m = request.POST.get('apellido_m')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        with open('BiblioBec/static/img/user-5.jpg','rb') as image_file:
            foto = image_file.read()
        with open('BiblioBec/static/img/no-imagen-user.jpg','rb') as image_file:
            huella = image_file.read()
        tipo_usuario_id_tipo = request.POST.get('tipo_usuario_id_tipo')
        password = request.POST.get('password')
        resp = agregar_usuario(rut_usr, nombre, apellido_p, apellido_m, direccion,
                                   telefono, correo, foto, huella, tipo_usuario_id_tipo, password)
        if resp == 1:
            return redirect('usuario_list')
    return render(request, 'Bibliobec/usuario_form.html', data)

def agregar_usuario(rut_usr, nombre, apellido_p, apellido_m, direccion, telefono, correo, foto, huella, tipo_usuario_id_tipo, password):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_USUARIO_INSERT', [rut_usr, nombre, apellido_p, apellido_m, direccion, telefono, correo, foto, huella, 
                                         tipo_usuario_id_tipo, password, salida])
    return salida.getvalue()

def lista_usuarios():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor_out= django_cursor.connection.cursor()
    cursor.callproc('SP_LISTAR_USUARIOS',[cursor_out])

    usuarios = []
    for i in cursor_out:
        datau = {'data': '', 'foto': '', 'huella': '' }
        datau['data'] = i
        if (i[7]):
            datau['foto'] = str(base64.b64encode(i[7].read()),'utf-8')
        
        if (i[8]):
            datau['huella'] = str(base64.b64encode(i[8].read()),'utf-8')

        usuarios.append(datau)
    return usuarios

def usuario_filtrado(rut_usr):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor_out = django_cursor.connection.cursor()
    cursor.callproc('SP_FILTRAR_USUARIO_POR_RUT',[rut_usr, cursor_out])
        
    usuarios = []
    for i in cursor_out:
        datau = {'data': '', 'foto': '', 'huella': '' }
        datau['data'] = i
        if (i[7]):
            datau['foto'] = str(base64.b64encode(i[7].read()),'utf-8')
            
        if (i[8]):
            datau['huella'] = str(base64.b64encode(i[8].read()),'utf-8')

        usuarios.append(datau)
    return usuarios

def usuario_update(rut_usr, nombre, apellido_p, apellido_m, direccion, telefono, correo, foto, huella, tipo_usuario_id_tipo, password):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_USUARIO_UPDATE',[rut_usr, nombre, apellido_p, apellido_m, direccion, telefono, correo, foto, huella, 
                                         tipo_usuario_id_tipo, password, salida])
    return salida.getvalue()

def editar_usuario(request):
    rut_usr = request.GET.get('rut_usr')
    data = {
        'usuario': usuario_filtrado(rut_usr),
        'mensajeError': None
    }
    if request.method == "GET":
        return render(request, 'Bibliobec/usuario_update.html', data)
    else:
        with open('BiblioBec/static/img/user-5.jpg','rb') as image_file:
            foto = image_file.read()
        with open('BiblioBec/static/img/no-imagen-user.jpg','rb') as image_file:
            huella = image_file.read()
        rut_usr = request.POST.get('rut_usr')
        nombre = request.POST.get('nombre')
        apellido_p = request.POST.get('apellido_p')
        apellido_m = request.POST.get('apellido_m')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        if 'foto' in request.FILES:
            foto = request.FILES['foto'].read()
        if 'huella' in request.FILES:
            huella = request.FILES['huella'].read()
        tipo_usuario_id_tipo = request.POST.get('tipo_usuario_id_tipo')
        password = request.POST.get('password')
        resp = usuario_update(rut_usr, nombre, apellido_p, apellido_m, direccion,
                                   telefono, correo, foto, huella, tipo_usuario_id_tipo, password)
        if resp == 1:
            return redirect('usuario_list')
        else:
            data = {'usuario': [{'data': {}}]}
            data['usuario'][0]['data'][0] = rut_usr
            data['usuario'][0]['data'][1] = nombre
            data['usuario'][0]['data'][2] = apellido_p
            data['usuario'][0]['data'][3] = apellido_m
            data['usuario'][0]['data'][4] = direccion
            data['usuario'][0]['data'][5] = telefono
            data['usuario'][0]['data'][6] = correo
            data['usuario'][0]['data'][7] = foto
            data['usuario'][0]['data'][8] = huella
            data['usuario'][0]['data'][9] = tipo_usuario_id_tipo
            data['usuario'][0]['data'][10] = password
            data['mensajeError'] = "No se pudo actualizar el usuario."
            return render(request, 'Bibliobec/usuario_update.html', data)


def eliminar_usuario(request):
    rut_usr = request.GET.get('rut')

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor.callproc('SP_USUARIO_DELETE',[rut_usr])
    return redirect('usuario_list')


    #vista para reserva 
def vista_reserva(request,isbn):
    data = { 
        'form': ReservaForm(), 
        "doc" : filtro_res(isbn)
    }
    return render(
    request,
    'reserva/reserva.html',
    data
    )

def filtro_res(isbn):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("P_FITRO_RES", [isbn,out_cur])

    lista = []

    for i in out_cur:
        lista.append({
            'data':i
        })
    
    return lista