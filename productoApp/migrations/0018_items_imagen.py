# Generated by Django 4.1.5 on 2023-01-13 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productoApp', '0017_remove_items_imag'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
