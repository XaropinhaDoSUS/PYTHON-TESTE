from django.http import JsonResponse #Faz com que as respostas saiam em json
from django.views.decorators.csrf import csrf_exempt 
from .models import Usuario
import json


@csrf_exempt
def cadastrar_usuario(request):
    # Verifica se o método usado é POST
    if request.method == "POST":

        # Pega os dados enviados no corpo da requisição
        dados = json.loads(request.body)

        # Verifica se já existe um usuário com esse CPF
        usuario_existente = Usuario.objects.filter(cpf=dados["cpf"]).first()

        if usuario_existente:
            return JsonResponse({
                "erro": "Já existe um usuário com esse CPF"
            }, status=400)

        # Verifica se já existe um usuário com esse login
        login_existente = Usuario.objects.filter(login=dados["login"]).first()

        if login_existente:
            return JsonResponse({
                "erro": "Já existe um usuário com esse login"
            }, status=400)

        # Cria o usuário no banco
        usuario = Usuario.objects.create(
            cpf=dados["cpf"],
            nome=dados["nome"],
            data_nascimento=dados["data_nascimento"],
            email=dados["email"],
            senha=dados["senha"],
            telefone=dados["telefone"],
            login=dados["login"]
        )

        # Retorna resposta de sucesso
        return JsonResponse({
            "mensagem": "Usuário cadastrado com sucesso",
            "usuario": {
                "cpf": str(usuario.cpf),
                "nome": usuario.nome,
                "email": usuario.email,
                "telefone": usuario.telefone,
                "login": usuario.login
            }
        }, status=201)

    # Se não for POST, retorna erro
    return JsonResponse({
        "erro": "Método não permitido"
    }, status=405)



#Metodo POST
@csrf_exempt #serve pra testar rota no json sem bloqueios
def login_usuario(request): #Criando função de login
    if request.method == "POST":
        dados = json.loads(request.body) #enviando dados em json
        login = dados["login"]
        senha = dados["senha"]

        usuario = Usuario.objects.filter(login=login, senha=senha).first() #procura os dados na tabela de objetos 

        if usuario:
            request.session["usuario_cpf"] = str(usuario.cpf) #guarda o cpf do usuario

            return JsonResponse({
                "mensagem": "Login realizado com sucesso",
                "usuario": usuario.nome
            })
        else:
            return JsonResponse({"erro": "Login ou senha inválidos"}, status=401)

    return JsonResponse({"erro": "Método não permitido"}, status=405)



#Metodo PUT 
@csrf_exempt
def atualizar_usuario(request):
    if "usuario_cpf" not in request.session:
        return JsonResponse({"erro": "Você precisa estar logado"}, status=401) #se o cpf n estiver na sessão, o usuario precisa realizar login
       
    if request.method == "PUT": #Verifica se o metodo de atualizar esta sendo utilizado
        dados = json.loads(request.body)

        cpf_logado = request.session["usuario_cpf"]
        usuario = Usuario.objects.filter(cpf=cpf_logado).first() #procura o usuario com o cpf do login, para ele editar ESTE usuario

        if usuario is None:
            return JsonResponse({"erro": "Usuário não encontrado"}, status=404)

        # Atualiza apenas os campos enviados
        usuario.nome = dados.get("nome", usuario.nome)
        usuario.email = dados.get("email", usuario.email)
        usuario.telefone = dados.get("telefone", usuario.telefone)
        usuario.senha = dados.get("senha", usuario.senha)
        usuario.login = dados.get("login", usuario.login)

        # Salva as alterações no banco
        usuario.save()

        return JsonResponse({
            "mensagem": "Usuário atualizado com sucesso",
            "usuario": {
                "cpf": str(usuario.cpf),
                "nome": usuario.nome,
                "email": usuario.email,
                "telefone": usuario.telefone,
                "login": usuario.login
            }
        })

    return JsonResponse({"erro": "Método não permitido"}, status=405)



# deletar
@csrf_exempt
def deletar_usuario(request):
    #verificação
    if "usuario_cpf" not in request.session:
        return JsonResponse({"erro": "Você precisa estar logado"}, status=401)

    if request.method == "DELETE":
        cpf_logado = request.session["usuario_cpf"] #requisição delete

        usuario = Usuario.objects.filter(cpf=cpf_logado).first() #assim como o atualizar só é possivel deletar pelo cpf logado

        if usuario is None: 
            return JsonResponse({"erro": "Usuário não encontrado"}, status=404) #caso o usuario não seja encontrado 

        usuario.delete()
        request.session.flush()

        return JsonResponse({
            "mensagem": "Usuário deletado com sucesso" #se a condição estiver correta, o usuario é deletado 
        })

    return JsonResponse({"erro": "Método não permitido"}, status=405)



# ==========================
# CAMINHOS PARA TESTAR NO POSTMAN
# ==========================

# CADASTRAR USUÁRIO
# Método: POST
# URL: http://127.0.0.1:8000/usuarios/cadastrar/
# Body > raw > JSON
# Serve para cadastrar um novo usuário no banco.

# LOGIN DO USUÁRIO
# Método: POST
# URL: http://127.0.0.1:8000/usuarios/login/
# Body > raw > JSON
# Serve para fazer login e salvar o CPF do usuário na sessão.

# ATUALIZAR USUÁRIO LOGADO
# Método: PUT
# URL: http://127.0.0.1:8000/usuarios/atualizar/
# Body > raw > JSON
# Serve para atualizar os dados do usuário que está logado.

# DELETAR USUÁRIO LOGADO
# Método: DELETE
# URL: http://127.0.0.1:8000/usuarios/deletar/
# Não precisa mandar body.
# Serve para deletar o usuário que está logado.

# OBSERVAÇÃO IMPORTANTE:
# Para testar atualizar e deletar, primeiro precisa fazer login no Postman.
# Depois do login, use a mesma aba ou mantenha os cookies/sessão do Postman.
# ==========================
# CAMINHOS PARA TESTAR NO POSTMAN
# ==========================

# CADASTRAR USUÁRIO
# Método: POST
# URL: http://127.0.0.1:8000/usuarios/cadastrar/
# Body > raw > JSON
# Serve para cadastrar um novo usuário no banco.

# LOGIN DO USUÁRIO
# Método: POST
# URL: http://127.0.0.1:8000/usuarios/login/
# Body > raw > JSON
# Serve para fazer login e salvar o CPF do usuário na sessão.

# ATUALIZAR USUÁRIO LOGADO
# Método: PUT
# URL: http://127.0.0.1:8000/usuarios/atualizar/
# Body > raw > JSON
# Serve para atualizar os dados do usuário que está logado.

# DELETAR USUÁRIO LOGADO
# Método: DELETE
# URL: http://127.0.0.1:8000/usuarios/deletar/
# Não precisa mandar body.
# Serve para deletar o usuário que está logado.

# OBSERVAÇÃO IMPORTANTE:
# Para testar atualizar e deletar, primeiro precisa fazer login no Postman.
# Depois do login, use a mesma aba ou mantenha os cookies/sessão do Postman.