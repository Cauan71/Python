import os

os.system("cls || clear")

lista = []
maior_peso:int = 0
menor_peso:int = 9999

for i in range(2):
    peso = float(input("Digite o seu peso: "))
    lista.append(peso)

    if peso > maior_peso:
        maior_peso = peso
    
    if peso < menor_peso:
        menor_peso = peso

print("Maior Peso: {}".format(maior_peso))
print("Menor Peso: {}".format(menor_peso))
