from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from .models import Emissor_Pf, Emissor_Pj, Coletor_Pf, Coletor_Pj

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

class ColetorPfView(ListView):
    template_name = 'coletor_pf.html'

    def get_context_data(self, **kwargs):
        context = super(ColetorPfView, self).get_context_data(**kwargs)
        #id = self.kwargs['id']
        context['coletor_pf'] = Coletor_Pf.objects.order_by('nome').all()
        return context


class ColetorPjView(TemplateView):
    template_name = 'coletor_pj.html'

    def get_context_data(self, **kwargs):
        context = super(ColetorPjView, self).get_context_data(**kwargs)
        context['coletor_pj'] = Coletor_Pj.objects.order_by('nome').all()
        return context

class PaginaColetoresPF(TemplateView):
    template_name = 'pagina-coletores-pf.html'

    def get_context_data(self, **kwargs):
        context = super(PaginaColetoresPF, self).get_context_data(**kwargs)
        context['pagina-coletores-pf'] = Coletor_Pf.objects.order_by('nome').all()
        return context

