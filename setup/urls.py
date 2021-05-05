from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from dispensa.views import DispensaViewSet
from compras.views import ComprasViewSet
from pessoas.views import PessoasViewset
from jogos.views import JogosViewset
from livros.views import LivrosViewset
from farmacia.views import FarmaciaViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('dispensa', DispensaViewSet, basename='dispensa')
router.register('compras', ComprasViewSet, basename='compras')
router.register('jogos', JogosViewset, basename='jogos')
router.register('livros', LivrosViewset, basename='livros')
router.register('pessoas', PessoasViewset, basename='pessoas')
router.register('farmacia', FarmaciaViewSet, basename='farmacia')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
