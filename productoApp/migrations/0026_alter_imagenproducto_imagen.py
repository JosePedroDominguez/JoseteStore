# Generated by Django 4.1.5 on 2023-01-24 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productoApp', '0025_alter_imagenproducto_imagen_alter_items_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenproducto',
            name='imagen',
            field=models.ImageField(upload_to='productos'),
        ),
    ]