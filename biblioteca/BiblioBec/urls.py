from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('solicitudes', views.solicitudes, name='solicitudes'),
    path('documento/create', views.create_doc, name='create_doc'),
]