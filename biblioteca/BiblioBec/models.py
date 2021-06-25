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
        
    def __str__(self):
        return self.descripcion

class DetalleSolicitudPrestamo(models.Model):
    id_solicitud = models.IntegerField(primary_key=True)
    fecha_devolucion = models.DateField()
    hora_devolucion = models.DateField()
    fecha_devolucion_real = models.DateField()
    hora_devolucion_real = models.DateField()
    numero_solicitud = models.ForeignKey('SolicitudPrestamo', models.DO_NOTHING, db_column='numero_solicitud')

    class Meta:
        managed = False
        db_table = 'detalle_solicitud_prestamo'
        
    def __str__(self):
        return str(self.numero_solicitud) 

class Ejemplar(models.Model):
    id_ejem = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    isbn = models.ForeignKey('Libro', models.DO_NOTHING, db_column='isbn')
    class Meta:
        managed = False
        db_table = 'ejemplar'
        
    def __str__(self):
        return str(self.id_ejem)

class Libro(models.Model):
    isbn = models.CharField(primary_key=True, max_length=200)
    titulo = models.CharField(max_length=250)
    autor = models.CharField(max_length=250)
    editorial = models.ForeignKey('Editorial', models.DO_NOTHING, db_column='id_editorial')
    fecha_publicacion = models.DateField()
    edicion = models.IntegerField()
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True)
    categoria_id_cate = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='categoria_id_cate')
    tipo_documento_id_tipo_doc = models.ForeignKey('TipoDocumento', models.DO_NOTHING, db_column='tipo_documento_id_tipo_doc')
    tipo_medio = models.ForeignKey('TipoMedio', models.DO_NOTHING, db_column='id_medio')
    
    class Meta:
        managed = False
        db_table = 'libro'
        
    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    numero_pres = models.IntegerField(primary_key=True)
    fecha_prestamo = models.DateField()
    rut_usr = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='rut_usr')
    tipo_prestamo = models.ForeignKey('TipoPrestamo', models.DO_NOTHING, db_column='tipo_prestamo')
    numero_solicitud = models.ForeignKey('SolicitudPrestamo', models.DO_NOTHING, db_column='numero_solicitud')

    class Meta:
        managed = False
        db_table = 'prestamo'
        
    def __str__(self):
        return str(self.numero_pres)

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
        
    def __str__(self):
        return str(self.numero_res)

class SolicitudPrestamo(models.Model):
    numero_solicitud = models.IntegerField(primary_key=True)
    fecha_solicitud = models.DateField()
    hora_solicitud = models.DateField()
    usuario_rut_usr = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_rut_usr')

    class Meta:
        managed = False
        db_table = 'solicitud_prestamo'
        
    def __str__(self):
        return str(self.numero_solicitud)

class TipoDocumento(models.Model):
    id_tipo_doc = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'tipo_documento'
        
    def __str__(self):
        return self.descripcion

class TipoMedio(models.Model):
    id_medio = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'tipo_medio'

    def __str__(self):
        return self.descripcion

class TipoPrestamo(models.Model):
    tipo_prestamo_id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=35)


    class Meta:
        managed = False
        db_table = 'tipo_prestamo'

    def __str__(self):
        return self.tipo

class TipoUsuario(models.Model):
    id_tipo = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'
        
    def __str__(self):
        return self.tipo

class Usuario(models.Model):
    rut_usr = models.CharField(primary_key=True, max_length=9)
    nombre = models.CharField(max_length=30)
    apellido_p = models.CharField(max_length=30)
    apellido_m = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    correo = models.EmailField(max_length=150)
    foto = models.ImageField(upload_to="imagenes")
    huella = models.ImageField(upload_to="imagenes")
    tipo_usuario_id_tipo = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='tipo_usuario_id_tipo')
    password = models.CharField(max_length=20)
    activo = models.IntegerField()
    fecha_activacion = models.DateField()
    cambio_contrasena = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario'
        
    def __str__(self):
        return self.rut_usr
        

class Sancion(models.Model):
    id_sansion = models.IntegerField(primary_key=True)
    rut_usr = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='rut_usr')
    estado = models.CharField(max_length=30)
    fecha_devolucion = models.DateField() 

    class Meta:
        managed = False
        db_table = 'sancion'
        
    def __str__(self):
        return str(self.id_sansion) 

class Editorial(models.Model):
    id_editorial = models.IntegerField(primary_key=True)
    editorial = models.CharField(max_length=250)


    class Meta:
        managed = False
        db_table = 'editorial'

    def __str__(self):
        return self.editorial

class Estado_res(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=30)


    class Meta:
        managed = False
        db_table = 'estado_res'

    def __str__(self):
        return self.estado

class Estado_pres(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=30)


    class Meta:
        managed = False
        db_table = 'estado_pres'

    def __str__(self):
        return self.estado

class Estado_ejem(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=30)


    class Meta:
        managed = False
        db_table = 'estado_ejem'

    def __str__(self):
        return self.estado

class Estado_san(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=30)


    class Meta:
        managed = False
        db_table = 'estado_san'

    def __str__(self):
        return self.estado