# Exercicio número negativo positivo ou zero 

def positivonegativo (n1):
    return "Positivo" if n1 > 0 else "Negativo" if n1 < 0 else "Zero"

def main():
    n1 =int(input("Digite o número: "))
    print(f"O número {n1} é {positivonegativo(n1)}")

    
if __name__ == "__main__":
    main()