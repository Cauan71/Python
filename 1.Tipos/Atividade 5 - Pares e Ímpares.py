import os

os.system("cls || clear")
numero = int
numeros = []
i = int
soma = float = 0
for i in range(5):
    numero =int(input(f"{i+1}ª Nota: "))
    numeros.append(numero)
    soma+=numero
pares = 0
impar = 0



for numero in numeros:

    if numero %2 == 0:
        pares +=1   
    else :
        impar +=1

print("Números PARES: ",pares)
print("Quantidade Ímpares: ",impar)
print("Soma dos Números: ",soma)