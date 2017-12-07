#-*- coding: utf-8 -*-
from django.contrib import admin
from models import Paciente, Evolucao
from forms import FormPaciente, FormEvolucao

class EvolucaoInline(admin.StackedInline):
    model = Evolucao

class PacienteAdmin(admin.ModelAdmin):
    #add_form = FormPaciente
    #form = FormPaciente

    list_display = ['nome', 'cpf', 'dataEntrada']
    inlines = [
        EvolucaoInline
    ]

admin.site.register(Paciente, PacienteAdmin)
#admin.site.register(Evolucao, EvolucaoAdmin)
