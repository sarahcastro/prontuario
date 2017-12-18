# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File

from django.contrib.auth.decorators import login_required


from forms import FormPaciente
from models import Paciente

def login(request):
    return render(request, 'login.html', {})

@login_required
def infopaciente(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes.html', locals())
