#Sequência Fibonacci.

def fibonacci_while(n): 
    p = 0      # primeiro numero começa com zero, então atribuimos o valor 0 a ele.         
    s = 1        # o segundo numero é 1, atribuimos o valor 1 
    i = 0        # contador começa contar do zero 
    
    while i <(n):   #Enquanto o contador for menor que o numero solicitado. # Def loop while
       print(p)     #print o primeiro numero que é 0
       p, s = s, p + s         # roca os valores: p recebe o valor anterior de s, e s recebe a soma dos valores anteriores de p e s
       i += 1           #contador recebe mais um a cada repetição

def fibonacci_for(n):           # Def loop for 
    p = 0                       # primeiro numero = 0    
    s = 1                       # segundo numero = 1   
    for c in range (n):         # contador conta até o numero solicitado pelo usuario
        print(p)                # Imprime o numero atual da sequência
        p, s = s, p + s         # p recebe o valor anterior de s, e s recebe a soma dos valores anteriores de p e s 

def mainwhile():
    n = int(input("Digite o numero de termos para sequência fibonacci: "))
    fibonacci_while(n)

def mainfor():
    n = int(input("Digite o numero de termos para sequência fobonacci: ")) 
    fibonacci_for(n)
if __name__ == "__main__":
    mainwhile()
    mainfor()
