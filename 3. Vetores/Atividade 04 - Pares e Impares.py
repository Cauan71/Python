import os

os.system("cls || clear")

lista = []
pares: int = 0
impares : int = 0 

for i in range(6):
    numero = int(input(f"Digite o {i+1}ª Número: "))
    lista.append(numero)

    if numero %2 == 0:
        pares = pares + 1
    else :
        impares = impares + 1
for i in range(6):
    print(f"{i+1}ª Número Informado: {lista[i]}")
print("Quantidade de Números Pares: {}".format(pares))
print("Quantidade de Números Ímpares: {}".format(impares))