from rest_framework import viewsets
from .models import Farmacia
from .serializers import FarmaciaSerializers


class FarmaciaViewSet(viewsets.ModelViewSet):
    queryset = Farmacia.objects.all()
    serializer_class = FarmaciaSerializers
