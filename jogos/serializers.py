from rest_framework import serializers
from .models import Jogos


class JogosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jogos
        fields = ['id', 'nome',
                  'plataforma', 'emprestado',
                  'data_emprestimo', 'pessoa']
