# Generated by Django 5.0 on 2024-01-03 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0011_alter_incidencias_departamento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculos',
            name='tipo',
            field=models.CharField(default='', max_length=64, verbose_name='Tipo:'),
        ),
    ]