from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import DocumentoForm , EjemplarForm, UsuarioForm, ReservaForm, formLogin
from django.http import HttpResponse, JsonResponse
from .models import Libro, Usuario, Ejemplar
from django.db import connection
import cx_Oracle
import base64
from django.core.files.base import ContentFile
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .utils import validarRut, cifrarPassword
from datetime import datetime
# Create your views here.
#Fecha actual

#API
def APILogin(request, rut_usr, password):
    usuarios = Usuario.objects.all()
    if not rut_usr:
        return JsonResponse({'success':False, 'error': "Debe ingresar el rut"})
    if not password:
        return JsonResponse({'success':False, 'error': "Debe ingresar la contraseña"})
        
    password_cifrada = cifrarPassword(password)
    verificar = usuarios.filter(rut_usr__contains = rut_usr, password = password_cifrada).exists()

    if verificar:
        usuario = usuario_filtrado(rut_usr)
        return JsonResponse({'success':True, 'data': {'rut_usr':usuario[0]['data'][0], 'nombre':usuario[0]['data'][1].title(), 
        'apellido_p':usuario[0]['data'][2].title(), 'apellido_m':usuario[0]['data'][3].title(), 'direccion':usuario[0]['data'][4].title(), 
        'telefono':usuario[0]['data'][5], 'correo':usuario[0]['data'][6], 'tipo_usuario':usuario[0]['data'][15].title(), 
        'password':usuario[0]['data'][10], 'foto': usuario[0]['foto'], 'huella':usuario[0]['huella']}})
    else:
        return JsonResponse({'success':False, 'error': "Usuario o contraseña incorrecto"})

def APIDocumentos(request):
    lista = lista_doc()
    documentos = []
    for documento in lista:
        documentoJson = {'id': documento['data'][0], 'titulo': documento['data'][1].title(), 
        'autor': documento['data'][2].title(), 'editorial': documento['data'][11].title(), 'imagen': documento['imagen']}
        documentos.append(documentoJson)
    return JsonResponse({'data' : documentos})

def APIPrestamos(request, rut_usr):
    usuario = usuario_filtrado(rut_usr)
    tipo_usuario = usuario[0]['data'][9]
    lista = None
    
    if tipo_usuario == 1 or tipo_usuario == 2:
        lista = lista_pres()
    else:
        lista = pres_filtrado_rut_usr(rut_usr)

    prestamos = []
    for pres in lista:
        prestamoJson = {'numero_pres':pres['data'][13],'rut_usr': pres['data'][0], 'nombre_usr': pres['data'][1].title(), 'tipo_pres': pres['data'][2].title(), 
        'documento':pres['data'][3].title(), 'autor':pres['data'][4].title(), 'editorial':pres['data'][19].title(), 'tipo_doc':pres['data'][6].title(),
        'fecha_pres':pres['data'][8], 'fecha_dev':pres['data'][10], 'estado': pres['data'][20].title()}
        prestamos.append(prestamoJson)

    return JsonResponse({'data' : prestamos})

def catalogo(request): 
    lista = lista_doc()
    if request.method == 'POST':
        documento = request.POST.get('documento')
        documento_encontrado = []
        for d in lista:
            if d['data'][1].upper().find(documento.upper()) != -1 or d['data'][2].upper().find(documento.upper()) != -1 or d['data'][10].upper().find(documento.upper()) != -1:
                documento_encontrado.append(d)
                # break / con este break solo muestra el primer resultado, no muestra si hay repetidos
        if len(documento_encontrado) < 1:
            messages.error(request, "Documento no encontrado./error")            
            return redirect('catalogo')
        lista = documento_encontrado
    paginator = Paginator(lista, 15) 
    page_number = request.GET.get('page')
    libros_page = paginator.get_page(page_number)
    now = datetime.now().strftime('%d/%m/%Y')
    try:
        
        rut = request.session['user_login']['user']['rut_usr']
        data = { 
            'libros': libros_page,
            'page_obj' : libros_page,
            'sansion': catalogo_sansion(rut),
            'fecha': now
        }
        return render(
            request,
            'catalogo.html',
            data,
        )
    except:
        
        data = { 
            'libros': libros_page,
            'page_obj' : libros_page,
            'sansion': 'no',
            'fecha': now
        }
        return render(
            request,
            'catalogo.html',
            data,
        )

