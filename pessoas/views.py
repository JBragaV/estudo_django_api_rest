from rest_framework import viewsets
from .models import Pessoas
from .serializers import PessoasSerializers


class PessoasViewset(viewsets.ModelViewSet):
    queryset = Pessoas.objects.all()
    serializer_class = PessoasSerializers
