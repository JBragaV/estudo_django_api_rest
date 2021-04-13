from rest_framework import viewsets
from .models import Jogos
from .serializers import JogosSerializers


class JogosViewset(viewsets.ModelViewSet):
    queryset = Jogos.objects.all()
    serializer_class = JogosSerializers
