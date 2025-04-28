#Média ponderada. 

def mediaponderada(n1, n2, n3, p1, p2, p3):
        return ((n1 * p1) + (n2 * p2) + (n3 * p3)) / (p1 + p2 + p3) 
    



def main():
    n1 =int(input("Nota 1: "))
    n2 =int(input("Nota 2: "))
    n3 =int(input("Nota 3:" ))
    p1 =int(input("Peso 1: "))
    p2 =int(input("Peso 2: "))        
    p3 =int(input("Peso 3: "))
    media = mediaponderada(n1, n2, n3, p1, p2, p3)
    print(f"A média ponderada é: {media:.2f}") 




if __name__ == "__main__":
    main()    