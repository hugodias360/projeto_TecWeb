# Generated by Django 2.0.3 on 2018-05-02 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0002_atividade_id_professor'),
    ]

    operations = [
        migrations.CreateModel(
            name='ALUNO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LOGIN', models.CharField(max_length=100, verbose_name='LOGIN')),
                ('SENHA', models.CharField(max_length=30, verbose_name='SENHA')),
                ('NOME', models.CharField(max_length=100, verbose_name='NOME')),
                ('EMAIL', models.EmailField(max_length=200, verbose_name='EMAIL')),
                ('CELULAR', models.IntegerField(verbose_name='CELULAR')),
                ('DT_EXPIRACAO', models.DateField(verbose_name='DT_EXPIRACAO')),
                ('RA', models.IntegerField(verbose_name='RA')),
            ],
        ),
        migrations.CreateModel(
            name='COORDENADOR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LOGIN', models.CharField(max_length=100, verbose_name='LOGIN')),
                ('SENHA', models.CharField(max_length=30, verbose_name='SENHA')),
                ('NOME', models.CharField(max_length=30, verbose_name='NOME')),
                ('EMAIL', models.EmailField(max_length=200, verbose_name='EMAIL')),
                ('CELULAR', models.IntegerField(verbose_name='CELULAR')),
                ('DT_EXPIRACAO', models.DateField(max_length=100, verbose_name='DT_EXPIRACAO')),
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
            ],
        ),
    ]
