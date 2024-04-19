import os

os.system("cls || clear")

negativos: int = 0
soma: int = 0
lista = []

for i in range(10):
    numero = int(input(f"Digite o {i+1} número: "))
    lista.append(numero)

    if numero < 0:
        negativos = negativos + 1

    if numero > 0:
        soma = soma+numero

print("Soma dos Números Positivos: {}".format(soma))
print("Quantidade de Números Negativos: {}".format(negativos))