# Generated by Django 3.2.25 on 2024-06-26 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diccionario', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='termino',
            old_name='definition',
            new_name='definicion',
        ),
        migrations.RenameField(
            model_name='termino',
            old_name='term',
            new_name='termino',
        ),
    ]
