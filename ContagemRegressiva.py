# Conta regressiva  de um número até 0 

def contagemRegressiva (n):
    c = n 
    while c >= 0: 
        print(c)
        c -= 1 
    

def main():
    n = int(input("Digite um número para regredi-lo a zero: "))
    (contagemRegressiva(n))
    
    
        
        
    
if __name__ == "__main__":
    main()
