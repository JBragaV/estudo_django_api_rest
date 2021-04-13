from datetime import datetime
from django.db import models


class Compras(models.Model):
    produto = models.CharField(max_length=20)
    quantidade = models.CharField(max_length=20)
    data_incercao = models.DateTimeField(default=datetime.now())
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.produto
