import random
import string

def gerar_senha(tamanho=8, incluir_maiusculas=True, incluir_numeros=True, incluir_pontuacao=True):
    caracteres = string.ascii_lowercase
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_pontuacao:
        caracteres += string.punctuation
    
    if len(caracteres) == 0:
        raise ValueError("Pelo menos um tipo de caractere deve ser incluído.")

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    try:
        tamanho_senha = int(input("Digite o tamanho da senha (mínimo 1): "))
        if tamanho_senha < 1:
            raise ValueError("O tamanho da senha deve ser pelo menos 1.")
        
        incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").strip().lower() == 's'
        incluir_numeros = input("Incluir números? (s/n): ").strip().lower() == 's'
        incluir_pontuacao = input("Incluir caracteres especiais? (s/n): ").strip().lower() == 's'
        
        senha = gerar_senha(tamanho_senha, incluir_maiusculas, incluir_numeros, incluir_pontuacao)
        print("Senha gerada:", senha)
    
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
