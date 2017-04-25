from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.paginadoctor, name='doctorInicio'),
    url(r'^itinerario/$', views.paginaitinerario, name='Itinerario'),
]
