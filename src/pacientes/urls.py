from django.conf.urls import url,include
from . import views
from pacientes.views import editar

urlpatterns = [
    url(r'^paciente/editar/(?P<id_paciente>\d+)$', editar, name='pacienteUpdate'),
    url(r'^paciente/$', views.paciente, name='pacienteInicio'),
    url(r'^familia/$', views.familia, name='familiaInicio'),
]
