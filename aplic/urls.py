from django.urls import path

from .views import IndexView, SobreView, EmissorPfView, EmissorPjView, ColetorPfView, ColetorPjView, PaginaColetoresPF, DadosTipoProdutoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('emissor_pf/', EmissorPfView.as_view(), name='emissor_pf'),
    path('emissor_pj/', EmissorPjView.as_view(), name='emissor_pj'),
    path('coletor_pf/', ColetorPfView.as_view(), name='coletor_pf'),
    path('coletor_pj/', ColetorPjView.as_view(), name='coletor_pj'),
    path('pagina-coletores-pf/', PaginaColetoresPF.as_view(), name='pagina-coletores-pf'),
    path('dados-grafico-coletas/', DadosTipoProdutoView.as_view(), name='dados-grafico-tipo-produto'),



]
