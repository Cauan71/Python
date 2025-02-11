import os
import time

os.system("cls || clear")

numeros = []

while True:
    valor = int(input("Digite um número: "))

    
    if (valor == -1):
        print("Finalizando.....")
        time.sleep(3)
        break
    else:
        numeros.append(valor)

for i in numeros:
    if(i %2 == 0):
        print(i)


