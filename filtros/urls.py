from django.urls import path

from filtros.views.filtrando import *

urlpatterns = [
    path('', lista_tabelas, name= 'lista_tabelas'),
]