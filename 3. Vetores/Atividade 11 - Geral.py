import os

os.system("cls || clear")

SIZE = 5
lista = []

pares : int = 0
impares : int = 0

positivo: int = 0
negativo : int = 0

contador : int = 0
contadorPar : int = 0
contadorImpar : int = 0


maiorNumero: int = 0
menorNumero: int = 99999

somaPar: int = 0
somarImpar : int = 0
somaTotal: int = 0

mediaImpar : int = 0
mediaPar : int = 0
mediaTotal: int = 0 

for i in range(SIZE):
    numero = int(input(f"Digite o {i+1}ª Número: "))
    lista.append(numero)
    contador = contador + 1
    

    if numero %2 == 0:
        contadorPar = contadorPar + 1
        pares = pares + 1
        somaPar = somaPar + lista[i]
        mediaPar = somaPar / contadorPar
    else :
        contadorImpar = contadorImpar + 1
        impares = impares + 1
        somarImpar = somarImpar + lista[i]
        mediaImpar = somarImpar / contadorImpar


    if numero >=0:
        positivo = positivo + 1
    else:
        negativo = negativo + 1

    if numero > maiorNumero:
        maiorNumero = numero

    if numero < menorNumero:
        menorNumero = numero

somaTotal = somaPar+somarImpar
mediaTotal = somaTotal/contador

print("Quantidade de Números Pares: {}".format(pares))
print("Quantidade de Números Ímpares: {}".format(impares))
print("Quantidade de Números Positivos: {}".format(positivo))
print("Quantidade de Números Negativos: {}".format(negativo))
print("Quantidade de Números Inseridos: {}".format(contador))
print("Maior Número: {}".format(maiorNumero))
print("Menor Número: {}".format(menorNumero))
print("Média dos Números Pares: {}".format(mediaPar))
print("Média dos Números Ímpares: {}".format(mediaImpar))
print("Média Total: {}".format(mediaTotal))

for i in range(SIZE-1, -1 , -1):
    print(f"{i+1}ª Número : {lista[i]}")



