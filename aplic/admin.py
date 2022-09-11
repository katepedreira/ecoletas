from django.contrib import admin

from .models import Emissor, Coletor


@admin.register(Emissor)
class EmissorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email')

@admin.register(Coletor)
class ColetorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email')

