# Generated by Django 4.0.5 on 2022-09-06 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inmobiliaria', '0002_remove_cliente_fecha_alta_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propiedad',
            name='disponibilidad',
        ),
    ]