def catalogo_audio(request):
    lista = listado_audios()
    if request.method == 'POST':
        documento = request.POST.get('documento')
        documento_encontrado = []
        for d in lista:
            if d['data'][1].upper().find(documento.upper()) != -1 or d['data'][2].upper().find(documento.upper()) != -1 or d['data'][10].upper().find(documento.upper()) != -1:
                documento_encontrado.append(d)
                # break / con este break solo muestra el primer resultado, no muestra si hay repetidos
        if len(documento_encontrado) < 1:
            messages.error(request, "Documento no encontrado./error")            
            return redirect('catalogo')
        lista = documento_encontrado
    paginator = Paginator(lista, 15) 
    page_number = request.GET.get('page')
    audios_page = paginator.get_page(page_number)

    try:
        rut = request.session['user_login']['user']['rut_usr']
        data = { 
            'audios': audios_page,
            'page_obj': audios_page,
            'sansion': catalogo_sansion(rut)
        }
        return render(
            request,
            'libros/catalogo_audio.html',
            data
        )
    except:
    
        data = { 
            'audios': audios_page,
            'page_obj': audios_page,
            'sansion': 'no'
        }
        return render(
            request,
            'libros/catalogo_audio.html',
            data
        )

def catalogo_video(request):
    lista = listado_videos()
    if request.method == 'POST':
        documento = request.POST.get('documento')
        documento_encontrado = []
        for d in lista:
            if d['data'][1].upper().find(documento.upper()) != -1 or d['data'][2].upper().find(documento.upper()) != -1 or d['data'][10].upper().find(documento.upper()) != -1:
                documento_encontrado.append(d)
                # break / con este break solo muestra el primer resultado, no muestra si hay repetidos
        if len(documento_encontrado) < 1:
            messages.error(request, "Documento no encontrado./error")            
            return redirect('catalogo')
        lista = documento_encontrado
    paginator = Paginator(lista, 15) 
    page_number = request.GET.get('page')
    videos_page = paginator.get_page(page_number)

    try:
        rut = request.session['user_login']['user']['rut_usr']
        data = { 
            'videos': videos_page,
            'page_obj': videos_page,
            'sansion': catalogo_sansion(rut)
        }
        return render(
            request,
            'libros/catalogo_videos.html',
            data
        )
    except:

        data = { 
            'videos': videos_page,
            'page_obj': videos_page,
            'sansion': 'no'
        }
        return render(
            request,
            'libros/catalogo_videos.html',
            data
        )

def catalogo_libro(request):
    lista = listado_libro()
    if request.method == 'POST':
        documento = request.POST.get('documento')
        documento_encontrado = []
        for d in lista:
            if d['data'][1].upper().find(documento.upper()) != -1 or d['data'][2].upper().find(documento.upper()) != -1 or d['data'][10].upper().find(documento.upper()) != -1:
                documento_encontrado.append(d)
                # break / con este break solo muestra el primer resultado, no muestra si hay repetidos
        if len(documento_encontrado) < 1:
            messages.error(request, "Documento no encontrado./error")            
            return redirect('catalogo')
        lista = documento_encontrado
    paginator = Paginator(lista, 15) 
    page_number = request.GET.get('page')
    libro_page = paginator.get_page(page_number)
    

    try:
        rut = request.session['user_login']['user']['rut_usr']
        data = { 
            'libro': libro_page,
            'page_obj': libro_page,
            'sansion': catalogo_sansion(rut)
        }
        return render(
            request,
            'libros/catalogo_libros.html',
            data
        )
    except:
        data = { 
            'libro': libro_page,
            'page_obj': libro_page,
            'sansion': 'no'
        }
        return render(
            request,
            'libros/catalogo_libros.html',
            data
        )

