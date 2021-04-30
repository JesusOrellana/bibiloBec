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
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = '__all__'

>>>>>>> 88abea396e483ce119f38cca9e0b615a07fbfc9e
