import os
import time


def limpar():
    os.system("cls || clear")
    
numeros = []
soma = 0
contador = 0

limpar()
for i in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    contador = contador + 1
    
    soma+= numero
    
    media = soma/contador
    
limpar()
print("===== RESULTADO =====")
print(f"Média dos Valores: {media}")    

