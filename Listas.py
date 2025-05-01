def main():
    numeros = [1, 2, 3, 4, 5]
    
    numeros [2] = 6  #Atribui valor a posição 2 da lista 
    
    numeros.append(10)    #Add o elemento 10 no final da lista (.APPEND)
    
    for num in numeros:     #Printar os numeros da lista com um loop for do primeiro ao ultimo elemento
        print(num)  
    print(len(numeros))     #Printa o numero de posições/elementos de uma lista
    
    print(numeros)
    numeros.insert(2, 8) #Add um novo valor(elemento) dentro da lista na posição que escolher. Colocando o valor antigo para direita
    print(numeros[2])
    print(numeros)
    print(numeros[3])
    numeros.remove(4)
    print(numeros)
    numeros.pop() 
    print(numeros)
    #numeros.append(50).pop()
    #print(numeros)
    del numeros[3]
    print(numeros)
    numeros.pop(1)
    print(numeros)
    
            
def main():
    lista = []
 
    for i in range(5):
        n = int(input("Numero: "))
        lista.append(n)
    print(f"A soma  da lista é {sum(lista)}")
    print(lista)

if __name__ == "__main__":
    main()
