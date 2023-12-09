from time import sleep
from menu import menu
from arquivos import arquivos


# Logica princiapal
arq = 'lista_tarefas.txt'
if not arquivos.verifica_arq(arq):
    arquivos.cria_arq(arq)
MN = ['1. Ver tarefas cadastradas',
      '2. Cadastrar novas tarefas',
      '3. Remover uma tarefa da lista',
      '4. Marcar uma tarefa como concluida',
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
                lista_de_tarefas = arquivos.tarefas_lista(arq)

                for i, v in enumerate(lista_de_tarefas):
                    print(f'Indice: {i}  Tarefa: {v}')

                while True:
                    try:
                        task = menu.lerint('Qual terefa deseja remover da'
                                           'lista?')
                        if task in range(len(lista_de_tarefas)):
                            del lista_de_tarefas[task]
                            break
                    except KeyboardInterrupt:
                        raise KeyboardInterrupt
                    else:
                        print('A lista nao contem esse indice,'
                              'tente novamente')
                choice = input('Deseja continuar? [S/N] ')

                if choice in 'Nn':
                    break

            arquivos.salva_tarefas(arq, lista_de_tarefas)
        elif choice == 4:
            ...

        elif choice == 5:
            menu.titulos('FINALIZANDO...')
            sleep(1)
            sistema_on = False

        elif choice not in range(1, 4):
            print('Digite uma opção valida!!!')
            sleep(0.5)

    except KeyboardInterrupt:
        sistema_on = False

menu.titulos('VOLTE SEMPRE!!')
