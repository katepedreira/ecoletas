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





