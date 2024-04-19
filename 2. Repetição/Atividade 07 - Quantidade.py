import os
 
os.system("cls || clear")

par: int = 0
impar: int = 0
mediaPar: float
mediaTotal: float
somar: float = 0
while True:
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        par = par + 1
        somar = somar + numero
        mediaPar = somar/par
    else:
        impar = impar + 1

    
    if numero == 0:
        break
    


print("Quantidade de Números Ímpares: {}".format(impar))
print("Quantidade de Números Pares: {}".format(par))
print("Média Pares: {}".format(mediaPar))

