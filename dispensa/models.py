from django.db import models

# Create your models here.


class Dispensa(models.Model):
    nome_produto = models.CharField(max_length=30, default='Produto sem nome')
    quantidade = models.CharField(default="0", max_length=30)

    def __str__(self):
        return self.nome_produto
