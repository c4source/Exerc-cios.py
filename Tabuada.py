# Exercicio Tabuada (loop)

def tabuada(n):
    for c in range (1, 11):
        print(f"{n} x {c} = {n * c}")
    

def main():
    n =int(input("Número da tabuada: "))
    tabuada(n)
   


if __name__ == "__main__":
    main()    