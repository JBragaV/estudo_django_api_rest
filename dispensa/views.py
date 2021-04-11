from django.http import JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import DispensaSerializers, Dispensa


def resposta_servidor(mensagem='Ocorreu um erro interno no servidor',
                      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR):
    return JsonResponse({'mensgem': mensagem}, status=status_code)


class DispensaList(APIView):

    def get(self, request):
        try:
            lista_dispensa = Dispensa.objects.all()
            dispensa_serializer = DispensaSerializers(lista_dispensa, many=True)
            return Response(dispensa_serializer.data)
        except Exception:
            return resposta_servidor()

    def post(self, request):
        try:
            produto = DispensaSerializers(data=request.data)
            if produto.is_valid():
                produto.save()
                return Response(produto.data, status=status.HTTP_201_CREATED)
            return Response(produto.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return resposta_servidor()


class DispensaDetalhes(APIView):

    def get(self, request, id):
        try:
            if id <= 0:
                return JsonResponse({'mensagem': 'Id inválido!!!'})
            dispensa = Dispensa.objects.get(pk=id)
            dispensa_serializer = DispensaSerializers(dispensa)
            return Response(dispensa_serializer.data)
        except Dispensa.DoesNotExist:
            return resposta_servidor('O produto não exite',
                                     status.HTTP_404_NOT_FOUND)
        except Exception:
            return resposta_servidor()

    def put(self, request, id):
        try:
            if id <= 0:
                return resposta_servidor('Id inválido!!!')
            produto = Dispensa.objects.get(pk=id)
            serializer = DispensaSerializers(produto, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        except produto.DoesNotExist:
            return resposta_servidor("Produto não encontrado no servidor",
                                     status.HTTP_404_NOT_FOUND)
        except Exception:
            return resposta_servidor()

    def delete(self, request, id):
        try:
            if id <= 0:
                return resposta_servidor('Id invlálido!!!',
                                         status.HTTP_400_BAD_REQUEST)

            print('Função Delete!!!')
            produto = Dispensa.objects.get(pk=id)
            produto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Dispensa.DoesNotExist:
            return resposta_servidor('Produto não encontrado!!!',
                                     status.HTTP_404_NOT_FOUND)
        except Exception:
            return resposta_servidor()
