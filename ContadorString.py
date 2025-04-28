#Comando len() função que retorna o número de elementos de um objeto
#Listas, dicionários, Strings, tuplas, conjuntos etc. 

def main():
    nome = "Atman"     #Retornou o numero de caracteres da string "gabriel"
    print(len(nome))
    print(f"Números de caracteres da string {nome} é:", len(nome)) 

def main2():
    lista = [1, 2, 3, 4, 5, 5, 2 ,32, 23, 23, 12, 12, 43]
    print(f"elemenetos da lista: ", lista)
    print(f"O número de elementos da lista é: ", len(lista))






if __name__ == "__main__":
    main()
    main2()
