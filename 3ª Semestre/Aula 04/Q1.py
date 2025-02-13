import os
import time
os.system("cls || clear")

numeros = []
maiorNumero = 0
menorNumero = 9999

for i in range(3):
    numero = int(input(f"Digite o {i+1}ª número: "))
    numeros.append(numero)
    
    if numero > maiorNumero:
        maiorNumero = numero
        
    if numero < menorNumero:
        menorNumero = numero
        
    
    
    

os.system("cls || clear")
print("="*5, " RESULTADO ", "="*5)
print(f"O Menor Número é: {menorNumero}")
print(f"O Maior Número é: {maiorNumero}")