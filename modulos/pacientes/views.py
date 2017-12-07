# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File


from forms import FormPaciente
from models import Paciente

def index_view(request):
    form = FormPaciente()
    return render(request, 'index.html', locals())
