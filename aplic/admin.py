from django.contrib import admin

from .models import Emissor_Pf, Emissor_Pj, Coletor_Pf, Coletor_Pj, Endereco, SolicitacaoColeta, PagamentoTaxaColeta


@admin.register(Emissor_Pf)
class EmissorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email')

@admin.register(Emissor_Pj)
class EmissorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email')

@admin.register(Coletor_Pf)
class ColetorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email')

@admin.register(Coletor_Pj)
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

