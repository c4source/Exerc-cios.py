#Juros Compostos
def juroscompostos(p, r, n):
    return p *(1 +r) ** n    #Equação de juros compostos: M = p x(1 +r)** n 
                             
    
def main ():
    p = float(input("Valor incial: R$ "))
    r = float(input("Taxa de juros mensal (%): ")) / 100 
    n = float(input("Tempo em meses: ")) 
    resultado = juroscompostos(p, r, n)
    print(f"Montante inicial de {p:.2f}")
    print(f"Taxa de juros mensal de {r*100:.2f}%")
    print(f"Periodo: {n} meses")
    print(f"Montante final: R$ {resultado:.2f}")



if __name__ == "__main__":
    main()    