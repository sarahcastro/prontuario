#-*- coding: utf-8 -*-
from django.forms import ModelForm
from models import Paciente, Evolucao
from django.contrib.auth.models import User
from django import forms
#from mangaverde.modulos.geograficos.models import Cidades
from modulos.utils.cpf import CPF
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

class FormAlterarDados(ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','email','password','last_name')
        exclude = ('email','username','first_name','last_name')

    CHOICES = (
        ('masculino', 'Masculino'),
        ('feminino','Feminino'),
    )
    STATUS = (
        ('estavel', 'Estavel'),
        ('risco_de_vida','Risco de vida'),
        ('alta','Alta'),
        ('coma_induzido','Coma induzido'),
        ('observacao', 'Observacao')
    )
    nome = forms.CharField(max_length = 255,required=False)
    #cidade = forms.ModelChoiceField(queryset=Cidades.objects.filter(fl_ativo='s').all())
    cidade =  forms.CharField(max_length = 255,required=False)
    endereco = forms.CharField(max_length = 255,required=False)
    cpf = forms.CharField(max_length = 15,required=False)
    #email = forms.EmailField(required=False)
    #rg = forms.CharField(max_length = 30,required=False)
    nascimento = forms.DateField(required=False)
    sexo = forms.ChoiceField(choices=CHOICES,required=False)
    status = forms.ChoiceField(choices=STATUS,required=False)
    #opt = forms.BooleanField(required=True)
    data = forms.DateTimeField(input_formats='%d-%m-%Y %H:%M:%S',required=False)
    confirme = forms.CharField(max_length=30, widget=forms.PasswordInput)


    def __init__(self, *args, **kwargs):
        self.base_fields['password'].widget = forms.PasswordInput()
        super(FormAlterarDados, self).__init__(*args, **kwargs)

    def clean_confirme(self):
        if self.cleaned_data['confirme'] != self.data['password']:
            raise forms.ValidationError('Confirmacao da senha nao confere, por favor verifique se a senha e o confirme estao iguais')
        return self.cleaned_data['confirme']

    def save(self, commit=True):
        usuario = super(FormAlterarDados, self).save(commit=False)
        usuario.set_password(self.cleaned_data['password'])
        usuario.username = self.cleaned_data['email']

        if commit:
            usuario.save()

        return usuario


class FormEvolucao(ModelForm):
    class Meta:
        model = Evolucao
        fields = ('acao',)

class FormPaciente(ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','email','password','last_name')
        exclude = ('username',)

    CHOICES = (
        ('masculino', 'Masculino'),
        ('feminino','Feminino'),
    )
    STATUS = (
        ('estavel', 'Estavel'),
        ('risco_de_vida','Risco de vida'),
        ('alta','Alta'),
        ('coma_induzido','Coma induzido'),
        ('observacao', 'Observacao')
    )

    nome = forms.CharField(max_length = 255)
    #email = forms.EmailField(max_length = 75)
    cpf = forms.CharField(max_length = 15)
    sexo = forms.ChoiceField(choices=CHOICES)
    status = forms.ChoiceField(choices=STATUS)
    sintomas = forms.CharField(max_length=2000)
    nascimento = forms.DateTimeField(input_formats='%d-%m-%Y %H:%M:%S',required=False)
    peso = forms.FloatField()
    altura = forms.FloatField()
    evolucao = forms.ModelChoiceField(queryset=Evolucao.objects.all())


    dataEntrada = forms.DateTimeField(input_formats='%d-%m-%Y %H:%M:%S',required=False)
    #confirme = forms.CharField(max_length=30, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.base_fields['password'].widget = forms.PasswordInput()
        super(FormPaciente, self).__init__(*args, **kwargs)

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email'],).count():
            raise forms.ValidationError('Ja existe um usuario cadastrado com este EMAIL')
        return self.cleaned_data['email']

    def clean_cpf(self):
        if (self.cleaned_data['cpf'] == '111.111.111-11' or self.cleaned_data['cpf'] == '222.222.222-22'
        or self.cleaned_data['cpf'] == '333.333.333-33' or self.cleaned_data['cpf'] == '444.444.444-44'
        or self.cleaned_data['cpf'] == '555.555.555-55' or self.cleaned_data['cpf'] == '666.666.666-66'
        or self.cleaned_data['cpf'] == '777.777.777-77' or self.cleaned_data['cpf'] == '888.888.888-88'
        or self.cleaned_data['cpf'] == '999.999.999-99' or self.cleaned_data['cpf'] == '000.000.000-00') :
            raise forms.ValidationError('Por favor informe um CPF valido')
            return self.cleaned_data['cpf']
        else:
            if Paciente.objects.filter(cpf=self.cleaned_data['cpf'],).count():
                raise forms.ValidationError('Ja existe um usuario cadastrado com este CPF')
                return self.cleaned_data['cpf']
            else:
                cpf = CPF(self.cleaned_data['cpf'])
                if cpf.valido():
                    return self.cleaned_data['cpf']
                else:
                    raise forms.ValidationError('Por favor informe um CPF valido')
                    return self.cleaned_data['cpf']

    def save(self, commit=True):
        usuario = super(FormPaciente, self).save(commit=False)
        usuario.set_password(self.cleaned_data['password'])
        usuario.username = self.cleaned_data['email']

        if commit:
            usuario.save()

        return usuario
