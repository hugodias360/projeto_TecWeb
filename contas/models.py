from django.db import models

class COORDENADOR(models.Model):
    LOGIN = models.CharField("LOGIN", max_length=100)
    SENHA = models.CharField("SENHA", max_length=30)
    NOME = models.CharField("NOME", max_length=30)
    EMAIL = models.EmailField("EMAIL", max_length=200)
    CELULAR = models.IntegerField("CELULAR")
    DT_EXPIRACAO = models.DateField("DT_EXPIRACAO", max_length=100)

class ALUNO(models.Model):
    LOGIN = models.CharField("LOGIN", max_length=100)
    SENHA = models.CharField("SENHA", max_length=30)
    NOME = models.CharField("NOME", max_length=100)
    EMAIL = models.EmailField("EMAIL", max_length=200)
    CELULAR = models.IntegerField("CELULAR")
    DT_EXPIRACAO = models.DateField("DT_EXPIRACAO")
    RA = models.IntegerField("RA")

class PROFESSOR(models.Model):
    
    LOGIN = models.CharField("LOGIN", max_length=30)
    SENHA = models.CharField("SENHA", max_length=50)
    NOME = models.CharField("NOME", max_length=100)
    EMAIL = models.EmailField("EMAIL", max_length=100)
    CELULAR = models.CharField("CELULAR", max_length=50)
    DT_EXPIRACAO = models.DateField("DT_EXPIRACAO", max_length=100)
    APELIDO = models.CharField("APELIDO", max_length=100)

class MENSAGEM(models.Model):
    ASSUNTO = models.CharField("ASSUNTO", max_length=300)
    REFERENCIA = models.CharField("REFERENCIA", max_length=300)
    CONTEUDO = models.CharField("CONTEUDO", max_length=400)
    STATUS = models.CharField("STATUS", max_length=20)
    DT_ENVIO = models.DateField("DT_ENVIO")
    DT_RESPOSTA = models.DateField("DT_RESPOSTA")
    RESPOSTA = models.CharField("RESPOSTA", max_length=400)


    ID_PROFESSOR = models.ManyToManyField("contas.PROFESSOR")
    ID_ALUNO = models.ManyToManyField("contas.ALUNO")
