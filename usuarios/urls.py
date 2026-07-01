from django.urls import path
from .views import cadastrar_usuario, atualizar_usuario, deletar_usuario

urlpatterns = [
    path("cadastrar/", cadastrar_usuario),
    path("atualizar/", atualizar_usuario),
    path("deletar/", deletar_usuario),
]