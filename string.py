# STRINGS E COMANDOS

#Exemplo 1   
def main():

    nome = "Gabriel"
    sobrenome = "Domingues"
    nome_completo = nome +" "+sobrenome     #Concatenação com +" "+ onde nome é "gabriel" e sobrenome é "domingues"                            
    print(nome_completo)

#Exemplo 2
def main2():

    nome = "Gabriel"
    sobrenome = "Domingues"
    nome_completo = f"{nome} {sobrenome}"  #Concatenação Fstring  
    print(nome_completo) 


if __name__ == "__main__":
    main()
    main2()