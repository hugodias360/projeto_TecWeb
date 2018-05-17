from django.conf.urls import url
from . import views


urlpatterns= [
    #URLS PROFESSOR
    url(r'^professor/$', views.indexProfessor , name='index'),
#    url(r'^professor/create/$', views.createProfessor, name='create'),
    url(r'^professor/edit/(?P<id>\d+)$', views.editProfessor, name='edit'),
    url(r'^professor/edit/update/(?P<id>\d+)$', views.updateProfessor, name='update'),
    url(r'^professor/delete/(?P<id>\d+)$', views.deleteProfessor, name='delete'),

    #URLS COORDENADOR
    url(r'^coordenador/$', views.indexCoordenador , name='index'),
    url(r'^coordenador/edit/(?P<id>\d+)$', views.editCoordenador, name='edit'),
    url(r'^coordenador/edit/update/(?P<id>\d+)$', views.updateCoordenador, name='update'),
    url(r'^coordenador/delete/(?P<id>\d+)$', views.deleteCoordenador, name='delete'),

    #URLS ALUNO
    url(r'^aluno/$', views.indexAluno , name='index'),
    url(r'^aluno/edit/(?P<id>\d+)$', views.editAluno, name='edit'),
    url(r'^aluno/edit/update/(?P<id>\d+)$', views.updateAluno, name='update'),
    url(r'^aluno/delete/(?P<id>\d+)$', views.deleteAluno, name='delete'),
]