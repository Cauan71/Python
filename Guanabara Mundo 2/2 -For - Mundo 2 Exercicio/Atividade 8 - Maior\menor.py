import os

os.system("cls || clear")



maior = 0
menor = 0

for i in range(1,6):
    peso = float(input("Digite o seu peso: "))

    if i == 1:
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

    
print("Maior Peso: {}".format(maior))
print("Menor Peso: {}".format(menor))