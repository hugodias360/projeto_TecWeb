# Generated by Django 2.0 on 2018-05-10 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CURSO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOME', models.CharField(max_length=100, verbose_name='NOME')),
            ],
        ),
        migrations.CreateModel(
            name='DISCIPLINA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOME', models.CharField(max_length=30, verbose_name='NOME')),
                ('DT_EXPIRACAO', models.DateField(verbose_name='DT_EXPIRACAO')),
                ('STATUS', models.CharField(max_length=7, verbose_name='STATUS')),
                ('PLANO_ENSINO', models.CharField(max_length=2000, verbose_name='PLANO_ENSINO')),
                ('CARGA_HORARIA', models.IntegerField(verbose_name='CARGA_HORARIA')),
                ('COMPETENCIAS', models.CharField(max_length=2000, verbose_name='COMPETENCIAS')),
                ('HABILIDADE', models.CharField(max_length=2000, verbose_name='HABILIDADE')),
                ('EMENTA', models.CharField(max_length=2000, verbose_name='EMENTA')),
                ('CONTEUDO_PROGRAMATICO', models.CharField(max_length=2000, verbose_name='CONTEUDO_PROGRAMATICO')),
                ('BIBLIOGRAFIA_BASICA', models.CharField(max_length=2000, verbose_name='BIBLIOGRAFIA_BASICA')),
                ('BIBLIOGRAFIA_COMPLEMENTAR', models.CharField(max_length=2000, verbose_name='BIBLIOGRAFIA_COMPLEMENTAR')),
                ('PERCENTUAL_PRATICO', models.IntegerField(verbose_name='PERCENTUAL_PRATICO')),
                ('PERCENTUAL_TEORICO', models.IntegerField(verbose_name='PERCENTUAL_TEORICO')),
                ('ID_COORDENADOR', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contas.COORDENADOR')),
            ],
        ),
        migrations.CreateModel(
            name='DISCIPLINA_OFERTADA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DATA_INICIO_MATRICULA', models.DateField(verbose_name='DATA_INICIO_MATRICULA')),
                ('DATA_FIM_MATRICULA', models.DateField(verbose_name='DATA_FIM_MATRICULA')),
                ('ANO', models.IntegerField(verbose_name='ANO')),
                ('SEMESTRE', models.CharField(max_length=1, verbose_name='SEMESTRE')),
                ('TURMA', models.CharField(max_length=3, verbose_name='SEMESTRE')),
                ('METODOLOGIA', models.CharField(max_length=2000, verbose_name='METODOLOGIA')),
                ('RECURSOS', models.CharField(max_length=2000, verbose_name='RECURSOS')),
                ('CRITERIO_AVALIACAO', models.CharField(max_length=2000, verbose_name='CRITERIO_AVALIACAO')),
                ('PLANO_AULAS', models.CharField(max_length=8000, verbose_name='PLANO_AULAS')),
                ('ID_COORDENADOR', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contas.COORDENADOR')),
                ('ID_CURSO', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='curriculo.CURSO')),
                ('ID_DISCIPLINA', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='curriculo.DISCIPLINA')),
                ('ID_PROFESSOR', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contas.PROFESSOR')),
            ],
        ),
    ]
