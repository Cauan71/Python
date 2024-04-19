import os

os.system("cls || clear")

lista = [] 
lista.reverse

for i in range(6):
        numero = int(input("Digite um número: "))
        lista.append(numero)

os.system("cls || clear")

for i in range(0,6):
    print(f"Números: ", lista[-1])
    del(lista[-1])