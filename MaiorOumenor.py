def maiormenor(n1, n2):
    return "maior" if n1 > n2 else "menor"

def main():
    n1 =int(input("Numero 1: "))
    n2 =int(input("Numero 2: "))
    print(f" O numero:{n1} é {maiormenor(n1, n2)} que o número {n2}") 

if __name__ == "__main__":
    main()