def solicitudes(request):
   
    if request.session['user_login']['user']['tipo'] == 3 or request.session['user_login']['user']['tipo'] == 2 or request.session['user_login']['user']['tipo'] == 1:
        now = datetime.now().strftime('%d/%m/%Y')
        data = {
            'pres': lista_pres(),
            'res' : lista_reserva(),
            'fecha': now
            }
        return render(
            request,
            'solicitudes.html',data)
    else:
        return redirect('index')

def ayuda(request):
    return render(request, 'preguntas_frec.html')

# vistas de documentos y ejemplares

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
            stock = request.POST.get('stock')
            

            agregar_documento(isbn,titulo,autor,editorial,fecha,categoria,tipo_doc,tipo_me,edi,imagen,ubi,stock)
            data = {
                'libros': lista_doc(),
                "msj": "exi_create",

            }
            messages.success(request, "Documento creado correctamente./success")
            return redirect('catalogo')
    except:
        data = {
                'libros': lista_doc(),
                #"msj": "error_create",

            }
        messages.error(request, "Lo sentimos, ha ocurrido un error./error")
        return redirect('form_doc')
    
def agregar_documento(isbn,titulo,autor,editorial,fecha,categoria,tipo_doc,tipo_me,edi,imagen,ubi,stock):
    cursor_dj = connection.cursor()
    cursor_ex = cursor_dj.connection.cursor() 
    salida = cursor_ex.var(cx_Oracle.NUMBER)
    cursor_ex.callproc('P_AGREGAR_DOCUMENTO',[isbn,titulo,autor,editorial,fecha,categoria,tipo_doc,tipo_me,edi,imagen,ubi,stock,salida])

def num_ejem(isbn):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("SP_NUM_EJEM", [isbn,out_cur])

    lista = []

    for i in out_cur:
        lista.append({
            'data':i
        })
    
    return lista

def num_ejem_pres(isbn):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("sp_num_presta", [isbn,out_cur])

    lista = []

    for i in out_cur:
        lista.append({
            'data':i
        })
    
    return lista

def delete_doc(request,isbn):
    pres = num_ejem_pres(isbn)
    pres = pres[0]['data'][0]
    cont = num_ejem_dis(isbn)
    cont = cont[0]['data'][0]
    contTotal = num_ejem(isbn)
    contTotal = contTotal[0]['data'][0]
    if(contTotal == cont):
        if(pres <= 0):
            cursor_dj = connection.cursor()
            cursor_ex = cursor_dj.connection.cursor() 
            cursor_ex.callproc('SP_DELETE_EJEMPLAR',[isbn,0,1])
            data = {
                        'libros': lista_doc(),
                        "msj": "exi_delete",

                    }
            messages.success(request, "Documento eliminado./success")
            return redirect('catalogo')
        else:
            cursor_dj = connection.cursor()
            cursor_ex = cursor_dj.connection.cursor() 
            cursor_ex.callproc('sp_desactivar_ejemplar',[isbn,0,1,'sin motivo'])
            data = {
                        'libros': lista_doc(),
                        "msj": "exi_delete",

                    }
            messages.success(request, "Documento deshabilitado./success")
            return redirect('catalogo')
    """"
    try:
        pres = num_ejem_pres(isbn)
        pres = pres[0]['data'][0]
        cont = num_ejem_dis(isbn)
        cont = cont[0]['data'][0]
        contTotal = num_ejem(isbn)
        contTotal = contTotal[0]['data'][0]
        if(contTotal == cont):
            if(pres <= 0):
                cursor_dj = connection.cursor()
                cursor_ex = cursor_dj.connection.cursor() 
                cursor_ex.callproc('SP_DELETE_EJEMPLAR',[isbn,0,1])
                data = {
                            'libros': lista_doc(),
                            "msj": "exi_delete",

                        }
                messages.success(request, "Documento eliminado./success")
                return redirect('catalogo')
            else:
                cursor_dj = connection.cursor()
                cursor_ex = cursor_dj.connection.cursor() 
                cursor_ex.callproc('sp_desactivar_ejemplar',[isbn,0,1,'sin motivo'])
                data = {
                            'libros': lista_doc(),
                            "msj": "exi_delete",

                        }
                messages.success(request, "Documento deshabilitado./success")
                return redirect('catalogo')
        else:
           messages.error(request, "El proceso no se pudo realizar debido a que hay ejemplares de este documento en préstamo./error")
           return redirect('catalogo') 
    except:
        messages.error(request, "El proceso no se pudo realizar debido a que hay ejemplares de este documento en préstamo./error")
        return redirect('catalogo')
    """
