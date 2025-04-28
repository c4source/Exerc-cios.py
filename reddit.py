print("=============================")
print("Requsitos para aposentadoria.")
print("Homens: 65 anos e 30 anos de tempo de contribuição")
print("Mulheres: 60 anos e 25 anos de tempo de contribuição")
print("=============================")


def main():
    sexo = str(input("Sexo: ")). lower() 
    idade = int(input("Idade: "))
    tempo = int(input("Tempo de contribuição: "))

    if sexo == "masculino" and idade >= 65 and tempo >= 30: 
        print("Homem pode se aposentar")
    elif sexo == "feminino" and idade >= 60 and tempo >= 25: 
        print("Mulher pode se aposentar ")
    else:
        print("Não pode se aposentar ainda")    



if __name__ == "__main__":
    main()