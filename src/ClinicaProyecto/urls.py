"""ClinicaProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url,include

from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from Usuario.views import inicio
from django.contrib.auth.views import login,logout_then_login



urlpatterns = [
    url(r'^/$', inicio,name='inicio'),
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^paciente/',include('pacientes.urls') ),
    url(r'^doctor/',include('Doctores.urls') ),
    url(r'^familia/',include('pacientes.urls') ),
    url(r'^$',login,{'template_name':'Usuario/login.html'},name='login'),


    #url(r'^medicamento/',include('Medicamentos.urls') ),
    #url(r'^visitador/',include('Visitadores.urls') ),
    #url de login

    #url(r'^logout',logout_then_login,name='logout'),
    # # views de app pacientes
    # url(r'^inicio/$', login_required(inicio), name='inicio'),
    # url(r'^paciente/$', login_required(paciente), name='pacientes'),
    #
    # url(r'^familia/$', login_required(familia), name='familias'),
    # url(r'^paciente/pacienteUpdate/(?P<pk>[0-9]+)/$', login_required(pacienteUpdate), name='paciente_update'),
    # #views de app docotres
    # url(r'^doctor/$', login_required(views.paginadoctor), name='doctores'),
    # url(r'^cita/$', login_required(views.paginaitinerario), name='citas'),
    #url(r'^cita/$', login_required(views.paginaitinerario), name='citas'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

LOGIN_URL =  '/'
