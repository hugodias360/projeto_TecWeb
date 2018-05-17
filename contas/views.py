from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
#from contas.forms import ProfessorForm
from contas.models import PROFESSOR
from contas.models import COORDENADOR
from contas.models import ALUNO


# CRUD ALUNO
def indexAluno(request):
    alunos = ALUNO.objects.all()
    context = {'alunos': alunos}
    return render(request, 'aluno/index.html', context)

def editAluno(request, id):
    alunos = ALUNO.objects.get(id=id)
    context = {'alunos': alunos}
    return render(request, 'aluno/edit.html', context)

def updateAluno(request, id):
    aluno = ALUNO.objects.get(id=id)
    aluno.LOGIN = request.POST['login']
    aluno.SENHA = request.POST['senha']
    aluno.NOME = request.POST['nome']
    aluno.EMAIL = request.POST['email']
    aluno.CELULAR = request.POST['celular']
    aluno.save()
    return redirect('/contas/aluno/')


def deleteAluno(request, id):
    aluno = ALUNO.objects.get(id=id)
    aluno.delete()
    return redirect('/contas/aluno/')

# CRUD COORDENADOR
def indexCoordenador(request):
    coordenadores = COORDENADOR.objects.all()
    context = {'coordenadores': coordenadores}
    return render(request, 'coordenador/index.html', context)

def editCoordenador(request, id):
    coordenadores = COORDENADOR.objects.get(id=id)
    context = {'coordenadores': coordenadores}
    return render(request, 'coordenador/edit.html', context)

def updateCoordenador(request, id):
    coordenador = COORDENADOR.objects.get(id=id)
    coordenador.LOGIN = request.POST['login']
    coordenador.SENHA = request.POST['senha']
    coordenador.NOME = request.POST['nome']
    coordenador.EMAIL = request.POST['email']
    coordenador.CELULAR = request.POST['celular']
    coordenador.save()
    return redirect('/contas/coordenador/')

def deleteCoordenador(request, id):
    coordenador = COORDENADOR.objects.get(id=id)
    coordenador.delete()
    return redirect('/contas/coordenador/')

# CRUD PROFESSOR
def indexProfessor(request):
    professores = PROFESSOR.objects.all()
    context = {'professores': professores}
    return render(request, 'professor/index.html', context)

#def createProfessor(request):
#   form = ProfessorForm(request.POST or None)

#    if request.method == 'POST' and form.is_valid():
#        form.save()
#        return HttpResponseRedirect('/contas/professor/')

#    context = RequestContext(request, {'form': form})
#    return render(request, 'professor/index.html', context)

def editProfessor(request, id):
    professores = PROFESSOR.objects.get(id=id)
    context = {'professores': professores}
    return render(request, 'professor/edit.html', context)
    
def updateProfessor(request, id):
    professor = PROFESSOR.objects.get(id=id)
    professor.LOGIN = request.POST['login']
    professor.SENHA = request.POST['senha']
    professor.NOME = request.POST['nome']
    professor.EMAIL = request.POST['email']
    professor.CELULAR = request.POST['celular']
    professor.APELIDO = request.POST['apelido']
    professor.save()
    return redirect('/contas/professor/')

def deleteProfessor(request, id):
    professor = PROFESSOR.objects.get(id=id)
    professor.delete()
    return redirect('/contas/professor/')