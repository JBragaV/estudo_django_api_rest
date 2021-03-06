from rest_framework import serializers
from .models import Compras


class ComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compras
        fields = ['id', 'produto', 'quantidade', 'data_incercao']
