#Dicionário                                    #O que é expressões regulares?
import json 

#montar um arquivo json, dicionario com as informações que vamos precisar guardar, diciplina do curso, atividades da diciplina, conteudo do curso 
# dps fazer a parte de dicionarios de de turma e alunos. 
#fazer login simples


# Cadastro:  inserir, alterar, apagar, leitura.
# CRUD  
# Created, read, update, delete 
   

#created
nome    = input("Nome...: ").capitalize()
celular = input("Celular: ")
email   = input("E-mail.: ").lower()

agenda = {}
agenda["nome"]    = nome
agenda["celular"] = celular
agenda["email"]   = email
print(agenda)
#Read
print(f"Agenda:  {agenda["nome"]}") # Mostra o atributo "nome" q esta dentro da agenda
print(f"Celular: {agenda["celular"]}") # Mostra o atributo "celular" q está dentro da agenda
print(f"Email:   {agenda["email"]}") # Mostra o atributo "email" q está dentro da agenda 

lista = []
lista.append(agenda)
print(lista)

with open("dados.json", "w") as arquivo:
    json.dump(lista,arquivo,indent=4)
 

#Dicionário                                    #O que é expressões regulares?
import json 


versao 2 


# Cadastro:  inserir, alterar, apagar, leitura.
# CRUD  
# Created, read, update, delete 
   

#created

agenda = {}
agenda["nome"]    = input("Nome...: ).capitalize()
agenda["celular"] = input("Celular: )
agenda["email"]   = input("Email..: ).lower()
print(agenda)
#Read
print(f"Agenda:  {agenda["nome"]}") # Mostra o atributo "nome" q esta dentro da agenda
print(f"Celular: {agenda["celular"]}") # Mostra o atributo "celular" q está dentro da agenda
print(f"Email:   {agenda["email"]}") # Mostra o atributo "email" q está dentro da agenda 

lista = []
lista.append(agenda)
print(lista)


with open("dados.json", "w") as arquivo:
    json.dump(lista,arquivo,indent=4)    #cerelizar 

print(f"Nome...: {lista[0]["nome"]}")  


#dados.json leitura de arquivo
import json

with open ("dados.json", "r") as arquivo:
    lista_carregada = json.load(arquivo)

print(lista_carregada)
print(lista_carregada[0]["email"])    

