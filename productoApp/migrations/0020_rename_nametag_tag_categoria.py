# Generated by Django 4.1.5 on 2023-01-13 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productoApp', '0019_rename_name_marca_marca'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='nametag',
            new_name='categoria',
        ),
    ]
