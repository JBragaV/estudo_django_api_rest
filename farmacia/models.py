from django.db import models
# Fazer o desenho do modelo da farmácia
# Create your models here.


class Farmacia(models.Model):
    nome_remedio = models.CharField(max_length=50)
    data_validade = models.DateField()
    medico = models.CharField(max_length=50)
    motivo_remedio = models.TextField()

    def __str__(self):
        return self.nome_remedio
