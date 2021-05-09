from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.iniciar_sesion, name='login'),
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
    path('reserva/<str:isbn>', views.vista_reserva, name='reserva'),
    path('solicitud-prestamo', views.solicitud_prestamo, name='solicitud_pres'),
    path('proceso-prestamo', views.proceso_prestamo, name='proceso_prestamo'),
]