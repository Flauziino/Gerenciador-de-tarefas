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
        captured_output = StringIO()
        sys.stdout = captured_output

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


if __name__ == '__main__':
    unittest.main()
