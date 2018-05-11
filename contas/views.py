from django.shortcuts import render, redirect
from contas.models import PROFESSOR

def indexProfessor(request):
    
    professores = PROFESSOR.objects.all()
    context = {'professores': professores}
    return render(request, 'professor/index.html', context)

def editProfessor(request):
    professores = PROFESSOR.objects.get(id=id)
    context = {'professores': professores}
    return render(request, 'professor/edit.html', context)
    
def updateProfessor(request, id):
    professor = PROFESSOR.objects.get(id=id)
    professor.NOME = request.POST['nome']
    professor.EMAIL = request.POST['email']
    professor.save()
    return redirect('/professor/')

def deleteProfessor(request, id):
    professor = PROFESSOR.objects.get(id=id)
    professor.delete()
    return redirect('/professor/')