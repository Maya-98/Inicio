from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

# Create your models here.
class UserC(AbstractUser, PermissionsMixin):

    STATUS = (
        ('estandar', 'estandar'),
        ('admin', 'admin'),
        ('superu', 'superu'),
    )

    username = models.CharField(max_length=200, verbose_name='Cédula:', default='', unique=True)
    nombre = models.CharField(max_length=200, verbose_name='Nombre:', default='')
    apellido = models.CharField(max_length=200, verbose_name='Apellido:', default='')
    password = models.CharField(max_length=200, verbose_name='Contraseña:', default='')
    tipo = models.CharField(max_length=200, verbose_name='Tipo de Usuario:', choices=STATUS, default='')
    sede = models.CharField(max_length=200, verbose_name='Sede:', default='')
    departamento = models.CharField(max_length=200, verbose_name='Departamento:', default='')

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
    
class Departamentos(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nombre:', default='', unique=True)

class Sedes(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nombre:', default='', unique=True)

class Reglamentos(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nombre de Reglamento:', default='')
    file = models.FileField(upload_to='reglamentos/', verbose_name='Archivo', default='')
    user = models.CharField(max_length=64, verbose_name='Usuario', default='')
    date = models.DateField(verbose_name='Fecha', blank=True)

class Normativas(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nombre de Normativa:', default='')
    file = models.FileField(upload_to='normativas/', verbose_name='Archivo', default='')
    user = models.CharField(max_length=64, verbose_name='Usuario', default='')
    date = models.DateField(verbose_name='Fecha', blank=True)

class Entradap(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nombre:', default='')
    apellido = models.CharField(max_length=64, verbose_name='Apellido:', default='')
    cedula = models.CharField(max_length=64, verbose_name='Cédula:', default='')
    telefono = models.CharField(max_length=64, verbose_name='Teléfono:', default='')
    fecha = models.DateField(verbose_name='Fecha')
    direccion = models.CharField(max_length=64, verbose_name='Dirección:', default='')
    cargo = models.CharField(max_length=64, verbose_name='Cargo:', default='')
    hora = models.CharField(max_length=64, verbose_name='Hora de Entrada:', default='')

class Salidap(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nombre:', default='')
    apellido = models.CharField(max_length=64, verbose_name='Apellido:', default='')
    cedula = models.CharField(max_length=64, verbose_name='Cédula:', default='')
    telefono = models.CharField(max_length=64, verbose_name='Teléfono:', default='')
    fecha = models.DateField(verbose_name='Fecha')
    direccion = models.CharField(max_length=64, verbose_name='Dirección:', default='')
    cargo = models.CharField(max_length=64, verbose_name='Cargo:', default='')
    hora = models.CharField(max_length=64, verbose_name='Hora de Entrada:', default='')

class Gestion(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nombre:', default='')
    apellido = models.CharField(max_length=64, verbose_name='Apellido:', default='')
    cedula = models.CharField(max_length=64, verbose_name='Cédula:', default='')
    tipo = models.CharField(max_length=64, verbose_name='Tipo de Incidente:', default='')
    descripcion = models.CharField(max_length=64, verbose_name='Descripción:', default='')
    fecha = models.DateField(verbose_name='Fecha')
    direccion = models.CharField(max_length=64, verbose_name='Dirección:', default='')
    cargo = models.CharField(max_length=64, verbose_name='Cargo:', default='')
    hora = models.CharField(max_length=64, verbose_name='Hora de Entrada:', default='')

class Vehiculos(models.Model):
    nombre = models.CharField(max_length=64, verbose_name='Nombre:', default='')
    apellido = models.CharField(max_length=64, verbose_name='Apellido:', default='')
    cedula = models.CharField(max_length=64, verbose_name='Cédula:', default='')
    tipo= models.CharField(max_length=64, verbose_name='Tipo:', default='')
    transporte = models.CharField(max_length=64, verbose_name='Transporte:', default='')
    modelo = models.CharField(max_length=64, verbose_name='Modelo:', default='')
    placa = models.CharField(max_length=64, verbose_name='Placa:', default='')
    fecha = models.DateField(verbose_name='Fecha')
    hora = models.CharField(max_length=64, verbose_name='Hora:', default='')

class Presupuesto(models.Model):
    nombrep = models.CharField(max_length=64, verbose_name='Nombre del Proyecto:', default='')
    fechai = models.DateField(verbose_name='Fecha de Inicio')
    fechac = models.DateField(verbose_name='Fecha de Culminación')
    situacionp = models.CharField(max_length=64, verbose_name='Situación Presupuestaria:', default='')
    pplurianual = models.CharField(max_length=64, verbose_name='Proyecto en Plurianual:', default='')
    montoaño = models.CharField(max_length=64, verbose_name='Monto Total del Proyecto para el año en curso:', default='')
    montoproyecto = models.CharField(max_length=64, verbose_name='Monto Total del Proyecto:', default='')
    responsableg = models.CharField(max_length=64, verbose_name='Responsable Gerente:', default='')
    responsablet = models.CharField(max_length=64, verbose_name='Responsable Técnico:', default='')
    responsabler = models.CharField(max_length=64, verbose_name='Responsable Registrador:', default='')
    responsablea = models.CharField(max_length=64, verbose_name='Responsable Administrativo:', default='')
    estatus = models.CharField(max_length=64, verbose_name='Estatus del Proyecto:', default='')

class Personal(models.Model):
    nombre = models.CharField(max_length=64, verbose_name='Nombre:', default='')
    apellido = models.CharField(max_length=64, verbose_name='Apellido:', default='')
    cedula = models.CharField(max_length=64, verbose_name='Cédula:', default='')
    nacionalidad = models.CharField(max_length=64, verbose_name='Transporte:', default='')
    sexo = models.CharField(max_length=64, verbose_name='Modelo:', default='')
    fecha_nac = models.CharField(max_length=64, verbose_name='Placa:', default='')
    edad = models.DateField(verbose_name='Fecha')
    telefono = models.CharField(max_length=64, verbose_name='Hora:', default='')
    estado_civil = models.CharField(max_length=64, verbose_name='Hora:', default='')
    conyugue = models.CharField(max_length=64, verbose_name='Hora:', default='')
    cedula_conyugue = models.CharField(max_length=64, verbose_name='Hora:', default='')
    tipo_sangre = models.CharField(max_length=64, verbose_name='Hora:', default='')
    discapacitado = models.CharField(max_length=64, verbose_name='Hora:', default='')
    talla_camisa = models.CharField(max_length=64, verbose_name='Hora:', default='')
    talla_pantalon = models.CharField(max_length=64, verbose_name='Hora:', default='')
    talla_zapato = models.CharField(max_length=64, verbose_name='Hora:', default='')
    fasmij = models.CharField(max_length=64, verbose_name='Hora:', default='')
    direccion = models.CharField(max_length=64, verbose_name='Hora:', default='')
    nro_cuenta = models.CharField(max_length=64, verbose_name='Hora:', default='')
    email = models.CharField(max_length=64, verbose_name='Hora:', default='')
    grado_instruccion = models.CharField(max_length=64, verbose_name='Hora:', default='')
    estudias = models.CharField(max_length=64, verbose_name='Hora:', default='')
    comision_servicio = models.CharField(max_length=64, verbose_name='Hora:', default='')
    pnb = models.CharField(max_length=64, verbose_name='Hora:', default='')
    tipo_personal = models.CharField(max_length=64, verbose_name='Hora:', default='')
    cargo = models.CharField(max_length=64, verbose_name='Hora:', default='')
    fecha_ingreso_911 = models.CharField(max_length=64, verbose_name='Hora:', default='')
    fecha_ingreso_apn = models.CharField(max_length=64, verbose_name='Hora:', default='')
    contratos = models.CharField(max_length=64, verbose_name='Hora:', default='')
    departamento = models.CharField(max_length=64, verbose_name='Hora:', default='')
    hijos_13_18 = models.CharField(max_length=64, verbose_name='Hora:', default='')
    edades1 = models.CharField(max_length=64, verbose_name='Hora:', default='')
    niño_menor_12 = models.CharField(max_length=64, verbose_name='Hora:', default='')
    edades2 = models.CharField(max_length=64, verbose_name='Hora:', default='')
    niña_menor_12 = models.CharField(max_length=64, verbose_name='Hora:', default='')
    edades3 = models.CharField(max_length=64, verbose_name='Hora:', default='')
    hijos_discapacidad = models.CharField(max_length=64, verbose_name='Hora:', default='')
    edades4 = models.CharField(max_length=64, verbose_name='Hora:', default='')
    sede = models.CharField(max_length=64, verbose_name='Hora:', default='')

class Incidencias(models.Model):
    estado=models.CharField(max_length=300)
    sede=models.CharField(max_length=300)
    departamento=models.CharField(max_length=300)
    tipoincidencia=models.CharField(max_length=300)
    usuario=models.CharField(max_length=300)
    observaciones=models.CharField(max_length=300)

    class Meta:
        verbose_name='incidencia'
        verbose_name_plural='incidencias'

    def __str__(self):
        return self.estado