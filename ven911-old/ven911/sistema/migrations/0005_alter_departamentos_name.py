# Generated by Django 4.1.8 on 2023-11-28 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0004_departamentos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamentos',
            name='name',
            field=models.CharField(default='', max_length=64, unique=True, verbose_name='Nombre:'),
        ),
    ]
