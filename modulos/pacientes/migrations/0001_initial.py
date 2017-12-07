# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 17:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evolucao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sintomas', models.TextField(blank=True, help_text=b'', null=True, verbose_name=b'Acao relacionada ao paciente')),
                ('dataEntrada', models.DateTimeField(auto_now_add=True, null=True, verbose_name=b'Data e hora')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text=b'', max_length=255, null=True, verbose_name=b'Nome')),
                ('hospital', models.CharField(blank=True, help_text=b'', max_length=255, null=True, verbose_name=b'Hospital')),
                ('cpf', models.CharField(help_text=b'', max_length=15, null=True, unique=True, verbose_name=b'CPF')),
                ('peso', models.FloatField(help_text=b'', null=True, verbose_name=b'Peso')),
                ('altura', models.FloatField(help_text=b'', null=True, verbose_name=b'Altura')),
                ('sexo', models.CharField(blank=True, choices=[(b'masculino', b'Masculino'), (b'feminino', b'Feminino')], max_length=30)),
                ('nascimento', models.DateTimeField(blank=True, help_text=b'', null=True, verbose_name=b'Data de nascimento')),
                ('status', models.CharField(blank=True, choices=[(b'estavel', b'Estavel'), (b'risco_de_vida', b'Risco de vida'), (b'alta', b'Alta'), (b'coma_induzido', b'Coma induzido'), (b'observacao', b'Observacao')], max_length=30, verbose_name=b'Estado clinico')),
                ('sintomas', models.TextField(blank=True, help_text=b'', null=True, verbose_name=b'Sintomas')),
                ('dataEntrada', models.DateTimeField(auto_now_add=True, null=True, verbose_name=b'Data e hora de entrada')),
                ('evolucao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evolucao_paciente', to='pacientes.Evolucao', verbose_name=b'Evolucao')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Paciente',
            },
        ),
    ]