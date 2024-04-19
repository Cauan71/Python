import os

os.system("cls || clear")

lista = []

for i in range(5):
    numero = int(input("Digite um número: "))
    lista.append(numero)

    if numero < 0:
        numero = 0

for i in range(5):
    print(f"{i+1}ª número : {lista[i]}")