def delete_ejemplar(request):
    id_ejem = request.POST.get('ejem')
    try:
        cursor_dj = connection.cursor()
        cursor_ex = cursor_dj.connection.cursor() 
        cursor_ex.callproc('SP_DELETE_EJEMPLAR',["sin isbn",id_ejem,2])
        return HttpResponse(1)
    except:
        return HttpResponse(2)

def desactivar_ejemplar(request):
    id_ejem = request.POST.get('ejem')
    motivo = request.POST.get('motivo')
    try:
        cursor_dj = connection.cursor()
        cursor_ex = cursor_dj.connection.cursor() 
        cursor_ex.callproc('sp_desactivar_ejemplar',["sin isbn",id_ejem,2,motivo])
        return HttpResponse(1)
    except:
        return HttpResponse(2)

def update_stock(request):
    isbn = request.POST.get('isbn')
    stock = request.POST.get('stock')
    ubi = request.POST.get('ubi')
    try:
        cursor_dj = connection.cursor()
        cursor_ex = cursor_dj.connection.cursor() 
        cursor_ex.callproc('sp_update_stock',[isbn,stock,ubi])
        return HttpResponse(1)
    except:
        return HttpResponse(2)

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
        'doc': filtro_doc(isbn),
        'ej': id_ejem(isbn,2)
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
            messages.success(request, "Documento editado correctamente./success")
            return redirect('catalogo')
    except:
        messages.error(request, "Lo sentimos, ha ocurrido un error./error")
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
        nombre_a_buscar = request.POST.get('nombre_usr')
        usuario_encontrado = []
        for u in lista:
            if rut_usr_a_buscar is not None:
                if u['data'][0] == rut_usr_a_buscar:
                    usuario_encontrado.append(u)
            else:  
                if u['data'][15].upper().find(nombre_a_buscar.upper()) != -1:
                    usuario_encontrado.append(u)

        if len(usuario_encontrado) < 1:
            messages.error(request, "Usuario no encontrado./error")            
            return redirect('usuario_list')

        return render(
            request,
            'Bibliobec/usuario_list.html',
            {'page_obj': usuario_encontrado}
        )

def enviar_email_habilitar(correo, rut_usr, nombre):
    context = {'mail': correo, 'rut_usr': rut_usr, 'nombre': nombre}
    template = get_template('correo_habilitar.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Active su cuenta para iniciar sesión en BiblioBEC',
        'BiblioBEC',
        settings.EMAIL_HOST_USER,
        to=[correo]
    )
    
    email.attach_alternative(content, 'text/html')
    return email

def enviar_email_restablecer_contrasena(correo, rut_usr, nombre):
    context = {'mail': correo, 'rut_usr': rut_usr, 'nombre': nombre}
    template = get_template('correo_restablecer_contrasena.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Restablecer contraseña',
        'BiblioBEC',
        settings.EMAIL_HOST_USER,
        to=[correo]
    )
    
    email.attach_alternative(content, 'text/html')
    return email

def form_usuario(request):
    if not request.session._session:
        return redirect('index')

    if  not request.session['user_login']['user']['tipo'] == 1:
        return redirect('index')
    data = {
        'form': UsuarioForm(),
        'usuarios': lista_usuarios()
    }
    if request.method == "POST":
        rut_usr = request.POST.get('rut_usr')
        if not validarRut(rut_usr):
            messages.error(request, 'El RUT ingresado no es válido./error')
            return render(request, 'Bibliobec/usuario_form.html', data)
        nombre = request.POST.get('nombre')
        apellido_p = request.POST.get('apellido_p')
        apellido_m = request.POST.get('apellido_m')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        tipo_usuario_id_tipo = request.POST.get('tipo_usuario_id_tipo')
        password = request.POST.get('password')
        password_cifrada = cifrarPassword(password)
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
                                   telefono, correo, foto, huella, tipo_usuario_id_tipo, password_cifrada)
        if resp == 1:
            resp = enviar_email_habilitar(correo, rut_usr, nombre)
            resp.send()
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

