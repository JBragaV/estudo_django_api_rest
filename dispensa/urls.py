from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('dispensa/', DispensaList.as_view()),
    path('dispensa/<int:id>', DispensaDetalhes.as_view())
]
