# Generated by Django 4.1.1 on 2022-11-26 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("aplic", "0004_remove_coletor_pf_imagem"),
    ]

    operations = [
        migrations.AddField(
            model_name="endereco",
            name="coletor",
            field=models.ForeignKey(
                default="NA",
                on_delete=django.db.models.deletion.CASCADE,
                to="aplic.coletor_pf",
            ),
        ),
    ]