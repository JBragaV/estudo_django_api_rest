from django.db import models
from pessoas.models import Pessoas


class Jogos(models.Model):
    nome = models.CharField(max_length=20)
    plataforma = models.CharField(max_length=15)
    emprestado = models.BooleanField(default=False)
    data_emprestimo = models.DateTimeField(null=True)
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE,
                               null=True, blank=True)

    def __str__(self):
        return self.nome
