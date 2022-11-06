from django.urls import path

from .views import IndexView, SobreView, EmissorPfView, EmissorPjView, ColetorPfView, ColetorPjView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('emissor_pf/', EmissorPfView.as_view(), name='emissor_pf'),
    path('emissor_pj/', EmissorPjView.as_view(), name='emissor_pj'),
    path('coletor_pf/', ColetorPfView.as_view(), name='coletor_pf'),
    path('coletor_pj/', ColetorPjView.as_view(), name='coletor_pj'),
]