def usuario_update(rut_usr, nombre, apellido_p, apellido_m, direccion, telefono, correo, foto, huella, tipo_usuario_id_tipo):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_USUARIO_UPDATE',[rut_usr, nombre, apellido_p, apellido_m, direccion, telefono, correo, foto, huella, 
                                          tipo_usuario_id_tipo, salida])
    return salida.getvalue()

def enviar_correo_restablecer_contrasena(request):
    if request.method == "POST":
        rut_usr = request.POST.get('rut_usr')
        usuario = usuario_filtrado(rut_usr)
        correo = usuario[0]['data'][6]
        nombre = usuario[0]['data'][1]
        resp = enviar_email_restablecer_contrasena(correo, rut_usr, nombre)
        resp.send()
        messages.success(request, 'Por favor revise su correo para restablecer su contraseña./success')
        return redirect('index')
    return render(request, 'session/form_restablecer_contrasena.html')

def editar_usuario(request):
    if not request.session._session:
        return redirect('index')
    
    if not request.session['user_login']['user']['tipo'] == 1:
        return redirect('index')

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
        resp = usuario_update(rut_usr, nombre, apellido_p, apellido_m, direccion,
                                   telefono, correo, foto, huella, tipo_usuario_id_tipo)
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
            messages.error(request, "No se pudo actualizar el usuario./error")
            return render(request, 'Bibliobec/usuario_update.html', data)

def eliminar_usuario(request):
    
    rut_usr = request.GET.get('rut_usr')
    pres = pres_filtrado_rut_usr(rut_usr)
    if request.session['user_login']['user']['rut_usr'] == rut_usr:
        messages.error(request, 'No se puede desactivar el usuario logueado./error')
        return redirect('usuario_list')
    if pres:
        if pres[0]['data'][15] == 1 or pres[0]['data'][15] == 2:
            messages.error(request, 'No se puede desactivar el usuario debido a que tiene préstamos en curso./error')
            return redirect('usuario_list')
        else:
            resp = delete_usuario(rut_usr)
            messages.success(request, "Usuario desactivado correctamente./success")
            return redirect('usuario_list')
    else:
        resp = delete_usuario(rut_usr)
        messages.success(request, "Usuario desactivado correctamente./success")
        return redirect('usuario_list')
        

def delete_usuario(rut_usr):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor.callproc('SP_USUARIO_DELETE',[rut_usr])

# Inicio de sesión
def iniciar_sesion(request):
    if request.method == 'POST':
        formulario = formLogin(request.POST)
        if formulario.is_valid:
            rut_usr = request.POST.get('rut_usr')
            if not validarRut(rut_usr):
                messages.error(request, 'El RUT ingresado no es válido./error')
                return render(request, 'session/login.html')
            password = request.POST.get('password')
            password_cifrada = cifrarPassword(password)
            verificacion = Usuario.objects.filter(rut_usr = rut_usr, password = password_cifrada).exists()
            
            
        if verificacion == True:
            usuario = usuario_filtrado(rut_usr)
            estado = usuario[0]['data'][14]
            correo = usuario[0]['data'][6]
            nombre = usuario[0]['data'][1]
            if estado == 0:
                messages.error(request, "Su cuenta está desactivada, por favor acérquese a un administrativo de biblioteca para activarla./warning")
                return render(request, 'session/login.html')
            if usuario[0]['data'][11] == 0: 
                messages.warning(request, "Debe activar su cuenta para iniciar sesión en BiblioBEC, se enviará un correo para habilitarla./warning")
                resp = enviar_email_habilitar(correo, rut_usr, nombre)
                resp.send()
                return render(request, 'session/login.html')
            request.session['user_login'] = {'user': {'foto':usuario[0]['foto'],'rut_usr':usuario[0]['data'][0], 
            'nombre':usuario[0]['data'][1], 'apellido':usuario[0]['data'][2], 'tipo':usuario[0]['data'][9], 'tipo_desc':usuario[0]['data'][15].title()}}
            if usuario[0]['data'][13] == 1:
                return redirect('cambiar_contrasena')
            return redirect('index')
        else:
            messages.success(request, "Usuario o contraseña incorrecta, por favor intente nuevamente./error")
            return render(request, 'session/login.html')
    else:
        formulario = formLogin()
    return render(request, 'session/login.html', {'formulario': formulario})

