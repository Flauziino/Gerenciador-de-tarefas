import json


users = 'usuarios.json'


# Funcao para verificar se o arquivo json existe
def verifica_json(arq):
    try:
        a = open(arq, 'r')
        a.close()
    except FileNotFoundError:
        print(f'Arquivo "{arq}" nao encontrado')
        return False
    else:
        return True


# Funcao para criar o arquivo json
def cria_json(arq):
    try:
        a = open(arq, 'w')
        a.close()
    except FileNotFoundError:
        raise FileNotFoundError
    else:
        print(f'Arquivo "{arq}" criado com sucesso!!!')


# Funcao para realizar o cadastro e salvar em json
def criar_cadastro(arq, nome, senha1, senha2):
    if senha1 == senha2:
        usuario = {nome: senha1}  # Cria um dicionário para o novo usuário

        try:
            # Tenta abrir o arquivo existente
            with open(arq, 'r') as arquivo:
                lista_usuarios = json.load(arquivo)

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            # Se o arquivo não existir ou estiver vazio, inicia uma lista vazia
            lista_usuarios = []

        # Adiciona o novo usuário à lista de usuários
        lista_usuarios.append(usuario)

        try:
            a = open(arq, 'w')
            json.dump(lista_usuarios, a, ensure_ascii=False, indent=2)

        except FileNotFoundError:
            raise FileNotFoundError

        else:
            print('CADASTRO REALIZADO COM SUCESSO!!!!!')

        finally:
            a.close()


# Funcao para realizar o login
def realiza_login(arq, nome, senha):
    try:
        with open(arq, 'r') as file:
            usuarios = json.load(file)

        # For para ler os arquivos carregados do json.load
        for user in usuarios:

            # Verifica se o nome de usuário existe na lista
            if nome in user:

                # Verifica se a senha corresponde ao user
                if user[nome] == senha:
                    print('LOGIN REALIZADO COM SUCESSO')
                    # Retornando True para realizar a logica do login
                    return True
        print('ERRO DE LOGIN: ')
        print('Nome de usuario ou senha incorretos')
        # Retornando False para realizar a logica do login
        return False

    except FileNotFoundError:
        raise FileNotFoundError
