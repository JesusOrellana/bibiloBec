# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categoria(models.Model):
    id_cate = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'categoria'


class DetalleSolicitudPrestamo(models.Model):
    fecha_devolucion = models.DateField()
    hora_devolucion = models.DateField()
    fecha_devolucion_real = models.DateField()
    hora_devolucion_real = models.DateField()
    id_ejemplar = models.OneToOneField('Ejemplar', models.DO_NOTHING, db_column='id_ejemplar', primary_key=True)
    numero_solicitud = models.ForeignKey('SolicitudPrestamo', models.DO_NOTHING, db_column='numero_solicitud')

    class Meta:
        managed = False
        db_table = 'detalle_solicitud_prestamo'
        unique_together = (('id_ejemplar', 'numero_solicitud'),)


class Ejemplar(models.Model):
    id_ejem = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    stock = models.IntegerField()
    stock_disponible = models.IntegerField()
    stock_ocupado = models.IntegerField(blank=True, null=True)
    libro_isbn = models.ForeignKey('Libro', models.DO_NOTHING, db_column='libro_isbn')

    class Meta:
        managed = False
        db_table = 'ejemplar'


class Libro(models.Model):
    isbn = models.CharField(primary_key=True, max_length=200)
    titulo = models.CharField(max_length=250)
    autor = models.CharField(max_length=250)
    editorial = models.CharField(max_length=250)
    fecha_publicacion = models.DateField()
    edicion = models.CharField(max_length=250)
    categoria_id_cate = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='categoria_id_cate')
    tipo_documento_id_tipo_doc = models.ForeignKey('TipoDocumento', models.DO_NOTHING, db_column='tipo_documento_id_tipo_doc')

    class Meta:
        managed = False
        db_table = 'libro'


class Prestamo(models.Model):
    numero_pres = models.IntegerField(primary_key=True)
    fecha_prestamo = models.DateField()
    rut_usr = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='rut_usr')
    tipo_prestamo = models.ForeignKey('TipoPrestamo', models.DO_NOTHING, db_column='tipo_prestamo')
    numero_solicitud = models.ForeignKey('SolicitudPrestamo', models.DO_NOTHING, db_column='numero_solicitud')

    class Meta:
        managed = False
        db_table = 'prestamo'


class Reserva(models.Model):
    numero_res = models.IntegerField(primary_key=True)
    fecha_reserva = models.DateField()
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField()
    ejemplar_id_ejem = models.ForeignKey(Ejemplar, models.DO_NOTHING, db_column='ejemplar_id_ejem')
    usuario_rut_usr = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_rut_usr')

    class Meta:
        managed = False
        db_table = 'reserva'


class SolicitudPrestamo(models.Model):
    numero_solicitud = models.IntegerField(primary_key=True)
    fecha_solicitud = models.DateField()
    hora_solicitud = models.DateField()
    usuario_rut_usr = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_rut_usr')

    class Meta:
        managed = False
        db_table = 'solicitud_prestamo'


class TipoDocumento(models.Model):
    id_tipo_doc = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'tipo_documento'


class TipoPrestamo(models.Model):
    id_tipo = models.BooleanField()
    tipo = models.CharField(max_length=35)
    tipo_prestamo_id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tipo_prestamo'


class TipoUsuario(models.Model):
    id_tipo = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Usuario(models.Model):
    rut_usr = models.CharField(primary_key=True, max_length=9)
    nombre = models.CharField(max_length=30)
    apellido_p = models.CharField(max_length=30)
    apellido_m = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=150)
    foto = models.CharField(max_length=1, blank=True, null=True)
    huella = models.CharField(max_length=1, blank=True, null=True)
    tipo_usuario_id_tipo = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='tipo_usuario_id_tipo')
    password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'usuario'