def habilitar_cuenta(request):
    rut_usr = request.GET.get('rut_usr')
    usuario = usuario_filtrado(rut_usr)
    if usuario[0]['data'][11] == 0:
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        cursor.callproc('SP_USUARIO_UPDATE_ACTIVO',[rut_usr])
        messages.success(request, "Su cuenta ha sido habilitada./success")
        return redirect('login')
    else:
        messages.info(request, "Su cuenta ya está habilitada, inicie sesión en BiblioBEC./info")
        return redirect('login')

def actualizar_contrasena(rut_usr, password):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_USUARIO_UPDATE_PASSWORD',[rut_usr, password, salida])

    return salida.getvalue()

def cambiar_contrasena(request):
    if not request.session._session:
        rut_usr = request.GET.get('rut_usr')
    else:
        rut_usr = request.session['user_login']['user']['rut_usr']
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password_cifrada = cifrarPassword(password1)
        resp = actualizar_contrasena(rut_usr, password_cifrada)
        if resp == 1:
            messages.success(request, 'Contraseña actualizada con éxito./success')
            return redirect('index')
        else:
            messages.error(request, 'No fue posible actualizar su contraseña, inténtelo nuevamente./error')
    else:
        return render(request, 'session/cambiar_contrasena.html')

def logout(request):
    try:
        del request.session['user_login']
    except KeyError:
        pass
    return redirect('index')

    #vista para reserva 
def vista_reserva(request,isbn):
    now = datetime.now().strftime('%Y-%m-%d')
    data = { 
        'form': ReservaForm(), 
        'ejem': id_ejem(isbn,1),
        'doc': filtro_doc(isbn),
        "fecha": fecha_proxima(isbn),
        "disp": num_ejem_dis(isbn),
        "fecha_2" :now
    }
    return render(
    request,
    'reserva/reserva.html',
    data
    )

def reserva_creada(isbn,id_ejem,fecha_d,fecha_h,rut):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("reserva_creada", [isbn,id_ejem,fecha_d,fecha_h,rut])

def accionar_res_cre(request):
    isbn = request.POST.get('isbn','')
    id_ejem = request.POST.get('id_ejem','')
    fecha_d = request.POST.get('fecha_desde','')
    fecha_h = request.POST.get('fecha_hasta','')
    rut = request.POST.get('rut','')

    reserva_creada(isbn,id_ejem, fecha_d, fecha_h, rut)
    messages.success(request, "Reserva correctamente creada./success")
    return redirect("catalogo")

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

def fecha_proxima(isbn):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("fecha_reserva_valida", [isbn,out_cur])

    lista = []

    for i in out_cur:
        lista.append({
            'data':i
        })
    
    return lista

def lista_reserva():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("sp_lista_reserva", [out_cur])

    lista = []

    for i in out_cur:
        lista.append({
            'data':i
        })
    
    return lista
def  sr(rut, id_ejem, isbn,fecha,pro,res,fecha_desde,fecha_hasta) :
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("p_solicitud_reserva", [rut,id_ejem,isbn,fecha,pro,res,fecha_desde,fecha_hasta])

