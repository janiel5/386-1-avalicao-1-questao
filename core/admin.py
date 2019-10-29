from django.contrib import admin
from.models import *

# Register your models here.
class DespesaAdmin(admin.ModelAdmin):
    list_display = ("data_criacao","tipo_despesa","descricao","forma_pagamento","vencimento","quitado")
    list_filter =  ("quitado","vencimento")
    date_hierarchy = "vencimento"

admin.site.register(Despesa, DespesaAdmin)

