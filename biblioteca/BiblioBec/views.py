from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import DocumentoForm , EjemplarForm, UsuarioForm, ReservaForm, formLogin
from django.http import HttpResponse
from .models import Libro, Usuario, Ejemplar
from django.db import connection
import cx_Oracle
import base64
from django.core.files.base import ContentFile
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def index(request):
   
    data = { 
        'libros': lista_doc()
    }
    return render(
        request,
        'catalogo.html',
        data,
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
   
    data = {
        'pres': lista_pres()
    }
    return render(
        request,
        'solicitudes.html',data
    )

# vistas de documentos

def form_cr_doc(request):
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
            

            agregar_documento(isbn,titulo,autor,editorial,fecha,categoria,tipo_doc,tipo_me,edi,imagen,ubi,stock)
            data = {
                'libros': lista_doc(),
                "msj": "exi_create",

            }
            messages.success(request, "Documento Creado Correctamente./success")
            return redirect('catalogo')
    except:
        data = {
                'libros': lista_doc(),
                #"msj": "error_create",

            }
        messages.error(request, "lo sentimos ha ocurrido un error./error")
        return redirect('form_doc')
    
def agregar_documento(isbn,titulo,autor,editorial,fecha,categoria,tipo_doc,tipo_me,edi,imagen,ubi,stock):
    cursor_dj = connection.cursor()
    cursor_ex = cursor_dj.connection.cursor() 
    salida = cursor_ex.var(cx_Oracle.NUMBER)
    cursor_ex.callproc('P_AGREGAR_DOCUMENTO',[isbn,titulo,autor,editorial,fecha,categoria,tipo_doc,tipo_me,edi,imagen,ubi,stock,salida])

def delete_doc(request,isbn):

    doc = get_object_or_404(Libro,isbn=isbn)
    cursor_dj = connection.cursor()
    cursor_ex = cursor_dj.connection.cursor() 
    cursor_ex.callproc('SP_DELETE_EJEMPLAR',[isbn])
    doc.delete()
    data = {
                'libros': lista_doc(),
                "msj": "exi_delete",

            }
    messages.success(request, "Documento Eliminado./success")
    return redirect('catalogo')

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

def update_doc(request):

    try:
        if request.method == 'POST':
            isbn = request.POST.get('isbn','')
            titulo = request.POST.get('titulo','')
            autor = request.POST.get('autor','')
            editorial = request.POST.get('editorial','')
            fecha = request.POST.get('fecha_publicacion','')
            cat = request.POST.get('categoria_id_cate','')
            doc = request.POST.get('tipo_documento_id_tipo_doc','')
            medio = request.POST.get('tipo_medio','')
            edi = request.POST.get('edicion','')
            opcion = request.POST.get('opcion')
            if opcion == 'a':
                imagen = request.FILES['imagen'].read()
            else: 
                with open('BiblioBec/static/img/user-5.jpg','rb') as image_file:
                    imagen = image_file.read()
            ubi = request.POST.get('ubicacion')
            #return HttpResponse(opcion)

            editar_documento(isbn,titulo ,autor ,editorial ,fecha ,cat,doc,medio,edi,imagen ,ubi,opcion)
            messages.success(request, "Documento Editado Correctamente./success")
            return redirect('catalogo')
    except:
        messages.error(request, "lo sentimos ha ocurrido un error./error")
        return redirect('catalogo')
    

def editar_documento(isbn,titulo ,autor ,editorial ,fecha ,cat,doc,medio,edi,imagen ,ubi,opcion):
    cursor_dj = connection.cursor()
    cursor_ex = cursor_dj.connection.cursor() 
    salida = cursor_ex.var(cx_Oracle.NUMBER)
    cursor_ex.callproc('SP_EDITAR_DOCUMENTO',[isbn,titulo ,autor ,editorial ,fecha ,cat,doc,medio,edi,imagen ,ubi,opcion,salida])
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
    '''
    Valida que se acceda a la vista solo los usuarios con sesión y con privilegios
    '''
    #Validar si existe la sesión
    if not request.session._session:
        print('entra al empty')
        return redirect('index')

    #Validar que el usuario no acceda a la vista si no es tipo administrador o bibliotecario
    if request.session['user_login']['user']['tipo'] == 3:
        return redirect('index')
        
    lista = lista_usuarios()
    if request.method == 'GET':
        paginator = Paginator(lista, 5) 
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

        if len(usuario_encontrado) < 1:
            messages.success(request, "Usuario no encontrado./error")
            return redirect('usuario_list')

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
        tipo_usuario_id_tipo = request.POST.get('tipo_usuario_id_tipo')
        password = request.POST.get('password')
        if 'foto' in request.FILES:
            foto = request.FILES['foto'].read()
        else:
            with open('BiblioBec/static/img/user-5.jpg','rb') as image_file:
                foto = image_file.read()
        if 'huella' in request.FILES:
            huella = request.FILES['huella'].read()
        else:
            with open('BiblioBec/static/img/no-imagen-user.jpg','rb') as image_file:
                huella = image_file.read()
        resp = agregar_usuario(rut_usr, nombre, apellido_p, apellido_m, direccion,
                                   telefono, correo, foto, huella, tipo_usuario_id_tipo, password)
        if resp == 1:
            messages.success(request, "Usuario registrado correctamente./success")
            return redirect('usuario_list')
        else:
            messages.success(request, "No se pudo registrar al usuario./error")
            return redirect('usuario_create')
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
    rut_usr = request.GET.get('rut_usr') if request.method == "GET" else request.POST.get('rut_usr')
    data = {
        'usuario': usuario_filtrado(rut_usr)
    }
    if request.method == "GET":
        return render(request, 'Bibliobec/usuario_update.html', data)
    else:
        foto = None
        huella = None
        if 'foto' in request.FILES:
            foto = request.FILES['foto'].read()
        else:
            if not data['usuario'][0]['data'][7]:
                with open('BiblioBec/static/img/user-5.jpg','rb') as image_file:
                    foto = image_file.read()
            else:
                foto = data['usuario'][0]['data'][7]
        
        if 'huella' in request.FILES:
            huella = request.FILES['huella'].read()
        else:
            if not data['usuario'][0]['data'][8]:
                with open('BiblioBec/static/img/no-imagen-user.jpg','rb') as image_file:
                    huella = image_file.read()
            else:
                huella = data['usuario'][0]['data'][8]
        rut_usr = request.POST.get('rut_usr')
        nombre = request.POST.get('nombre')
        apellido_p = request.POST.get('apellido_p')
        apellido_m = request.POST.get('apellido_m')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        tipo_usuario_id_tipo = request.POST.get('tipo_usuario_id_tipo')
        password = request.POST.get('password')
        resp = usuario_update(rut_usr, nombre, apellido_p, apellido_m, direccion,
                                   telefono, correo, foto, huella, tipo_usuario_id_tipo, password)
        if resp == 1:
            messages.success(request, "Usuario actualizado correctamente./success")
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
            messages.error(request, "No se pudo actualizar el usuario./error")
            return render(request, 'Bibliobec/usuario_update.html', data)

def eliminar_usuario(request):
    rut_usr = request.GET.get('rut_usr')

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor.callproc('SP_USUARIO_DELETE',[rut_usr])
    messages.success(request, "Usuario eliminado correctamente./success")
    return redirect('usuario_list')

# Inicio de sesión
def iniciar_sesion(request):
    if request.method == 'POST':
        formulario = formLogin(request.POST)
        if formulario.is_valid:
            usuario = request.POST.get('rut_usr')
            password = request.POST.get('password')
            verificacion = Usuario.objects.filter(rut_usr = usuario, password = password).exists()
            
        if verificacion == True:
            usuario = usuario_filtrado(usuario)
            request.session['user_login'] = {'user': {'foto':usuario[0]['foto'],'rut_usr':usuario[0]['data'][0], 
            'nombre':usuario[0]['data'][1], 'apellido':usuario[0]['data'][2], 'tipo':usuario[0]['data'][9], 'tipo_desc':usuario[0]['data'][11].title()}}
            return redirect('index')
        else:
            messages.success(request, "Usuario o contraseña incorrecta, por favor intente nuevamente./error")
            return render(request, 'session/login.html')
    else:
        formulario = formLogin()
    return render(request, 'session/login.html', {'formulario': formulario})

def logout(request):
    try:
        del request.session['user_login']
    except KeyError:
        pass
    return redirect('index')

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

# VISTAS DE SOLICITUD DOCUMENTO

def solicitud_prestamo(request):
    rut = request.POST.get('rut','')
    isbn = request.POST.get('isbn','')
    
    data={
        'num' : num_ejem_dis(isbn),
        'ejem': id_ejem(isbn),
        'doc': filtro_doc(isbn),
        'rut': rut,
    }
    return render(request,'prestamo.html',data)

def proceso_prestamo(request):
    rut = request.POST.get('rut','')
    id_ejem = request.POST.get('id_ejem','')
    isbn = request.POST.get('isbn','')
    tipo = request.POST.get('tipo','')
    
    sp(rut, id_ejem, isbn, tipo)
    messages.success(request, "Solicitud Procesada correctamente Dirijase al mesón de ayuda para retirar el documento./success")
    return redirect('catalogo')


def sp(rut,id_ejem,isbn,tipo):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("p_solicitud_prestamo", [rut,id_ejem,isbn,tipo])

def num_ejem_dis(isbn):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("sp_num_ejemplar_disponible", [isbn,out_cur])

    lista = []

    for i in out_cur:
        lista.append({
            'data':i
        })
    
    return lista

def id_ejem(isbn):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("sp_ejemplar", [isbn,out_cur])

    lista = []

    for i in out_cur:
        lista.append({
            'data':i
        })
    
    return lista

def lista_pres():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("sp_prestamos", [out_cur])

    lista = []

    for i in out_cur:
        lista.append({
            'data':i
        })
    
    return lista