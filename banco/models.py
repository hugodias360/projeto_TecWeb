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

class ATIVIDADE (models.Model):

    TITULO = models.CharField("TITULO", max_length=30)
    DESCRICAO = models.CharField("DESCRICAO", max_length=100)
    CONTEUDO = models.CharField("CONTEUDO", max_length=200)
    TIPO = models.CharField("TIPO", max_length=20)
    EXTRAS = models.CharField("EXTRAS", max_length=200)
    ID_PROFESSOR = models.ForeignKey(PROFESSOR,  null=True , on_delete=models.CASCADE)

class DISCIPLINA(models.Model):
    NOME = models.CharField("NOME", max_length=30)
    DT_EXPIRACAO = models.DateField("DT_EXPIRACAO")
    STATUS = models.CharField("STATUS", max_length=7)
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
    ID_COORDENADOR = models.ForeignKey(COORDENADOR,  null=True , on_delete=models.CASCADE)

class CURSO(models.Model):
    NOME = models.CharField("NOME", max_length=100)

class DISCIPLINA_OFERTADA(models.Model):
    DATA_INICIO_MATRICULA = models.DateField("DATA_INICIO_MATRICULA")
    DATA_FIM_MATRICULA = models.DateField("DATA_FIM_MATRICULA")
    ANO = models.IntegerField("ANO")
    SEMESTRE = models.CharField ("SEMESTRE", max_length=1)
    TURMA = models.CharField ("SEMESTRE", max_length=3)
    METODOLOGIA = models.CharField("METODOLOGIA",max_length=2000)
    RECURSOS = models.CharField("RECURSOS",max_length=2000)
    CRITERIO_AVALIACAO = models.CharField("CRITERIO_AVALIACAO",max_length=2000)
    PLANO_AULAS = models.CharField("PLANO_AULAS",max_length=8000)

    ID_PROFESSOR = models.ForeignKey(PROFESSOR,  null=True , on_delete=models.CASCADE)
    ID_CURSO = models.ForeignKey(CURSO,  null=True , on_delete=models.CASCADE)
    ID_DISCIPLINA = models.ForeignKey(DISCIPLINA,  null=True , on_delete=models.CASCADE)
    # N para N ou 1 para N?
    ID_COORDENADOR = models.ForeignKey(COORDENADOR,  null=True , on_delete=models.CASCADE)

class SOLICITACAO_MATRICULA(models.Model):
    DTSOLICITACAO = models.DateField("DTSOLICITACAO")
    STATUS = models.CharField("STATUS", max_length=20)

    ID_ALUNO = models.ForeignKey(ALUNO, null=True, on_delete=models.CASCADE)
    ID_DISCIPLINA_OFERTADA = models.ForeignKey(DISCIPLINA_OFERTADA, null=True, on_delete=models.CASCADE)
    ID_COORDENADOR = models.ForeignKey(COORDENADOR,  null=True , on_delete=models.CASCADE)

class ATIVIDADE_VINCULADA(models.Model):

    ROTULO = models.CharField("ROTULO", max_length=200)
    STATUS = models.CharField("STATUS", max_length=20)
    DTINICIORESPOSTAS = models.DateField("DTINICIORESPOSTAS")
    DTFIMRESPOSTAS = models.DateField("DTFIMRESPOSTAS")

    ID_PROFESSOR = models.ForeignKey(PROFESSOR,  null=True , on_delete=models.CASCADE)
    ID_ATIVIDADE = models.ForeignKey(ATIVIDADE,  null=True , on_delete=models.CASCADE)
    ID_DISCIPLINA_OFERTADA = models.ForeignKey(DISCIPLINA_OFERTADA,  null=True , on_delete=models.CASCADE)

class ENTREGA(models.Model):

    TITULO = models.CharField("TITULO", max_length=40)
    RESPOSTA = models.CharField("RESPOSTA", max_length=100)
    DT_ENTREGA = models.DateField("DT_ENTREGA")
    STATUS = models.CharField("STATUS", max_length=20)
    NOTA = models.DecimalField("NOTA", decimal_places=2 ,max_digits=4)
    DT_AVALIACAO = models.DateField("DT_AVALIACAO")
    OBS = models.CharField("OBS", max_length=100)

    ID_PROFESSOR = models.ForeignKey(PROFESSOR,  null=True , on_delete=models.CASCADE)
    ID_ALUNO = models.ForeignKey(ALUNO, null=True, on_delete=models.CASCADE)
    ID_ATIVIDADE_VINCULADA = models.ForeignKey(ATIVIDADE_VINCULADA,  null=True , on_delete=models.CASCADE)

class MENSAGEM(models.Model):
    ASSUNTO = models.CharField("ASSUNTO", max_length=300)
    REFERENCIA = models.CharField("REFERENCIA", max_length=300)
    CONTEUDO = models.CharField("CONTEUDO", max_length=400)
    STATUS = models.CharField("STATUS", max_length=20)
    DT_ENVIO = models.DateField("DT_ENVIO")
    DT_RESPOSTA = models.DateField("DT_RESPOSTA")
    RESPOSTA = models.CharField("RESPOSTA", max_length=400)


    ID_PROFESSOR = models.ManyToManyField(PROFESSOR)
    ID_ALUNO = models.ManyToManyField(ALUNO)