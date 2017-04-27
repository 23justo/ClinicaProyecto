from django.conf.urls import url
from . import views
from Doctores.views import editar

urlpatterns = [
    url(r'^doctor/$', views.paginadoctor, name='doctorInicio'),
    url(r'^itinerario/$', views.paginaitinerario, name='Itinerario'),
    url(r'^doctor/editar/(?P<id_doctor>\d+)$', editar, name='doctorUpdate'),
]
