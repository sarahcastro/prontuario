from django.conf.urls import include, url
from django.contrib import admin
#from views import infopaciente
from django.contrib.auth.views import login

urlpatterns = [
    #url(r'^pacientes/', include('prontuario.modulos.pacientes.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^infopaciente/', include('modulos.pacientes.urls')),


    #zero

    #url(r'^$', include('modulos.pacientes.urls')),

]
