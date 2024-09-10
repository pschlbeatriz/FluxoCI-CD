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
        self.a
