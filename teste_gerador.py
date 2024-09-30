import unittest
import string
from gerador_senhas import gerar_senha

class TestGeradorSenhas(unittest.TestCase):

    def test_senha_tamanho(self):
        senha = gerar_senha(12)
        self.assertEqual(len(senha), 12, "A senha deve ter 12 caracteres.")

    def test_senha_sem_maiusculas(self):
        senha = gerar_senha(12, incluir_maiusculas=False)
        self.assertTrue(senha.islower(), "A senha não deve conter letras maiúsculas.")

    def test_senha_com_numeros(self):
        senha = gerar_senha(12, incluir_numeros=True)
        self.assertTrue(any(char.isdigit() for char in senha), "A senha deve conter números.")

    def test_senha_com_pontuacao(self):
        senha = gerar_senha(12, incluir_pontuacao=True)
        self.assertTrue(any(char in string.punctuation for char in senha), "A senha deve conter caracteres especiais.")

    # Comentado temporariamente
    # def test_senha_sem_caracteres(self):
    #     with self.assertRaises(ValueError):
    #         gerar_senha(12, incluir_maiusculas=False, incluir_numeros=False, incluir_pontuacao=False)

class TestGeradorSenhas(unittest.TestCase):

    # Novo Teste 01: Geração de senha sem números
    def test_senha_sem_numeros(self):
        senha = gerar_senha(12, incluir_numeros=False)
        self.assertFalse(any(char.isdigit() for char in senha), "A senha não deve conter números.")

    # Novo Teste 02: Geração de senha sem caracteres especiais
    def test_senha_sem_pontuacao(self):
        senha = gerar_senha(12, incluir_pontuacao=False)
        self.assertFalse(any(char in string.punctuation for char in senha), "A senha não deve conter caracteres especiais.")

    # Novo Teste 03: Testa o tamanho da senha mínima
    def test_senha_tamanho_minimo(self):
        senha = gerar_senha(1)
        self.assertEqual(len(senha), 1, "A senha deve ter pelo menos 1 caractere.")

    # Novo Teste 04: Testa exceção se nenhum tipo de caractere for incluído
    def test_senha_sem_caracteres(self):
        with self.assertRaises(ValueError):
            gerar_senha(12, incluir_maiusculas=False, incluir_numeros=False, incluir_pontuacao=False)

    # Novo teste 05: Testa a senha gerada com todos os parâmetros ativos
    def test_senha_todos_parametros(self):
        senha = gerar_senha(12, incluir_maiusculas=True, incluir_numeros=True, incluir_pontuacao=True)
        self.assertTrue(any(char.isupper() for char in senha), "A senha deve conter letras maiúsculas.")
        self.assertTrue(any(char.isdigit() for char in senha), "A senha deve conter números.")
        self.assertTrue(any(char in string.punctuation for char in senha), "A senha deve conter caracteres especiais.")


if __name__ == "__main__":
    unittest.main()
    
