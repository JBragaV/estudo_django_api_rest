from django.db import models
from pessoas.models import Pessoas


class Livros(models.Model):
    nome = models.CharField(max_length=30)
    tema = models.CharField(max_length=20)
    emprestado = models.BooleanField(default=False)
    pessoas = models.ForeignKey(Pessoas, on_delete=models.CASCADE,
                                null=True, blank=True)

    def __str__(self):
        return self.nome
