# Generated by Django 2.0.3 on 2018-05-02 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0005_auto_20180501_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensagem',
            name='ID_ALUNO',
            field=models.ManyToManyField(to='banco.ALUNO'),
        ),
        migrations.AlterField(
            model_name='mensagem',
            name='ID_PROFESSOR',
            field=models.ManyToManyField(to='banco.PROFESSOR'),
        ),
    ]