# Generated by Django 4.1.1 on 2022-11-26 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("aplic", "0006_remove_endereco_coletor"),
    ]

    operations = [
        migrations.RemoveField(model_name="coletor_pj", name="imagem",),
    ]
