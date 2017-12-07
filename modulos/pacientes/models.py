#-*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User
#from measurement.measures import Weight
import random
import string


class Paciente(models.Model):
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
    usuario = models.OneToOneField(User)
    #email = models.EmailField("Email", blank = False, null = True, help_text = "", unique = True)
    nome = models.CharField("Nome", max_length = 255, blank = True, null = True, help_text = "")
    queixa = models.CharField("Queixa principal", max_length = 255, blank = True, null = True, help_text = "")

    cpf = models.CharField("CPF", max_length = 15, blank = False, null = True, help_text = "", unique=True)
    peso = models.FloatField("Peso", blank = False, null = True, help_text = "")
    altura = models.FloatField("Altura", blank = False, null = True, help_text = "")
    sexo = models.CharField(max_length=30,choices=CHOICES, blank=True)
    nascimento = models.DateTimeField("Data de nascimento", blank = True, null = True, help_text = "")
    status = models.CharField("Estado clinico", max_length=30,choices=STATUS, blank=True)
    sintomas = models.TextField("Sintomas apresentados", blank = True, null = True, help_text = "")
    #evolucao = models.ForeignKey(Evolucao, verbose_name = "Evolucao", related_name = "evolucao_paciente", blank = True, null = True)

    #cidade = models.CharField("Cidade", max_length = 255, blank = True, null = True, help_text = "")

    #opt = models.BooleanField("OPT", help_text = "O usuario deseja receber emails com noticias e ofertas da Manga Verde ?",blank = True)
    dataEntrada = models.DateTimeField("Data e hora de entrada", auto_now_add = True, blank = True, null = True)

    class Meta:
        verbose_name = u"Paciente"
        verbose_name_plural = u"Pacientes"

    def __str__(self) :
        return u"{0} - {1}" .format(self.nome,self.cpf)

    def __unicode__(self) :
        return u"{0} - {1}" .format(self.nome,self.cpf)

    def getClass(self) :
        return "Paciente"

    def get_senha(self):
        digits = "".join( [random.choice(string.digits) for i in xrange(8)] )
        chars = "".join( [random.choice(string.letters) for i in xrange(15)] )
        mensagem = str(self.dataEntrada.second) + str(self.id) + str(self.dataEntrada.minute) + str(self.dataEntrada.day) + str(self.dataEntrada.second) + digits + chars
        mensagem_cifrada = base64.b64encode(mensagem)
        return "%s" % (str(mensagem_cifrada))[:10]
    get_senha.short_description = u"Senha"

    



class Evolucao(models.Model):
    paciente = models.ForeignKey(Paciente, verbose_name = "Paciente", related_name = "evolucao_paciente", blank = True, null = True)

    acao = models.TextField("Acao relacionada ao paciente", blank = True, null = True, help_text = "")
    dataEntrada = models.DateTimeField("Data e hora", auto_now_add = True, blank = True, null = True)

    class Meta:
        verbose_name = u"Ocorrência em:"
        verbose_name_plural = u"Evoluções"

    def __str__(self) :
        return u"{0} - {1} (...)" .format(self.dataEntrada.strftime("%d/%m/%Y - %H:%M:%S"),self.acao[0:100])

    def __unicode__(self) :
        return u"{0} - {1} (...)" .format(self.dataEntrada.strftime("%d/%m/%Y - %H:%M:%S"),self.acao[0:100])

    def getClass(self) :
        return "Evolucao"
