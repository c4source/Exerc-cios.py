#Sequência Fibonacci.

def fibonacci_while(n): 
    p = 0
    s = 1
    i = 0 
    while i <(n):               # Def loop while
       print(p)
       p, s = s, p + s 
       i += 1 

def fibonacci_for(n):         # Def loop for 
    p = 0
    s = 1 
    for c in range (n): 
        print(p)
        p, s = s, p + s 

def mainwhile():
    n = int(input("Digite o numero de termos para sequência fibonacci: "))
    fibonacci_while(n)

def mainfor():
    n = int(input("Digite o numero de termos para sequência fobonacci: ")) 
    fibonacci_for(n)
if __name__ == "__main__":
    mainwhile()
    mainfor()
