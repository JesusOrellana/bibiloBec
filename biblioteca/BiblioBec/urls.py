from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('catalogo/audios/', views.catalogo_audio, name='catalogo_audio'),
    path('catalogo/libros/', views.catalogo_libro, name='catalogo_libros'),
    path('catalogo/videos/', views.catalogo_video, name='catalogo_videos'),
    path('solicitudes', views.solicitudes, name='solicitudes'),
    path('documento', views.form_doc, name='form_doc'),
    path('documento/create', views.create_doc, name='create_doc'),
    path('documento-update/<str:isbn>', views.form_up_doc, name='update_doc'),
    path('reserva/<str:isbn>', views.vista_reserva, name='reserva'),
]