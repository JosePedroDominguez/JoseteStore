# Generated by Django 4.1.5 on 2023-01-24 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productoApp', '0023_alter_items_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenproducto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
        migrations.AlterField(
            model_name='items',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
