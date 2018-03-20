from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt

 

def index(request):
    return render(request, "index.html")

@csrf_exempt
@ensure_csrf_cookie
def login(request):
    if request.method == "GET":
        print("Acesso via GET")
    else:
        print("Acesso via POST")
        senha = request.POST.get("senha")
        if senha == "teste123":
            print("Usuario entrou com sucesso")
            return render(request, "index.html")
        else:
            print("“Usuário " + request.POST.get("email") + " digitou a senha errada!")
        print("Acesso via POST")
    return render(request, "login.html")

@csrf_exempt
@ensure_csrf_cookie
def contato(request):
    if request.method == "GET":
        print("Acesso via GET")
        return render(request, "contato.html")
    else:
        print("Acesso via POST, Nome: " + request.POST.get("nome") + " Sobrenome:" + request.POST.get("sobrenome"))
    return render(request, "contato.html")