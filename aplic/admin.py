from django.contrib import admin

from .models import Emissor

@admin.register(Emissor)
class EmissorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email')

