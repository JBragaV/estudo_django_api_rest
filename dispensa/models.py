from django.db import models
from pessoas.models import Pessoas
# Create your models here.


class Dispensa(models.Model):
    nome_produto = models.CharField(max_length=30, default='Produto sem nome')
    quantidade = models.CharField(default="0", max_length=30)
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome_produto
