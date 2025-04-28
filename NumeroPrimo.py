# Números primos.

import math 

def primo (n):
    if n <= 1:
        return False    # 1ª Verificar se o numero n é menor ou igual a 1.
    for i in range (2, int(math.sqrt(n)) + 1): # 2ª passo gerar uma sequência de números do 2 até a raiz quadrada de n
        if n % i == 0:   # 3º passo verificar se o resto do numero até a raiz quadrada de n é 0 se for, não é primo. 
            return False  
    return True   # Se não encontrar nenhum divisor, o número é primo.       


def main():
    n = int(input("Digite o número para verificar se ele é primo: ")) 
    if primo(n):
        print(f"{n} é primo") 
    else:
        print(f"{n} não é primo") 



if __name__ == "__main__":
    main() 
