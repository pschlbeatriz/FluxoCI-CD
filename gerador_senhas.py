import argparse
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
    parser = argparse.ArgumentParser(description="Gerador de senhas")
    parser.add_argument('--tamanho', type=int, default=8, help="Tamanho da senha (mínimo 1)")
    parser.add_argument('--maiusculas', action='store_true', help="Incluir letras maiúsculas")
    parser.add_argument('--numeros', action='store_true', help="Incluir números")
    parser.add_argument('--pontuacao', action='store_true', help="Incluir caracteres especiais")

    args = parser.parse_args()

    try:
        if args.tamanho < 1:
            raise ValueError("O tamanho da senha deve ser pelo menos 1.")
        
        senha = gerar_senha(args.tamanho, args.maiusculas, args.numeros, args.pontuacao)
        print("Senha gerada:", senha)
    
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
