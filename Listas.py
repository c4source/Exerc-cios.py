def main():
    numeros = [1, 2, 3, 4, 5]
    
    numeros [2]= 6
    
    numeros.append(10)    
    
    for num in numeros: 
        print(num)  
    print(len(numeros))
    
    print(numeros)
    numeros.insert(2, 8)
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
