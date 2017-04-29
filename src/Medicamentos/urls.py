from django.conf.urls import url
from . import views
from Medicamentos.views import editar
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^medicamento/$', views.medicamentos, name='doctorInicio'),
    url(r'^medicamento/editar/(?P<id_medicamento>\d+)$', login_required(editar), name='medicamentoUpdate'),
]
