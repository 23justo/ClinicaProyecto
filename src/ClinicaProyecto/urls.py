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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from pacientes.views import inicio,paciente,familia
from Medicamentos.views import medicamentos
from Visitadores.views import visitadores
from Doctores import views
from django.contrib.auth.views import login,logout_then_login



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url de login
    url(r'^$',login,{'template_name':'Usuario/login.html'},name='login'),
    url(r'^logout',logout_then_login,name='logout'),
    # views de app pacientes
    url(r'^inicio/$', login_required(inicio), name='inicio'),
    url(r'^paciente/$', login_required(paciente), name='pacientes'),
    url(r'^familia/$', login_required(familia), name='familias'),
    #views de app docotres
    url(r'^doctor/$', login_required(views.paginadoctor), name='doctores'),
    url(r'^itinerario/$', views.paginaitinerario, name='itinerario'),
    #views de app visitadores
    url(r'^Visitadores/$', login_required(visitadores), name='visitadores'),
    #views de app medicamentos
    url(r'^medicamentos/$', login_required(medicamentos), name='medicamentos'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
