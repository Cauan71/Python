import os

os.system("cls || clear")
numero = int
numeros = []

for i in range(5):
    numero =int(input("Digite um Número: "))
    numeros.append(numero)
    
pares = 0
impar = 0

for numero in numeros:

    if numero %2 == 0:
        pares +=1   
    else :
        impar +=1

print("Números PARES: ",pares)
print("Quantidade Ímpares: ",impar)
