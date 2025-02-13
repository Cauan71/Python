import os
import time

os.system("cls || clear")



numeros = []
soma = 0

while True:
    
    numero = int(input(f"Digite um Número: "))
    numeros.append(numero)
    
    if numero > 0:
        soma += numero
         
    elif numero == 0:
        os.system("cls || clear")
        print("="*5, " RESULTADO ", "="*5)
        print(f"A soma dos Valores é: {soma}")
        
    else:
        print("Digite um número válido")