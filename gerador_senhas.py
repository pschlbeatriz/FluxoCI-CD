import random
import string

def gerar_senha(tamanho=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

if __name__ == "__main__":
    tamanho_senha = int(input("Digite o tamanho da senha: "))
    print("Senha gerada:", gerar_senha(tamanho_senha))
