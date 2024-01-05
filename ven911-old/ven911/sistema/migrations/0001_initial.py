# Generated by Django 4.1.8 on 2023-11-28 02:33

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entradap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=64, verbose_name='Nombre:')),
                ('apellido', models.CharField(default='', max_length=64, verbose_name='Apellido:')),
                ('cedula', models.CharField(default='', max_length=64, verbose_name='Cédula:')),
                ('telefono', models.CharField(default='', max_length=64, verbose_name='Teléfono:')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('direccion', models.CharField(default='', max_length=64, verbose_name='Dirección:')),
                ('cargo', models.CharField(default='', max_length=64, verbose_name='Cargo:')),
                ('hora', models.CharField(default='', max_length=64, verbose_name='Hora de Entrada:')),
            ],
        ),
        migrations.CreateModel(
            name='Gestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=64, verbose_name='Nombre:')),
                ('apellido', models.CharField(default='', max_length=64, verbose_name='Apellido:')),
                ('cedula', models.CharField(default='', max_length=64, verbose_name='Cédula:')),
                ('tipo', models.CharField(default='', max_length=64, verbose_name='Tipo de Incidente:')),
                ('descripcion', models.CharField(default='', max_length=64, verbose_name='Descripción:')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('direccion', models.CharField(default='', max_length=64, verbose_name='Dirección:')),
                ('cargo', models.CharField(default='', max_length=64, verbose_name='Cargo:')),
                ('hora', models.CharField(default='', max_length=64, verbose_name='Hora de Entrada:')),
            ],
        ),
        migrations.CreateModel(
            name='Normativas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=64, verbose_name='Nombre de Normativa:')),
                ('file', models.FileField(default='', upload_to='normativas/', verbose_name='Archivo')),
                ('user', models.CharField(default='', max_length=64, verbose_name='Usuario')),
                ('date', models.DateField(blank=True, verbose_name='Fecha')),
            ],
        ),
        migrations.CreateModel(
            name='Reglamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=64, verbose_name='Nombre de Reglamento:')),
                ('file', models.FileField(default='', upload_to='reglamentos/', verbose_name='Archivo')),
                ('user', models.CharField(default='', max_length=64, verbose_name='Usuario')),
                ('date', models.DateField(blank=True, verbose_name='Fecha')),
            ],
        ),
        migrations.CreateModel(
            name='Salidap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=64, verbose_name='Nombre:')),
                ('apellido', models.CharField(default='', max_length=64, verbose_name='Apellido:')),
                ('cedula', models.CharField(default='', max_length=64, verbose_name='Cédula:')),
                ('telefono', models.CharField(default='', max_length=64, verbose_name='Teléfono:')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('direccion', models.CharField(default='', max_length=64, verbose_name='Dirección:')),
                ('cargo', models.CharField(default='', max_length=64, verbose_name='Cargo:')),
                ('hora', models.CharField(default='', max_length=64, verbose_name='Hora de Entrada:')),
            ],
        ),
        migrations.CreateModel(
            name='UserC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('ci', models.CharField(default='', max_length=64, unique=True, verbose_name='Cédula:')),
                ('nombre', models.CharField(default='', max_length=64, verbose_name='Nombre:')),
                ('apellido', models.CharField(default='', max_length=64, verbose_name='Apellido:')),
                ('password', models.CharField(default='', max_length=64, verbose_name='Contraseña:')),
                ('tipo', models.CharField(choices=[('estandar', 'estandar'), ('admin', 'admin'), ('superu', 'superu')], default='', max_length=64, verbose_name='Tipo de Usuario:')),
                ('sede', models.CharField(default='', max_length=64, verbose_name='Sede:')),
                ('departamento', models.CharField(default='', max_length=64, verbose_name='Departamento:')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]