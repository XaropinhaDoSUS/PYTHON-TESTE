from django.db import models

class Usuario(models.Model): #criando a tabela do banco
    cpf = models.CharField(max_length=11, primary_key=True) #só é necessario colocar o key = true caso seja uma chave primaria
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField() #aqui é diferente por conta do campo
    email = models.EmailField()
    senha = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)

    login = models.CharField(max_length=50, unique=True)

    def __str__(self):   
        return self.nome #No banco de dados vai aparecer o nome do usuario ao inves de object (1)