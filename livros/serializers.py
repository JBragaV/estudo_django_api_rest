from rest_framework import serializers
from .models import Livros


class LivrosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields = ['id', 'nome', 'tema', 'emprestado', 'pessoas']
