from django.db import models
from stdimage.models import StdImageField
import uuid

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Emissor_Pf(models.Model):
    nome = models.CharField('Nome', max_length=100)
    telefone = models.CharField('Telefone', max_length=11)
    email = models.EmailField('E-mail')
    foto = StdImageField('Foto', null=True, blank=True, upload_to=get_file_path,variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', blank=True, max_length=200)
    linkedin = models.CharField('LinkedIn', blank=True, max_length=200)
    twitter = models.CharField('Twitter', blank=True, max_length=200)
    instagram = models.CharField('Instagram', blank=True, max_length=200)
    imagem = StdImageField('Imagem', null=True, blank=True, upload_to=get_file_path,variations={'thumb': {'width': 420, 'height': 260, 'crop': True}})

    class Meta:
        abstract = False
        verbose_name = 'Emissor'
        verbose_name_plural = 'Emissores'

    def __str__(self):
        return self.nome


class Emissor_Pj(models.Model):
    nome = models.CharField('Nome', max_length=100)
    telefone = models.CharField('Telefone', max_length=11)
    email = models.EmailField('E-mail')
    foto = StdImageField('Foto', null=True, blank=True, upload_to=get_file_path,variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', blank=True, max_length=200)
    linkedin = models.CharField('LinkedIn', blank=True, max_length=200)
    twitter = models.CharField('Twitter', blank=True, max_length=200)
    instagram = models.CharField('Instagram', blank=True, max_length=200)
    imagem = StdImageField('Imagem', null=True, blank=True, upload_to=get_file_path,variations={'thumb': {'width': 420, 'height': 260, 'crop': True}})

    class Meta:
        abstract = False
        verbose_name = 'Emissor'
        verbose_name_plural = 'Emissores'

    def __str__(self):
        return self.nome

class Coletor_Pf(models.Model):
    nome = models.CharField('Nome', max_length=100)
    telefone = models.CharField('Telefone', max_length=11)
    email = models.EmailField('E-mail')
    foto = StdImageField('Foto', null=True, blank=True, upload_to=get_file_path,variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', blank=True, max_length=200)
    linkedin = models.CharField('LinkedIn', blank=True, max_length=200)
    twitter = models.CharField('Twitter', blank=True, max_length=200)
    instagram = models.CharField('Instagram', blank=True, max_length=200)

    class Meta:
        abstract = False
        verbose_name = 'Coletor'
        verbose_name_plural = 'Coletores'

    def __str__(self):
        return self.nome

class Coletor_Pj(models.Model):
    nome = models.CharField('Nome', max_length=100)
    telefone = models.CharField('Telefone', max_length=11)
    email = models.EmailField('E-mail')
    foto = StdImageField('Foto', null=True, blank=True, upload_to=get_file_path,variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', blank=True, max_length=200)
    linkedin = models.CharField('LinkedIn', blank=True, max_length=200)
    twitter = models.CharField('Twitter', blank=True, max_length=200)
    instagram = models.CharField('Instagram', blank=True, max_length=200)

    class Meta:
        abstract = False
        verbose_name = 'Coletor'
        verbose_name_plural = 'Coletores'

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    logradouro = models.CharField('Logradouro', max_length=200)
    numero = models.CharField('N??mero', max_length=10)
    cidade = models.CharField('Cidade', max_length=50)
    bairro = models.CharField('Bairro', max_length=100)
    complemento = models.CharField('Complemento', max_length=200)
    cep = models.CharField('CEP', max_length=8)

    class Meta:
        verbose_name = 'Endere??o'
        verbose_name_plural = 'Endere??os'

    def __str__(self):
        return self.logradouro

class SolicitacaoColeta(models.Model):
    OPCOES = (
        ('Celular', 'Celular'),
        ('Computador', 'Computador'),
        ('Televisao', 'Televisao'),
        ('Carregador', 'Carregador'),
        ('Pilha', 'Pilha'),
        ('Outros', 'Outros')
    )

    valor = models.FloatField('Valor', max_length=200)
    dataSolicitacao = models.DateField('Data', max_length=10)
    qtdItens = models.IntegerField('Quantidade de Itens')
    tipoProduto = models.CharField('Tipo de Produto', blank=True, max_length=100, choices=OPCOES)
    coletorPf = models.ForeignKey(Coletor_Pf, on_delete=models.DO_NOTHING)

class PagamentoTaxaColeta(models.Model):
    status = models.CharField('Status', max_length=200)
    desconto = models.FloatField('Desconto')








