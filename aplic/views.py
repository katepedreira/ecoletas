from django.shortcuts import render

from django.views.generic import TemplateView, ListView
from .models import Emissor_Pf, Emissor_Pj, Coletor_Pf, Coletor_Pj, SolicitacaoColeta
from django.db.models import Count
from chartjs.views.lines import BaseLineChartView

class IndexView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['coletor_pf'] = Coletor_Pf.objects.order_by('?').all()
        return context


class SobreView(TemplateView):
    template_name = 'about-us.html'

class EmissorPfView(TemplateView):
    template_name = 'emissor_pf.html'

    def get_context_data(self, **kwargs):
        context = super(EmissorPfView, self).get_context_data(**kwargs)
        context['emissor_pf'] = Emissor_Pf.objects.order_by('nome').all()
        return context

class EmissorPjView(TemplateView):
    template_name = 'emissor_pj.html'

    def get_context_data(self, **kwargs):
        context = super(EmissorPjView, self).get_context_data(**kwargs)
        id = self.kwargs['id']
        context['emissor_pj'] = Emissor_Pj.objects.order_by('nome').all()
        return context

class ColetorPfView(TemplateView):
    template_name = 'coletor_pf.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ColetorPfView, self).get_context_data(**kwargs)
        #id = self.kwargs['id']
        context['coletor_pf'] = Coletor_Pf.objects.order_by('nome').all()
        return context


class ColetorPjView(TemplateView):
    template_name = 'coletor_pj.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ColetorPjView, self).get_context_data(**kwargs)
        context['coletor_pj'] = Coletor_Pj.objects.order_by('nome').all()
        return context

class PaginaColetoresPF(TemplateView):
    template_name = 'pagina-coletores-pf.html'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(PaginaColetoresPF, self).get_context_data(**kwargs)
        context['pagina-coletores-pf'] = Coletor_Pf.objects.order_by('nome').all()
        return context

class PaginaColetoresPJ(TemplateView):
    template_name = 'pagina-coletores-pj.html'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(PaginaColetoresPJ, self).get_context_data(**kwargs)
        context['pagina-coletores-pj'] = Coletor_Pj.objects.order_by('nome').all()
        return context

class DadosTipoProdutoView(BaseLineChartView):

    def get_labels(self):
        labels = ['Celular',
        'Computador',
        'Televisao',
        'Carregador']
        return labels

    def get_data(self):
        resultado = []
        dados = []
        queryset = SolicitacaoColeta.objects.filter(tipoProduto='Celular')
        #queryset = SolicitacaoColeta.objects.order_by('tipoProduto').annotate(total=Count('tipoProduto'))
        total = 0
        for linha in queryset:
            total = total + linha.qtdItens
        dados.append(total)
        queryset = SolicitacaoColeta.objects.filter(tipoProduto='Computador')
        #queryset = SolicitacaoColeta.objects.order_by('tipoProduto').annotate(total=Count('tipoProduto'))
        total = 0
        for linha in queryset:
            total = total + linha.qtdItens
        dados.append(total)
        queryset = SolicitacaoColeta.objects.filter(tipoProduto='Televisao')
        #queryset = SolicitacaoColeta.objects.order_by('tipoProduto').annotate(total=Count('tipoProduto'))
        total = 0
        for linha in queryset:
            total = total + linha.qtdItens
        dados.append(total)
        queryset = SolicitacaoColeta.objects.filter(tipoProduto='Carregador')
        #queryset = SolicitacaoColeta.objects.order_by('tipoProduto').annotate(total=Count('tipoProduto'))
        total = 0
        for linha in queryset:
            total = total + linha.qtdItens
        dados.append(total)
        resultado.append(dados)
        return resultado


