#Par ou impar (Condicional)
def parimpar (n1):
    return "par" if n1 % 2 == 0 else "impar" 
def main():
    n1 =int(input("Digite o número: "))
    print(f"O numero {n1} é {parimpar(n1)}") 




if __name__ == "__main__":
    main()
