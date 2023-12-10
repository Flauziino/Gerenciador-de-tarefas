# Funcao para verificar se o arquivo existe
def verifica_arq(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        print(f'Arquivo "{arq}" nao encontrado')
        return False
    else:
        return True


# Funcao para criar o arquivo
def cria_arq(arq):
    try:
        a = open(arq, 'wt')
        a.close()
    except FileNotFoundError:
        print('Houve um problema.')
    else:
        print(f'Arquivo "{arq}" criado com sucesso')


# Funcao para mostrar a lista de tarefas
def ver_tarefas(arq):
    try:
        a = open(arq, 'rt')
    except FileNotFoundError:
        print('Houve um problema...')
    else:
        for linha in a:
            tarefas = linha.strip()
            print(tarefas)
    finally:
        a.close()


# Funcao para salvar a lista de tarefas
def salva_tarefas(arq, task):
    try:
        a = open(arq, 'at')
    except FileNotFoundError:
        print('Houve um problema...')
    else:
        try:
            a.write(f'{task}\n')
        except FileNotFoundError:
            print('Houve um problema tentando salvar a tarefa')
        else:
            print(f'Tarefa "{task}" salva com sucesso na lista de afazer')
    finally:
        a.close()


# Funcao para ler as tarefas em txt e retornar para uma lista.
def tarefas_lista(arq):
    try:
        a = open(arq, 'rt')
        lista_tarefas = []
        for i, v in enumerate(a):
            tarefas = v.strip()
            lista_tarefas.append(tarefas)
        return lista_tarefas
    except FileNotFoundError:
        print('Houve um problema...')
        return []
    finally:
        a.close()


# Funcao para salvar as tarefas depois te ter removido a tarefa desejada.
def salva_tarefas_2(arq, lst):
    try:
        a = open(arq, 'wt')
        a.truncate()
    except FileNotFoundError:
        print('Houve um problema...')
    else:
        try:
            for i, v in enumerate(lst):
                a.write(f'{v}\n')
        except FileNotFoundError:
            print('Houve um problema...')
        else:
            print(f'Arquivo "{arq}" atualizado com sucesso!!!')
    finally:
        a.close()


if __name__ == '__main__':
    tarefas_lista('lista_tarefas.txt')
