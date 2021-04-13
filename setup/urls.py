from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from dispensa.views import DispensaViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('dispensa', DispensaViewSet, basename='dispensa')
router.register('lista_compras', DispensaViewSet, basename='lista')
router.register('jogos', DispensaViewSet, basename='jogos')
router.register('livros', DispensaViewSet, basename='livros')
router.register('pessoas', DispensaViewSet, basename='pessoas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
