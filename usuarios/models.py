from django.db import models
from django.contrib.postgres.fields import ArrayField


class Usuario(models.Model): #mapeando a tabela de usuario do banco
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
        return self.nome #No terminal do django vai aparecer o nome do usuario ao inves de object (1)

    class Meta:
        db_table = '"universidade"."usuario"' #fala para o Django usar a tabela usuario dentro do schema universidade
        managed = False #fala para o Django não tentar criar essa tabela, porque ela já existe no banco


class Estudante(models.Model): #mapeando a tabela de estudante do banco
    mat_estudante = models.CharField(max_length=7, primary_key=True) 

    #abaixo criamos um atributo de estudante chamado usuario, que representa o usuario do qual o estudante depende, e essa
    #ligação é feita pelo cpf

    usuario = models.OneToOneField( #aqui representa que é uma relação um pra um, ou seja, 1 cpf pra 1 usuario e 1 estudante
        Usuario, #aqui mostra a tabela de destino dessa ligação, q no caso é a de usuario q ta acima da de estudante
        to_field="cpf",  #aq diz qual campo de usuario ta sendo usado de referencia
        db_column="cpf", #aq diz qual coluna no banco que estamos relacionando com a de referencia
        on_delete=models.SET_NULL, #aq diz oq acontece com o estudante se o usuario for deletado, e no caso o campo de cpf vira null
        null=True, #aq diz que esse campo pode ser nulo
        blank=True #permite que deixemos em branco esse campo na h de preencher algum formulario, mas no postman isso n é mt relevante
    )

    mc = models.DecimalField(
        max_digits=2,
        decimal_places=0,
        null=True,
        blank=True
    )

    ano_ingresso = models.IntegerField(null=True, blank=True)

    def __str__(self):   
        return self.mat_estudante #No terminal do django vai aparecer a matricula do estudante

    class Meta:
        db_table = '"universidade"."estudante"' #fala para o Django usar a tabela estudante dentro do schema universidade
        managed = False #fala para o Django não tentar criar essa tabela, porque ela já existe no banco

class Curso(models.Model):
    #ta faltando criar esse model ainda

class Vinculo(models.Model):
    #tb falta criar esse model

