# Generated by Django 4.1.5 on 2023-01-11 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productoApp', '0015_rename_marca_marca_name_items_marca'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagenproducto',
            old_name='imag',
            new_name='imagen',
        ),
        migrations.AlterField(
            model_name='imagenproducto',
            name='items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='productoApp.items'),
        ),
    ]
