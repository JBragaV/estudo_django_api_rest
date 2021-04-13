from rest_framework import serializers
from .models import Pessoas


class PessoasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pessoas
        fields = ['id', 'nome', 'cidade']
