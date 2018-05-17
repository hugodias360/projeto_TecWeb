from django.db import models

class DISCIPLINA(models.Model):
    NOME = models.CharField("NOME", max_length=30)
    DT_EXPIRACAO = models.DateField("DT_EXPIRACAO", null=True)
    STATUS = models.CharField("STATUS", max_length=7,null=True)
    PLANO_ENSINO = models.CharField("PLANO_ENSINO",max_length=2000)
    CARGA_HORARIA = models.IntegerField("CARGA_HORARIA")
    COMPETENCIAS = models.CharField("COMPETENCIAS",max_length=2000)
    HABILIDADE = models.CharField("HABILIDADE",max_length=2000)
    EMENTA = models.CharField("EMENTA",max_length=2000)
    CONTEUDO_PROGRAMATICO = models.CharField("CONTEUDO_PROGRAMATICO",max_length=2000)
    BIBLIOGRAFIA_BASICA = models.CharField("BIBLIOGRAFIA_BASICA",max_length=2000)
    BIBLIOGRAFIA_COMPLEMENTAR = models.CharField("BIBLIOGRAFIA_COMPLEMENTAR",max_length=2000)
    PERCENTUAL_PRATICO = models.IntegerField("PERCENTUAL_PRATICO")
    PERCENTUAL_TEORICO = models.IntegerField("PERCENTUAL_TEORICO")
    ID_COORDENADOR = models.ForeignKey("contas.COORDENADOR",  null=True , on_delete=models.CASCADE)

class CURSO(models.Model):
    NOME = models.CharField("NOME", max_length=100)

class DISCIPLINA_OFERTADA(models.Model):
    DATA_INICIO_MATRICULA = models.DateField("DATA_INICIO_MATRICULA",null=True)
    DATA_FIM_MATRICULA = models.DateField("DATA_FIM_MATRICULA",null=True)
    ANO = models.IntegerField("ANO",null=True)
    SEMESTRE = models.CharField ("SEMESTRE", max_length=1,null=True)
    TURMA = models.CharField ("TURMA", max_length=3,null=True)
    METODOLOGIA = models.CharField("METODOLOGIA",max_length=2000,null=True)
    RECURSOS = models.CharField("RECURSOS",max_length=2000,null=True)
    CRITERIO_AVALIACAO = models.CharField("CRITERIO_AVALIACAO",max_length=2000,null=True)
    PLANO_AULAS = models.CharField("PLANO_AULAS",max_length=8000,null=True)

    ID_PROFESSOR = models.ForeignKey("contas.PROFESSOR",  null=True , on_delete=models.CASCADE)
    ID_CURSO = models.ForeignKey("curriculo.CURSO",  null=True , on_delete=models.CASCADE)
    ID_DISCIPLINA = models.ForeignKey("curriculo.DISCIPLINA",  null=True , on_delete=models.CASCADE)
    # N para N ou 1 para N?
    ID_COORDENADOR = models.ForeignKey("contas.COORDENADOR",  null=True , on_delete=models.CASCADE)
