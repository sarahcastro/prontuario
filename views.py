# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File


from modulos.pacientes.forms import FormPaciente
from modulos.pacientes.models import Paciente

from django.contrib.auth.decorators import login_required

def index_view(request):
    form = FormPaciente()
    return render_to_response(
        'index.html',
        locals(),
        context_instance=RequestContext(request),)

@login_required(login_url='/accounts/login/')
def infopaciente(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes.html', locals())

def login_view(request):
    return render_to_response(
        'login.html',
        locals(),
        context_instance=RequestContext(request),)


class FormContato(forms.Form):
    nome = forms.CharField(max_length=50,required=True)
    email = forms.EmailField(max_length=50,required=True)
    assunto = forms.CharField(max_length=50,required=True)
    mensagem = forms.Field(widget=forms.Textarea,required=True)

    def enviar(self):
        assunto = 'ProntuarioOnline - [Ouvidoria] Contato enviado pelo site'
        destino = 'sarah.dheyne@gmail.com'
        email = self.cleaned_data["email"]
        texto = """
        Nome: %(nome)s
        E-mail: %(email)s
        Assunto:%(assunto)s
        Mensagem:
        %(mensagem)s
        """ % self.cleaned_data

        send_mail(
            subject=assunto,
            message=texto,
            from_email=email,
            recipient_list=[destino],
            )


def contato_view(request):

    enviado = False
    form = FormContato()

    if request.method == 'POST':
        form = FormContato(request.POST)

        if form.is_valid():
            form.enviar()
            enviado = True

    return render_to_response(
        'contato.html',
        locals(),
        context_instance=RequestContext(request),)
