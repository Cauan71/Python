import os

os.system("cls || clear")
lista = []

for i in range(2):
    print(f"\n===== {i+1}ª Pessoa =====")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Sexo [M / F]: ")

    lista.append(idade)

    soma = soma + idade
    media = soma/2   


print("Média : {}".format(media))