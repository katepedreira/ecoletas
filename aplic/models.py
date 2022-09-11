from django.db import models

class Emissor(models.Model):
    nome = models.CharField('Nome', max_length=100)
    telefone = models.CharField('Telefone', max_length=11)
    email = models.EmailField('E-mail')
    codEmissor = models.CharField('Código', max_length=100)

    class Meta:
        verbose_name = 'Emissor'
        verbose_name_plural = 'Emissores'

    def __str__(self):
        return self.nome

class Coletor(models.Model):
    nome = models.CharField('Nome', max_length=100)
    telefone = models.CharField('Telefone', max_length=11)
    email = models.EmailField('E-mail')
    codColetor = models.CharField('Código', max_length=100)

    class Meta:
        verbose_name = 'Coletor'
        verbose_name_plural = 'Coletores'

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    codEndereco = models.CharField('Código', max_length=100)
    logradouro = models.CharField('Logradouro', max_length=200)
    numero = models.CharField('Número', max_length=10)
    cidade = models.CharField('Cidade', max_length=50)
    bairro = models.CharField('Bairro', max_length=100)
    complemento = models.CharField('Complemento', max_length=200)
    cep = models.CharField('CEP', max_length=8)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return self.codEndereco

class SolicitacaoColeta(models.Model):
    codSolicitacao = models.CharField('Código', max_length=100)
    valor = models.FloatField('Valor', max_length=200)
    dataSolicitacao = models.DateField('Data', max_length=10)
    qtdItens = models.IntegerField('Quantidade de Itens', max_length=100)
    tipoProduto = models.CharField('Tipo de Produto', max_length=100)

class PagamentoTaxaColeta(models.Model):
    codPagamento = models.CharField('Código', max_length=100)
    status = models.CharField('Status', max_length=200)
    desconto = models.FloatField('Desconto', max_length=10)








