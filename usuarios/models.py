from django.db import models
from django.contrib.postgres.fields import ArrayField


class Usuario(models.Model): #criando a tabela do banco
    cpf = models.DecimalField(max_digits=13, decimal_places=0, primary_key=True) #só é necessario colocar o key = true caso seja uma chave primaria
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True) #aqui é diferente por conta do campo

    email = ArrayField(
        models.CharField(max_length=100),
        null=True,
        blank=True
    ) #no banco está como VARCHAR[], por isso aqui vira uma lista

    senha = models.CharField(max_length=32)

    telefone = ArrayField(
        models.CharField(max_length=20),
        null=True,
        blank=True
    ) 

    login = models.CharField(max_length=45, unique=True)

    def __str__(self):   
        return self.nome #No banco de dados vai aparecer o nome do usuario ao inves de object (1)

    class Meta:
        db_table = '"universidade"."usuario"' #fala para o Django usar a tabela usuario dentro do schema universidade
        managed = False #fala para o Django não tentar criar essa tabela, porque ela já existe no banco