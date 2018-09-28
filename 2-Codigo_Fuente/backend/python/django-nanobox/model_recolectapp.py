# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Localidad(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'localidad'


class Operacion(models.Model):
    url = models.CharField(max_length=255, blank=True, null=True)
    nombre_operacion = models.CharField(max_length=255, blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operacion'


class OperacionRol(models.Model):
    id_operacion = models.ForeignKey(Operacion, models.DO_NOTHING, db_column='id_operacion', primary_key=True)
    id_rol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='id_rol')

    class Meta:
        managed = False
        db_table = 'operacion_rol'


class OrdenServicio(models.Model):
    numero_orden = models.CharField(max_length=50, blank=True, null=True)
    fecha_creacion = models.DateField(blank=True, null=True)
    fecha_ejecucion = models.DateField(blank=True, null=True)
    param_codigo_estado = models.CharField(max_length=20, blank=True, null=True)
    id_solicitud = models.ForeignKey('SolicitudServicio', models.DO_NOTHING, db_column='id_solicitud')

    class Meta:
        managed = False
        db_table = 'orden_servicio'


class OrdenServicioHistorico(models.Model):
    id_orden = models.ForeignKey(OrdenServicio, models.DO_NOTHING, db_column='id_orden')
    param_codigo_estado = models.CharField(max_length=20, blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'orden_servicio_historico'


class Parametro(models.Model):
    dominio = models.CharField(max_length=100, blank=True, null=True)
    dominio_padre = models.CharField(max_length=100, blank=True, null=True)
    codigo = models.CharField(max_length=20, blank=True, null=True)
    codigo_padre = models.CharField(max_length=20, blank=True, null=True)
    valor = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametro'


class Rol(models.Model):
    param_codigo_tipo_rol = models.CharField(max_length=20, blank=True, null=True)
    estado = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol'


class SolicitudServicio(models.Model):
    numero_solicitud = models.CharField(max_length=50, blank=True, null=True)
    fecha_solicitud = models.DateField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    ubicacion = models.CharField(max_length=255, blank=True, null=True)
    fecha_recogida = models.DateField(blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_ubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, db_column='id_ubicacion')
    param_codigo_estado = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitud_servicio'


class SolicitudServicioHistorico(models.Model):
    id_solicitud = models.ForeignKey(SolicitudServicio, models.DO_NOTHING, db_column='id_solicitud')
    param_codigo_estado = models.CharField(max_length=20, blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'solicitud_servicio_historico'


class Ubicacion(models.Model):
    latitud = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ubicacion'


class Usuario(models.Model):
    primer_nombre = models.CharField(max_length=50, blank=True, null=True)
    segundo_nombre = models.CharField(max_length=50, blank=True, null=True)
    primer_apellido = models.CharField(max_length=50, blank=True, null=True)
    segundo_apellido = models.CharField(max_length=50, blank=True, null=True)
    param_codigo_tipo_documento = models.CharField(max_length=20, blank=True, null=True)
    numero_documento = models.CharField(max_length=20, blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)
    clave = models.CharField(max_length=255, blank=True, null=True)
    tel_fijo = models.CharField(max_length=15, blank=True, null=True)
    tel_celular = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    id_ubicacion = models.ForeignKey(Ubicacion, models.DO_NOTHING, db_column='id_ubicacion')
    id_localidad = models.ForeignKey(Localidad, models.DO_NOTHING, db_column='id_localidad')
    estado = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class UsuarioRol(models.Model):
    id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='id_rol', primary_key=True)
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'usuario_rol'
        unique_together = (('id_rol', 'id_usuario'),)
