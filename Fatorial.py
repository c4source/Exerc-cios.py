#Fatorial de um número
def fatorial(n):
    x = 1 
    while n >= 1:
        print(x)
        x *= n 
        n-= 1
    return x 

def main():
    n= int(input("Número para fatoriar: ")) 
    print(f"O fatorial de {n} é {fatorial(n)}")






if __name__ == "__main__":
    main()    