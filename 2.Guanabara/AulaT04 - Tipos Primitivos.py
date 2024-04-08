import os

os.system("cls || clear")
 
 #Declarando variável, e perguntando ao usuário
tipo = input("Digite algo: ")

#obtendo o tipo dos dados digitados
print("O tipo Primitivo é: ",type(tipo))
print("Só tem espaços : ", tipo.isspace())
print("É um Número: ",tipo.isnumeric())
print("É alfabético: ",tipo.isalpha())
print("É alfanúmerico ? ",tipo.isalnum())
print("Esta em Maiúscula ?",tipo.isupper())
print("Esta em Minúscula ?",tipo.islower())

