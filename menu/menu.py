from time import sleep


# Funcao para linhas
def linhas(tam=60):
    print('-'*tam)


# Funcao rapida para titulos
def titulos(msg):
    linhas()
    print(f'{msg.center(60)}')
    linhas()


# Funcao para o menu principal (recebe lista de opcoes)
def menu(lst):
    for k, v in enumerate(lst):
        print(f'    {v}')
    linhas()


# Funcao para validar apenas numeros inteiros.
def lerint(msg):
    while True:
        try:
            n = input(msg)
            if n.isnumeric():
                num = int(n)
                return num
        except KeyboardInterrupt:
            print('Usuario preferiu interromper o programa')
            sleep(1)
            raise KeyboardInterrupt
        else:
            print('ERROR!!! Por favor, digite um numero inteiro!')
            sleep(0.5)


if __name__ == '__main__':
    # Lista de opcoes do menu
    MN_TEST = [
        '1. Ver tarefas',
        '2. Cadastrar novas tarefas',
        '3. Remover uma tarefa/ Marcar como confluida',
        '4. Finalizar o gerenciador'
    ]

    menu(MN_TEST)