def proceso_solicitud_reserva(request):
    rut = request.POST.get('rut','')
    id_ejem = request.POST.get('id_ejem','')
    isbn = request.POST.get('isbn','')
    pro = request.POST.get('pro','')
    fecha = datetime.now()
    res = request.POST.get('res','')
    fecha_desde = request.POST.get('fecha_desde','')
    fecha_hasta = request.POST.get('fecha_hasta','')
    print (fecha_desde)
    print (fecha_hasta)
    sr(rut, id_ejem, isbn,fecha,pro,res,fecha_desde,fecha_hasta)
    messages.success(request, "Solicitud procesada correctamente. Diríjase al mesón para retirar el documento./success")
    return redirect('catalogo')

def pro_cancelar_res(request):
    num= request.POST.get('num','')
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("sp_cancelar_res", [num])
    return redirect('solicitudes')
    
    

# VISTAS DE SOLICITUD DOCUMENTO

def enviar_email_recordatorio(numero_pres, correo, rut_usr, nombre, titulo, autor,fecha_prestamo, tipo, vencimiento):
    context = {'mail': correo, 'rut_usr': rut_usr, 'nombre': nombre, 'titulo': titulo, 'autor': autor, 'fecha_prestamo': fecha_prestamo, 
    'tipo': tipo, 'vencimiento': vencimiento}
    template = get_template('correo_recordatorio.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Recordatorio de devolución',
        'BiblioBEC',
        settings.EMAIL_HOST_USER,
        to=[correo]
    )
    
    email.attach_alternative(content, 'text/html')
    return email

def enviar_email_comprobante(numero_pres,correo,nombre, rut_usr, id_ejem ,documento, fecha_prestamo, fecha_devolucion,tipo, autor):
    context = {'mail': correo, 'rut_usr': rut_usr, 'nombre': nombre, 'documento': documento,'id_ejem':id_ejem,'fecha_prestamo': fecha_prestamo, 
    'tipo': tipo, 'numero_pres': numero_pres ,'fecha_devolucion': fecha_devolucion, 'autor': autor}
    template = get_template('correo_comprobante.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Comprobante de préstamo',
        'BiblioBEC',
        settings.EMAIL_HOST_USER,
        to=[correo]
    )
    
    email.attach_alternative(content, 'text/html')
    return email

def solicitud_prestamo(request):
    rut = request.POST.get('rut','')
    isbn = request.POST.get('isbn','')
    
    data={
        'num' : num_ejem_dis(isbn),
        'ejem': id_ejem(isbn,1),
        'doc': filtro_doc(isbn),
        'rut': rut,
    }
    return render(request,'prestamo.html',data)

def proceso_solicitud(request):
    rut = request.POST.get('rut','')
    id_ejem = request.POST.get('id_ejem','')
    isbn = request.POST.get('isbn','')
    tipo = request.POST.get('tipo','')
    pro = request.POST.get('pro','')
    fecha = datetime.now()
    sp(rut, id_ejem, isbn, tipo,fecha,pro)
    messages.success(request, "Solicitud procesada correctamente. Diríjase al mesón para retirar el documento./success")
    return redirect('catalogo')

def proceso_aprobacion(request,pres,rut,fecha):
    sp(pres, 0, '', '','','p')  
    cp = lista_com_pre(rut,fecha)
    correo = enviar_email_comprobante(cp[0]["data"][0],cp[0]["data"][1],cp[0]["data"][2],cp[0]["data"][3],cp[0]["data"][4],
    cp[0]["data"][5],cp[0]["data"][6],cp[0]["data"][7],cp[0]["data"][8], cp[0]["data"][9])
    correo.send()
    return redirect('solicitudes')

def proceso_cancelar(request,pres,id_ejem):
    sp(pres, id_ejem, '', '','','c')  
    return redirect('solicitudes')


def sp(rut,id_ejem,isbn,tipo,fecha,pro):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("p_solicitud_prestamo", [rut,id_ejem,isbn,tipo,fecha,pro])

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

def id_ejem(isbn,opcion):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("sp_ejemplar", [isbn,opcion,out_cur])

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

def lista_com_pre(rut, fecha):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("sp_comprobante_pres", [rut,fecha,out_cur])

    lista = []

    for i in out_cur:
        lista.append({
            'data':i
        })
    
    return lista

