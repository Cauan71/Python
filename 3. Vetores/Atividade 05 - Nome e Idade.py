import os

os.system("cls || clear")

nomes = []
idades = []

for i in range(5):
    nome = input("Digite seu nome: ")
    nomes.append(nome)
    idade = int(input("Digite sua idade: "))
    idades.append(idade)
    os.system("cls || clear")

for i in range(5):
    print(f"{i+1}ª Nome Informado: {nomes[i]}")
    print(f"{i+1}ª Idade Informado: {idades[i]}\n")
