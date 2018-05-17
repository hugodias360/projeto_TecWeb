from django.conf.urls import url
from . import views


urlpatterns= [
    url(r'^professor/$', views.indexProfessor , name='index'),
#    url(r'^professor/create/$', views.createProfessor, name='create'),
    url(r'^professor/edit/(?P<id>\d+)$', views.editProfessor, name='edit'),
    url(r'^professor/edit/update/(?P<id>\d+)$', views.updateProfessor, name='update'),
    url(r'^professor/delete/(?P<id>\d+)$', views.deleteProfessor, name='delete'),
    url(r'^coordenador/$', views.indexCoordenador , name='index'),
    url(r'^aluno/$', views.indexAluno , name='index'),
]