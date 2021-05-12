from django import forms
from . models import Libro, Categoria, TipoMedio, TipoDocumento , Ejemplar, Reserva , SolicitudPrestamo 
from . models import TipoPrestamo, TipoUsuario, DetalleSolicitudPrestamo, Prestamo, Usuario

# formulario documento

class DocumentoForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = '__all__'

class EjemplarForm(forms.ModelForm):

    class Meta:
        model = Ejemplar
        fields = '__all__'

#Formulario Usuario
class UsuarioForm(forms.ModelForm):
    tipo_usuario_id_tipo = forms.ModelChoiceField(queryset=TipoUsuario.objects.all(),label='Tipo usuario', required=True, widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))

    rut_usr = forms.CharField(label='RUT Usuario', required=True, max_length=9, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    nombre = forms.CharField(label='Nombre', required=True, max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    apellido_p = forms.CharField(label='Apellido paterno', max_length=30, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    apellido_m = forms.CharField(label='Apellido materno', max_length=30, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    direccion = forms.CharField(label='Dirección', required=True, max_length=100, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    telefono = forms.IntegerField(label='Teléfono', required=True, widget=forms.NumberInput(
        attrs={
            'class': 'form-control'
        }
    ))

    correo = forms.EmailField(label='Correo electrónico', max_length=150, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    password = forms.CharField(label='Password', max_length=20, required=True, widget=forms.PasswordInput(
    attrs={
            'class': 'form-control'
        }
    ))

    foto = forms.ImageField(label='Foto', required=False, widget=forms.FileInput(
        attrs={
            'class': 'form-control'
        }
    ))

    huella = forms.ImageField(label='Huella', required=False, widget=forms.FileInput(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Usuario
        fields = ('rut_usr' , 'nombre', 'apellido_p', 'apellido_m', 'direccion', 'telefono', 'correo', 'foto',
                'huella', 'tipo_usuario_id_tipo', 'password')

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = '__all__'

class formLogin(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut_usr','password']