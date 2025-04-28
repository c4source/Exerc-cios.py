# Soma dos número de 1 a N
def soma (n):
    soma = 0
    c = 1  
    while c <= n: 
        print(f"{c}")
        soma += c 
        c += 1  
    return soma  

def main():
    n =int(input("Numero:"))
    resultado = soma(n)
    print(f"A soma dos números de 1 a {n} é: {resultado}")
  
if __name__ == "__main__":
    main()