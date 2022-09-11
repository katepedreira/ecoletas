from django.contrib import admin

from .models import Emissor, Coletor, Endereco, SolicitacaoColeta, PagamentoTaxaColeta


@admin.register(Emissor)
class EmissorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email')

@admin.register(Coletor)
class ColetorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email')

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro', 'numero', 'cidade', 'bairro', 'complemento', 'cep')

@admin.register(SolicitacaoColeta)
class SolicitacaoColetaAdmin(admin.ModelAdmin):
    list_display = ('valor', 'dataSolicitacao', 'qtdItens', 'tipoProduto')

@admin.register(PagamentoTaxaColeta)
class SolicitacaoColetaAdmin(admin.ModelAdmin):
    list_display = ('status', 'desconto')

