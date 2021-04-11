from rest_framework import serializers
from .models import Dispensa


class DispensaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dispensa
        fields = ['id', 'nome_produto', 'quantidade']
