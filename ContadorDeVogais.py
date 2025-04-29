# Função de contar vogais de uma string

def contador_vogal(palavra):
    vogais = "aeiou"
    return sum(1 for char in palavra.lower() if char in vogais)


def main():
    palavra =str(input(": "))
    NumeroVogais = contador_vogal(palavra)
    print(f" O número de vogais da palavra {palavra} é {NumeroVogais}") 


if __name__ == "__main__":
    main()