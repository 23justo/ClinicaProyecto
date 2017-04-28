from django.conf.urls import url
from . import views
from Doctores.views import editar,editarCita
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^doctor/$', login_required(views.paginadoctor), name='doctorInicio'),
    url(r'^cita/$', login_required(views.paginaitinerario), name='Itinerario'),
    url(r'^cita/editarCita/(?P<id_cita>\d+)$', login_required(editarCita), name='citaUpdate'),
    url(r'^doctor/editar/(?P<id_doctor>\d+)$', login_required(editar), name='doctorUpdate'),
]
