# Generated by Django 3.2.6 on 2021-09-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pedidos", "0006_alter_denuncia_status"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="denuncia",
            options={"verbose_name": "Denúncia", "verbose_name_plural": "Denúncias"},
        ),
        migrations.AddField(
            model_name="denuncia",
            name="titulo",
            field=models.CharField(default="", max_length=100, verbose_name="Título"),
            preserve_default=False,
        ),
    ]
