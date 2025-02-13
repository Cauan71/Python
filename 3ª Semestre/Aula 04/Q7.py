import os
import time


def limpar():
    os.system("cls || clear")
    
numeros = []
contadorPositivo = 0
contadorNegativo = 0
soma = 0


limpar()
for i in range(3):
    numero = int(input(f"Digite o {i+1}ª número: "))
    numeros.append(numero)
    
    if numero >= 0:
        soma += numero
        contadorPositivo = contadorPositivo + 1
        
    else:
        contadorNegativo = contadorNegativo + 1

limpar()
print("===== RESULTADO =====")
(f"\nQuantidade de Números Positivos: {contadorPositivo}")
print(f"Quantidade de Números Negativos: {contadorNegativo}")
print(f"\nSoma dos Números Positivos: {soma}")        
        
        
    