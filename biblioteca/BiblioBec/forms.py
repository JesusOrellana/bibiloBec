from django import forms
from . models import Libro, Categoria, TipoMedio, TipoDocumento , Ejemplar, Reserva , SolicitudPrestamo 
from . models import TipoPrestamo, TipoUsuario, DetalleSolicitudPrestamo, Prestamo , Usuario

# formulario documento

class DocumentoForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = '__all__'

class EjemplarForm(forms.ModelForm):

    class Meta:
        model = Ejemplar
        fields = '__all__'

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'