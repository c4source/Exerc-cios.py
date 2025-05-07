#Dicionário                                    #O que é expressões regulares?
import json 




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
 
   
    

