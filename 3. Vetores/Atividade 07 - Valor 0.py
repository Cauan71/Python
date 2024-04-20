import os

os.system("cls || clear")
SIZE = 5
lista = []

for i in range(SIZE):
    numero = int(input("Digite um número: "))
    lista.append(numero)

    if lista[i] < 0:
        lista[i] = 0

for i in range(SIZE):
    print(f"{i+1}ª número : {lista[i]}")

