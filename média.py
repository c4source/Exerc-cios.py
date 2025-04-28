#Exercicio 2 média

def media(n1, n2, n3):
    return (n1 + n2+ n3) / 3

def main():
    n1 =int(input("Nota 1: "))
    n2 =int(input("Nota 2: "))
    n3 =int(input("Nota 3: "))
    print ("A média do aluno é: ",round(media(n1, n2, n3),2)) # print(f"A média do aluno é: {media(n1, n2, n3):.2f}")

if __name__ == "__main__":
    main()

