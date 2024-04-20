import os

os.system("cls || clear")

SIZE = 6
lista = []

for i in range(SIZE):
        numero = int(input(f"Digite o {i+1} número: "))
        lista.append(numero)


for i in range(SIZE-1,-1,-1):
        print(f"{i+1}ª Número: {lista[i]}")

