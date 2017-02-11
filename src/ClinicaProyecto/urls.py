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
from pacientes import views
from pacientes.views import inicio
from pacientes.views import paciente,familia
from Doctores import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # views de app pacientes
    url(r'^inicio/$', inicio, name='inicio'),
    url(r'^paciente/$', paciente, name='pacientes'),
    url(r'^familia/$', familia, name='familias'),
    #views de app docotres
    url(r'^paginadoctor/$', views.paginadoctor, name='doctores'),
    url(r'^itinerario/$', views.paginaitinerario, name='itinerario'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
