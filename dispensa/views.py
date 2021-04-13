from rest_framework import viewsets

from .models import Dispensa
from .serializers import DispensaSerializers


class DispensaViewSet(viewsets.ModelViewSet):
    queryset = Dispensa.objects.all()
    serializer_class = DispensaSerializers

