from django.db import models

class ATIVIDADE (models.Model):

    TITULO = models.CharField("TITULO", max_length=30)
    DESCRICAO = models.CharField("DESCRICAO", max_length=100)
    CONTEUDO = models.CharField("CONTEUDO", max_length=200)
    TIPO = models.CharField("TIPO", max_length=20)
    EXTRAS = models.CharField("EXTRAS", max_length=200)
    ID_PROFESSOR = models.ForeignKey("contas.PROFESSOR",  null=True , on_delete=models.CASCADE)

class ATIVIDADE_VINCULADA(models.Model):

    ROTULO = models.CharField("ROTULO", max_length=200)
    STATUS = models.CharField("STATUS", max_length=20)
    DTINICIORESPOSTAS = models.DateField("DTINICIORESPOSTAS")
    DTFIMRESPOSTAS = models.DateField("DTFIMRESPOSTAS")

    ID_PROFESSOR = models.ForeignKey("contas.PROFESSOR",  null=True , on_delete=models.CASCADE)
    ID_ATIVIDADE = models.ForeignKey("restrito.ATIVIDADE",  null=True , on_delete=models.CASCADE)
    ID_DISCIPLINA_OFERTADA = models.ForeignKey("curriculo.DISCIPLINA_OFERTADA",  null=True , on_delete=models.CASCADE)

class ENTREGA(models.Model):

    TITULO = models.CharField("TITULO", max_length=40)
    RESPOSTA = models.CharField("RESPOSTA", max_length=100)
    DT_ENTREGA = models.DateField("DT_ENTREGA")
    STATUS = models.CharField("STATUS", max_length=20)
    NOTA = models.DecimalField("NOTA", decimal_places=2 ,max_digits=4)
    DT_AVALIACAO = models.DateField("DT_AVALIACAO")
    OBS = models.CharField("OBS", max_length=100)

    ID_PROFESSOR = models.ForeignKey("contas.PROFESSOR",  null=True , on_delete=models.CASCADE)
    ID_ALUNO = models.ForeignKey("contas.ALUNO", null=True, on_delete=models.CASCADE)
    ID_ATIVIDADE_VINCULADA = models.ForeignKey("restrito.ATIVIDADE_VINCULADA",  null=True , on_delete=models.CASCADE)

class SOLICITACAO_MATRICULA(models.Model):
    DTSOLICITACAO = models.DateField("DTSOLICITACAO")
    STATUS = models.CharField("STATUS", max_length=20)

    ID_ALUNO = models.ForeignKey("contas.ALUNO", null=True, on_delete=models.CASCADE)
    ID_DISCIPLINA_OFERTADA = models.ForeignKey("curriculo.DISCIPLINA_OFERTADA", null=True, on_delete=models.CASCADE)
    ID_COORDENADOR = models.ForeignKey("contas.COORDENADOR",  null=True , on_delete=models.CASCADE)