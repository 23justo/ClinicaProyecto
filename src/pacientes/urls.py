from django.conf.urls import url,include
from . import views
from pacientes.views import editar,editarFam

urlpatterns = [

    url(r'^paciente/$', views.paciente, name='pacienteInicio'),
    url(r'^familia/$', views.familia, name='familiaInicio'),
    url(r'^paciente/editar/(?P<id_paciente>\d+)$', editar, name='pacienteUpdate'),
    url(r'^familia/editar/(?P<id_familia>\d+)$', editarFam, name='familiaUpdate'),
]
