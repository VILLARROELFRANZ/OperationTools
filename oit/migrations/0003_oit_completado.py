# Generated by Django 4.2.7 on 2023-12-03 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oit', '0002_remove_repuesto_oit_oit_cantidad_usada_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='oit',
            name='completado',
            field=models.BooleanField(default=False, verbose_name='Completado'),
        ),
    ]