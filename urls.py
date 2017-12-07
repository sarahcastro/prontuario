from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    #url(r'^pacientes/', include('prontuario.modulos.pacientes.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^grappelli/', include('grappelli.urls')),

    #zero
    url(r'^$', include('modulos.pacientes.urls')),
    #cadastro
    #(r'^cadastro/', 'testing.views.cadastro_view'),
    #(r'^alterar_dados/$', 'testing.views.alterardados_view',{}, 'alterar_dados'),
    #(r'^login/$', 'testing.views.login_view',{}, 'entrar'),
    #(r'^logout/$', 'testing.views.logout_view',{}, 'sair'),
    #(r'^esqueceu_sua_senha/$', 'testing.views.esqueceusuasenha_view'),

]
