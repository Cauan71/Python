import os

os.system("cls || clear")

SIZE = 5
lista = []
contador : int = 0
pares : int = 0
impares : int = 0
positivo : int = 0
negativo : int = 0


for i in range(SIZE):
    numero = int(input(f"Digite o {i+1}ª número: "))
    lista.append(numero)
    contador = contador + 1
    
    if lista[i] %2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
        
    if lista[i] > 0:
        positivo = positivo + 1
    else:
        negativo = negativo + 1
        
os.system("cls || clear")

print("="*5, " R E S U L T A D O ", "="*5)
print("Quantidade de Números Pares: {}".format(pares))
print("Quantidade de Números Ímpares: {}".format(impares))
print("Quantidade de Números Positivos: {}".format(positivo))
print("Quantidade de Números Negativos: {}".format(negativo))
print("Quantidade de Números Inseridos: {}".format(contador))
print("="*32)
