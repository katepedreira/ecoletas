# Generated by Django 4.1.1 on 2022-11-22 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("aplic", "0003_coletor_pf_imagem_coletor_pj_imagem_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="coletor_pf", name="imagem",),
    ]