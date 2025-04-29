#Calculo IMC
def imcc(al, pe):
    return pe / (al ** 2)

def classificarimc(imc):
    if imc < 18.5:
        return "Abaixo do peso ideal"
    elif imc < 25:
        return "Dentro do peso normal"
    elif imc < 30:
        return "Execesso de peso"
    elif imc < 35: 
        return "Obseidade classe 1"
    elif imc < 40:
        return "Obsedidade Classe 2"
    else:
        return "Obesidade Classe 3"
    
def main():
    al = float(input("Altura: "))
    pe = float(input("Peso: "))
    imc = imcc(al, pe)
    classificaçao = classificarimc(imc)
    print(F"O seu IMC é: {imc:.2f} Você está {classificaçao}.")



if __name__ == "__main__":
    main()