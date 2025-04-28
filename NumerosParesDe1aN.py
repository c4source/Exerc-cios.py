#Numeros pares de 1 a N

def pares(n):
    for c in range(1, n + 1):
        if c % 2 == 0:
            print(c) 
    
def main():
    n =int(input("Número até contar: "))

    pares(n)




if __name__ == "__main__":
    main()            