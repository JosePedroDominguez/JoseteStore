# Generated by Django 4.1.5 on 2023-01-24 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productoApp', '0022_alter_items_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='imagen',
            field=models.ImageField(upload_to='productos'),
        ),
    ]
