from django.contrib import admin
from . models import Libro, Categoria, TipoMedio, TipoDocumento , Ejemplar, Reserva , SolicitudPrestamo 
from . models import TipoPrestamo, TipoUsuario, DetalleSolicitudPrestamo, Prestamo , Usuario


# Register your models here.
admin.site.register(Libro)
admin.site.register(Categoria)
admin.site.register(TipoMedio)
admin.site.register(TipoDocumento)
admin.site.register(TipoUsuario)
admin.site.register(DetalleSolicitudPrestamo)
admin.site.register(Ejemplar)
admin.site.register(Prestamo)
admin.site.register(Reserva)
admin.site.register(SolicitudPrestamo)
admin.site.register(Usuario)
admin.site.register(TipoPrestamo)


