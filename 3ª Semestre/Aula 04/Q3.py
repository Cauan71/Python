import os
import time

def limpar():
    os.system("cls || clear")

lista = []
maiorNumero = 0
menorNumero = 9999
soma = 0

limpar()
for i in range(10):
    numeros = int(input(f"Digite o {i+1}ª Número: "))
    lista.append(numeros)
    
    soma+= numeros
    
    if numeros > maiorNumero:
        maiorNumero = numeros
        
    if numeros < menorNumero:
        menorNumero = numeros
       
limpar()
print("===== RESULTADO =====")
print(f"Maior Número: {maiorNumero}") 
print(f"Soma dos Valores: {soma}")
        