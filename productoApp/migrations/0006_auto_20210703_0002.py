# Generated by Django 3.2.4 on 2021-07-03 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productoApp', '0005_alter_items_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='items',
            name='tag',
        ),
    ]
