from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from .forms import ProfessorForm
from .models import PROFESSOR


def indexProfessor(request):
    professores = PROFESSOR.objects.all()
    context = {'professores': professores}
    return render(request, 'professor/index.html', context)

def createProfessor(request):
    form = ProfessorForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect('/contas/professor/')

    context = RequestContext(request, {'form': form})
    return render(request, 'professor/index.html', context)

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