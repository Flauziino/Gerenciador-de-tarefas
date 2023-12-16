import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import sys
from arquivos import arquivos
import os


class TestArquivos(unittest.TestCase):

    def setUp(self):
        # Criar arquivos de teste
        with open('lista_tarefas.txt', 'w') as file:
            file.write('Testeeee')

    def tearDown(self):
        # Deleta os asquivos criados para teste
        os.remove('lista_tarefas.txt')

    def test_verifica_arq_existente(self):
        # Teste para verificar se o arquivo existe
        resultado = arquivos.verifica_arq('lista_tarefas.txt')
        self.assertTrue(resultado)

    def test_verifica_arq_inexistente(self):
        # Teste para verificar se o arquivo NAO existe
        resultado = arquivos.verifica_arq('lista_tarefas_2.txt')
        self.assertFalse(resultado)

    def test_cria_arq(self):
        # Teste para criar um arquivo
        arquivos.cria_arq('arquivo_novo.txt')
        resultado = arquivos.verifica_arq('arquivo_novo.txt')
        self.assertTrue(resultado)

    def test_ver_tarefas(self):
        # Simula as linhas do arquivo
        lines = ['Tarefa1\n', 'Tarefa2\n']

        # Redireciona a saída para um buffer StringIO
        captured_output = StringIO()  # fez isso para rastrear o PRINT interno
        sys.stdout = captured_output  # da funcao

        # Chama a função que deveria imprimir as linhas do arquivo
        with patch(
            'builtins.open',
             mock_open(
                 read_data=''.join(lines)
                )
             ):
            arquivos.ver_tarefas('arquivo_novo.txt')

        # Restaura a saída padrão
        sys.stdout = sys.__stdout__

        # Obtém o conteúdo do buffer (o que foi impresso)
        printed_content = captured_output.getvalue()

        # Verifica se as linhas do arquivo foram corretamente impressas
        self.assertEqual(printed_content, 'Tarefa1\nTarefa2\n')

    # Teste para verificar se a função salva uma tarefa corretamente
    def test_salva_tarefa(self):
        # Chame a função que você está testando
        task = 'Fazer compras'
        nome_arquivo = 'arquivo_novo.txt'
        arquivos.salva_tarefas(nome_arquivo, task)

        # Verifique se o arquivo foi criado e a tarefa foi salva corretamente
        self.assertTrue(os.path.exists(nome_arquivo))  # Verifica se o
        with open(nome_arquivo, 'r') as file:          # arquivo existe
            conteudo = file.read()
            # Verifica se a tarefa está no conteúdo do arquivo
            self.assertIn(task, conteudo)

    # Teste para verificar se a função lida corretamente com a escrita no arq
    def test_escrita_no_arquivo(self):
        # Simula um erro durante a escrita no arquivo
        with unittest.mock.patch(
            'builtins.open',
            side_effect=Exception(
                'Erro ao escrever'
                                  )
                                ):
            with self.assertRaises(Exception):
                arquivos.salva_tarefas(self.nome_arquivo, 'Tarefa com erro')

    # Teste para verificar se a função lê corretamente as tarefas do arquivo
    def test_tarefas_lista(self):
        nome_arquivo = 'arquivo_novo_2.txt'
        # Chame a função que você está testando
        lista_tarefas = arquivos.tarefas_lista(nome_arquivo)

        # Verifique se a lista retornada contém as tarefas esperadas
        self.assertEqual(lista_tarefas, [
            'Tarefa 1', 'Tarefa 2', 'Tarefa 3'
            ])

    # Teste para verificar se a função remove e salva
    # corretamente a tarefa desejada
    def test_salva_tarefas_2(self):
        # Chame a função que você está testando
        nome_arquivo = 'arquivo_novo_3.txt'
        tarefas = ['Tarefa 1', 'Tarefa 3']  # Lista sem a 'Tarefa 2'
        arquivos.salva_tarefas_2(nome_arquivo, tarefas)

        # Verifique se a tarefa foi removida corretamente
        with open(nome_arquivo, 'r') as file:
            conteudo = file.read()
            # Verifica se a 'Tarefa 2' não está no conteúdo do arquivo
            self.assertNotIn('Tarefa 2', conteudo)

        # Verifique se as outras tarefas foram salvas corretamente
        with open(nome_arquivo, 'r') as file:
            conteudo_atualizado = file.read()
            # Verifica se a 'Tarefa 1' está no conteúdo do arquivo
            self.assertIn('Tarefa 1', conteudo_atualizado)
            # Verifica se a 'Tarefa 3' está no conteúdo do arquivo
            self.assertIn('Tarefa 3', conteudo_atualizado)


if __name__ == '__main__':
    unittest.main()