def pres_filtrado(numero_pres):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("SP_PRESTAMO_FILTRADO", [numero_pres, out_cur])

    lista = []

    for i in out_cur:
        lista.append({
            'data':i
        })
    
    return lista

def pres_filtrado_rut_usr(rut_usr):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("SP_PRESTAMO_FILTRADO_RUT_USR", [rut_usr, out_cur])

    lista = []

    for i in out_cur:
        lista.append({
            'data':i
        })
    
    return lista


def enviar_correo_dev(request): 
    numero_pres = request.GET.get('numero_pres')
    data = {
        'pres_filtrado':pres_filtrado(numero_pres) #Todos
    }
    resp = enviar_email_recordatorio(numero_pres, data['pres_filtrado'][0]['data'][3],data['pres_filtrado'][0]['data'][1], data['pres_filtrado'][0]['data'][2], 
    data['pres_filtrado'][0]['data'][5], data['pres_filtrado'][0]['data'][6], data['pres_filtrado'][0]['data'][7], 
    data['pres_filtrado'][0]['data'][4], data['pres_filtrado'][0]['data'][9])
    resp.send()
    return redirect('solicitudes')

def devolucion(request,id_ejem, num):
    sp_devolucion(id_ejem,num)
    return redirect('solicitudes')

def sp_devolucion(id_ejem,num):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor.callproc("SP_DEVOLUCION_DOC", [id_ejem,num])

def calcular_sansion(request):
    morosos = request.POST.getlist('moroso[]')
    cont = request.POST.get('cont')

    if int(cont) > 0:
        lista_cod = []
        l = []
        ejem = 0
        rut = ""
        isbn = ""
        pres = 0
        for mo in morosos:
            codigos2 = mo
            for cod in range(0,len(mo)):
                pos_fin = codigos2.find(",")
                if pos_fin != -1:
                    codi = codigos2[0:pos_fin]
                    codigos2 = codigos2[(pos_fin+1):(pos_fin+len(codigos2))]
                    ejem = codi
                    pos_fin = codigos2.find(",")
                    if pos_fin != -1:
                        codi = codigos2[0:pos_fin]
                        codigos2 = codigos2[(pos_fin+1):(pos_fin+len(codigos2))]
                        rut = codi
                        pos_fin = codigos2.find(",")
                        if pos_fin != -1:
                            codi = codigos2[0:pos_fin]
                            codigos2 = codigos2[(pos_fin+1):(pos_fin+len(codigos2))]
                            isbn= codi
                            pos_fin = codigos2.find("}")
                            if pos_fin != -1:
                                codi = codigos2[0:pos_fin]
                                codigos2 = codigos2[(pos_fin+1):(pos_fin+len(codigos2))]
                                pres =codi
        
            l = [ejem,rut,isbn,pres]
            lista_cod.append(l)  
        for mo in lista_cod:
            print(mo)
            
            cont2 = cont_sansion(int(mo[0]),mo[1])
            if(cont2[0]['data'][0] > 0):
                x = 2
            else:
                sp_sansion(mo[1],int(mo[0]),mo[2],mo[3])
                x = 3
            
    cosa = 1
    return HttpResponse(x)

def cont_sansion(ejem,rut):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("sp_cont_sansion", [rut, ejem,out_cur]) 
    lista = []

    for i in out_cur:
        lista.append({
            'data':i
        })
    
    return lista

def sp_sansion(rut,id_ejem,isbn,pres):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor.callproc("sp_calcular_sansion", [rut,id_ejem,isbn,pres])

def catalogo_sansion(rut):
    cursor_dj = connection.cursor()
    cursor_ex = cursor_dj.connection.cursor() 
    cursor_out= cursor_dj.connection.cursor() 
    cursor_ex.callproc('sp_cont_sansionRut',[rut,cursor_out])

    lista = []
    for i in cursor_out:
        lista.append({
            'data':i,
        })

    return lista

def fin_sancion(request):
    rut = request.POST.get('rut')
    cursor_dj = connection.cursor()
    cursor_ex = cursor_dj.connection.cursor() 
    cursor_ex.callproc('sp_fin_sancion',[rut])
    return 1

