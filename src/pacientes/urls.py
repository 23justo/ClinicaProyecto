from django.conf.urls import url,include
from . import views
from pacientes.views import editar,editarFam
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^paciente/$', login_required(views.paciente), name='pacienteInicio'),
    url(r'^familia/$', login_required(views.familia), name='familiaInicio'),
    url(r'^paciente/editar/(?P<id_paciente>\d+)$', login_required(editar), name='pacienteUpdate'),
    url(r'^familia/editar/(?P<id_familia>\d+)$', login_required(editarFam), name='familiaUpdate'),
]
