# Generated by Django 4.1.8 on 2023-11-28 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userc',
            name='ci',
        ),
        migrations.AlterField(
            model_name='userc',
            name='username',
            field=models.CharField(default='', max_length=64, unique=True, verbose_name='Cédula:'),
        ),
    ]
