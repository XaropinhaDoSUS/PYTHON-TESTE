from django.urls import path
from .views import cadastrar_usuario, login_usuario, atualizar_usuario, deletar_usuario

urlpatterns = [
    path("cadastrar/", cadastrar_usuario),
    path("login/", login_usuario),
    path("atualizar/", atualizar_usuario),
    path("deletar/", deletar_usuario),
]