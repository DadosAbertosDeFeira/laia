# Generated by Django 3.2.6 on 2021-09-22 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_auto_20210920_0833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orgao',
            old_name='esfera_orgao',
            new_name='esfera',
        ),
    ]
