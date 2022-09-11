# Generated by Django 2.2.19 on 2022-09-11 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0003_endereco'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitacaoColeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codSolicitacao', models.CharField(max_length=100, verbose_name='Código')),
                ('valor', models.IntegerField(max_length=200, verbose_name='Valor')),
                ('dataSolicitacao', models.DateField(max_length=10, verbose_name='Data')),
                ('qtdItens', models.IntegerField(max_length=100, verbose_name='Quantidade de Itens')),
                ('tipoProduto', models.CharField(max_length=100, verbose_name='Tipo de Produto')),
            ],
        ),
    ]