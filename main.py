from time import sleep
from menu import menu
from arquivos import arquivos
import os


# Logica principal
arq = 'lista_tarefas.txt'

if not arquivos.verifica_arq(arq):
    arquivos.cria_arq(arq)

MN = [
    '1. Ver tarefas cadastradas',
    '2. Cadastrar novas tarefas',
    '3. Remover uma tarefa da lista',
    '4. Atualizar uma tarefa da lista',
    '5. Finalizar o gerenciador de tarefas'
    ]

sistema_on = True
while sistema_on:
    try:
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
                        task = menu.lerint('Qual terefa deseja remover da'
                                           'lista? ')
                        if task in range(len(lista_de_tarefas)):
                            del lista_de_tarefas[task]
                            break

                    except KeyboardInterrupt:
                        raise KeyboardInterrupt

                    else:
                        print('A lista nao contem esse indice,'
                              'tente novamente')
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
                        task = menu.lerint('Qual tarefa deseja atualizar? ')

                        if task in range(len(tarefas_para_atualizar)):
                            nova_tarefa = input('Qual a nova tarefa? ')
                            tarefas_para_atualizar[task] = nova_tarefa
                            break

                    except KeyboardInterrupt:
                        raise KeyboardInterrupt

                    else:
                        print('Nao existe esse indice na sua lista de tarefas,'
                              'tente novamente')
                break

            arquivos.salva_tarefas_2(arq, tarefas_para_atualizar)

        elif choice == 5:
            menu.titulos('FINALIZANDO...')
            sleep(1)
            sistema_on = False

        elif choice not in range(1, 4):
            print('Digite uma opção valida!!!')
            sleep(0.5)

    except KeyboardInterrupt:
        sistema_on = False

os.system('cls')
menu.titulos('VOLTE SEMPRE!!')
