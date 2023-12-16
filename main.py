import os
from time import sleep
from cadastros import cadastro
from menu import menu
from arquivos import arquivos


# Logica principal
arq = 'lista_tarefas.txt'
users = 'usuarios.json'
if not cadastro.verifica_json(users):
    cadastro.cria_json(users)

if not arquivos.verifica_arq(arq):
    arquivos.cria_arq(arq)

# Menu das tarefas, so chega nele caso login seja efetuado
MN = [
    '1. Ver tarefas cadastradas',
    '2. Cadastrar novas tarefas',
    '3. Remover uma tarefa da lista',
    '4. Atualizar uma tarefa da lista',
    '5. Voltar para o menu de login'
    ]

# Menu primario
MN_2 = [
    '[1] Para realizar Cadastro',
    '[2] Para realizar Login',
    '[3] Para sair.'
]

sistema = True  # Sistema principal
while sistema:
    menu.titulos('MENU DE LOGIN')
    menu.menu(MN_2)
    escolha = menu.lerint('O que deseja? ')

    if escolha == 1:
        menu.titulos('REALIZANDO NOVO CADASTRO')
        nome = input('Digite seu nome: ')

        while True:
            senha = input('Digite sua senha: ')
            senha_2 = input('Confirme sua senha: ')

            if senha == senha_2:
                break

            else:
                print('A senha 1 é diferente da senha 2')
        cadastro.criar_cadastro(users, nome, senha, senha_2)

    elif escolha == 2:
        menu.titulos('REALIZANDO LOGIN')
        nome = input('Nome: ')
        senha = input('Senha: ')

        if cadastro.realiza_login(users, nome, senha):
            sistema_on = True
            while sistema_on:
                try:
                    menu.titulos('MENU PRINCIPAL')
                    menu.menu(MN)
                    choice = menu.lerint('Escolha uma opção > ')

                    if choice == 1:
                        menu.titulos('LISTA DE TAREFAS CADASTRADAS')
                        arquivos.ver_tarefas(arq)

                    elif choice == 2:
                        menu.titulos('CADASTRE NOVAS TAREFAS')
                        task = input('Qual tarefa deseja cadastrar? ')
                        arquivos.salva_tarefas(arq, task)

                    elif choice == 3:
                        while True:
                            menu.titulos('DELETAR UMA TAREFA')
                            lista_de_tarefas = arquivos.tarefas_lista(arq)

                            for i, v in enumerate(lista_de_tarefas):
                                print(f'Indice: {i}  Tarefa: {v}')
                            menu.linhas()

                            while True:
                                try:
                                    task = menu.lerint(
                                        'Qual terefa deseja remover da lista? '
                                                    )
                                    if task in range(len(lista_de_tarefas)):
                                        del lista_de_tarefas[task]
                                        break

                                except KeyboardInterrupt:
                                    raise KeyboardInterrupt

                                else:
                                    print(
                                        'A lista nao contem esse indice,'
                                        'tente novamente'
                                        )
                            break

                        arquivos.salva_tarefas_2(arq, lista_de_tarefas)

                    elif choice == 4:
                        while True:

                            menu.titulos('ATUALIZAR UMA TAREFA')
                            tarefas_para_atualizar = arquivos.tarefas_lista(arq)

                            for i, v in enumerate(tarefas_para_atualizar):
                                print(f'Indice: {i}   Tarefa: {v}')
                            menu.linhas()

                            while True:
                                try:
                                    task = menu.lerint(
                                        'Qual tarefa deseja atualizar? '
                                        )

                                    if task in range(
                                        len(tarefas_para_atualizar)
                                         ):
                                        nova_tarefa = input(
                                            'Qual a nova tarefa? '
                                            )
                                        tarefas_para_atualizar[task] = nova_tarefa
                                        break

                                except KeyboardInterrupt:
                                    raise KeyboardInterrupt

                                else:
                                    print(
                                        'Nao existe esse indice'
                                        ' na sua lista de tarefas,'
                                        'tente novamente'
                                        )
                            break

                        arquivos.salva_tarefas_2(arq, tarefas_para_atualizar)

                    elif choice == 5:
                        menu.titulos('RETORNANDO PARA MENU DE LOGIN')
                        sleep(1)
                        sistema_on = False

                    elif choice not in range(1, 5):
                        print('Digite uma opção valida!!!')
                        sleep(0.5)

                except KeyboardInterrupt:
                    sistema_on = False

    elif escolha not in range(1, 4):
        print('Opçao invalida, tente novamente')

    elif escolha == 3:
        menu.titulos('FINALIZANDO')
        sistema = False

os.system('cls')
menu.titulos('VOLTE SEMPRE!!')
