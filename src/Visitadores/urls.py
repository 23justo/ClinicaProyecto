from django.conf.urls import url,include
from . import views
from pacientes.views import editar
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^visitador/$', login_required(views.visitadores), name='visitadorInicio'),

    url(r'^visitador/editar/(?P<id_visitador>\d+)$', login_required(editar), name='visitadorUpdate'),
]
