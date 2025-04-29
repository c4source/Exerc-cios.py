#Verificar se a palavra é um Palindromo (Palavra que de tras para frente le-se igual)

def palindromo(palavra):      
    palavra = palavra.replace(" ", "").lower() # Substitur os espaços e transformar a palavra em letra minuscula
    palavra = ''.join(e for e in palavra if e.isalnum()) # Remover as pontuações
    return palavra == palavra[::-1]  # Verificar com um slicing se a palavra é um palíndromo
    


def main ():
    palavra = str(input("Qual palavra quer verificar se é um palíndromo?: "))
    if palindromo(palavra):
        print(f"A palavra {palavra} é um palíndromo")
    else:
        print(f"A palavra {palavra} não é um palíndromo")    







if __name__ == "__main__":
    main()