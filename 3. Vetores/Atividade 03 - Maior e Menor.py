import os

os.system("cls || clear")

lista = []
maiorNumero = 0
menorNumero = 9999

for i in range(5):
    numero = int(input(f"Digite o {i+1} número: "))
    lista.append(numero)

    if numero > maiorNumero:
        maiorNumero = numero

    if numero < menorNumero:
        menorNumero = numero

for i in range(5):
    print(f"\n{i+1} Número: {lista[i]}")
print(f"Maior Número: {maiorNumero}")
print(f"Menor Número: {menorNumero}")