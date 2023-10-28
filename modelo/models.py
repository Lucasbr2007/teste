from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    contato = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    