from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='index'),
    path('login', views.iniciar_sesion, name='login'),
    path('cambiar_contrasena', views.cambiar_contrasena, name='cambiar_contrasena'),
    path('logout', views.logout, name='logout'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('catalogo/audios/', views.catalogo_audio, name='catalogo_audio'),
    path('catalogo/libros/', views.catalogo_libro, name='catalogo_libros'),
    path('catalogo/videos/', views.catalogo_video, name='catalogo_videos'),
    path('solicitudes', views.solicitudes, name='solicitudes'),
    path('documento', views.form_cr_doc, name='form_doc'),
    path('documento/create', views.create_doc, name='create_doc'),
    path('documento-update/<str:isbn>', views.form_up_doc, name='form_update_doc'),
    path('documento/update', views.update_doc, name='update_doc'),
    path('documento-delete/<str:isbn>', views.delete_doc, name='eliminar_documento'),
    path('usuario/create', views.form_usuario, name='usuario_create'),
    path('usuarios', views.usuarios, name='usuario_list'),
    path('usuario/create', views.form_usuario, name='usuario_create'),
    path('usuario/update', views.editar_usuario, name='usuario_update'),
    path('usuario/delete', views.eliminar_usuario, name='usuario_delete'),
    path('usuario/habilitar', views.habilitar_cuenta, name='habilitar'),
    path('restablecer_contrasena', views.enviar_correo_restablecer_contrasena, name='u_restablecer_contrasena'),
    path('cambiar_contrasena', views.cambiar_contrasena, name='cambiar_contrasena'),
    path('reserva/<str:isbn>', views.vista_reserva, name='reserva'),
    path('solicitud-prestamo', views.solicitud_prestamo, name='solicitud_pres'),
    path('proceso-solicitud', views.proceso_solicitud, name='proceso_solicitud'),
    path('proceso-aprobacion/<str:pres>/<str:rut>/<str:fecha>', views.proceso_aprobacion, name='proceso_aprobacion'),
    path('proceso-cancelar/<str:pres>/<str:id_ejem>', views.proceso_cancelar, name='proceso_cancelar'),
    path('recordatorio', views.enviar_correo_dev, name='correo_recordatorio'),
    path('devolucion/<str:id_ejem>/<str:num>', views.devolucion, name='devolucion'),
    path('ayuda', views.ayuda, name="ayuda"),
    path('reserva_creada', views.accionar_res_cre, name="reserva_creada"),
    path('calcular-sansion/', views.calcular_sansion, name="calcular_sansion")
]