from rest_framework import serializers
from .models import Farmacia


class FarmaciaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Farmacia
        fields = ['id', 'nome_remedio',
                  'data_validade', 'medico', 'motivo_remedio']
