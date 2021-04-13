from django.db import models

# Create your models here.


class Pessoas(models.Model):
    nome = models.CharField(max_length=30)
    cidade = models.CharField(max_length=50, default='Rio de Janeiro')

    def __str__(self):
        return self.nome
