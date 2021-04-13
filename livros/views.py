from rest_framework import viewsets
from .models import Livros
from .serializers import LivrosSerializers


class LivrosViewset(viewsets.ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializers
