# Generated by Django 4.2.7 on 2023-12-06 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0007_vehiculos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=64, verbose_name='Nombre:')),
                ('apellido', models.CharField(default='', max_length=64, verbose_name='Apellido:')),
                ('cedula', models.CharField(default='', max_length=64, verbose_name='Cédula:')),
                ('nacionalidad', models.CharField(default='', max_length=64, verbose_name='Transporte:')),
                ('sexo', models.CharField(default='', max_length=64, verbose_name='Modelo:')),
                ('fecha_nac', models.CharField(default='', max_length=64, verbose_name='Placa:')),
                ('edad', models.DateField(verbose_name='Fecha')),
                ('telefono', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('estado_civil', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('conyugue', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('cedula_conyugue', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('tipo_sangre', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('discapacitado', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('talla_camisa', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('talla_pantalon', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('talla_zapato', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('fasmij', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('direccion', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('nro_cuenta', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('email', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('grado_instruccion', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('estudias', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('comision_servicio', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('pnb', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('tipo_personal', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('cargo', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('fecha_ingreso_911', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('fecha_ingreso_apn', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('contratos', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('departamento', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('hijos_13_18', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('edades1', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('niño_menor_12', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('edades2', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('niña_menor_12', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('edades3', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('hijos_discapacidad', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('edades4', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('sede', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('creador', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('created', models.CharField(default='', max_length=64, verbose_name='Hora:')),
                ('updated', models.CharField(default='', max_length=64, verbose_name='Hora:')),
            ],
        ),
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrep', models.CharField(default='', max_length=64, verbose_name='Nombre del Proyecto:')),
                ('fechai', models.DateField(verbose_name='Fecha de Inicio')),
                ('fechac', models.DateField(verbose_name='Fecha de Culminación')),
                ('situacionp', models.CharField(default='', max_length=64, verbose_name='Situación Presupuestaria:')),
                ('pplurianual', models.CharField(default='', max_length=64, verbose_name='Proyecto en Plurianual:')),
                ('montoaño', models.CharField(default='', max_length=64, verbose_name='Monto Total del Proyecto para el año en curso:')),
                ('montoproyecto', models.CharField(default='', max_length=64, verbose_name='Monto Total del Proyecto:')),
                ('responsableg', models.CharField(default='', max_length=64, verbose_name='Responsable Gerente:')),
                ('responsablet', models.CharField(default='', max_length=64, verbose_name='Responsable Técnico:')),
                ('responsabler', models.CharField(default='', max_length=64, verbose_name='Responsable Registrador:')),
                ('responsablea', models.CharField(default='', max_length=64, verbose_name='Responsable Administrativo:')),
                ('estatus', models.CharField(default='', max_length=64, verbose_name='Estatus del Proyecto:')),
            ],
        ),
    ]