import os

os.system("cls || clear")

resposta = "S"
contador = media = soma =  0
maior_numero = 0
menor_numero = 999

while resposta == "S":
    num = int(input("Digite um número: "))
    contador += 1
    soma += num
    resposta = str(input("Quer continuar? [S / N ] ")).upper().strip()  [0] 
    
    #upper = letras maiúsculas
    #strip = tirar os espaços
    #[0] = considerar a primeira letra

    media = soma/contador

    if num > maior_numero:
        maior_numero = num

    if num < menor_numero:
        menor_numero = num 

    if resposta == "N":
        print("\nVocê digitou {} números ".format(contador))
        print("A soma deles foi de {} ".format(soma))
        print("A média deles foi de {} ".format(media))
        print("Maior Número: {}".format(maior_numero))
        print("Menor Número: {} ".format(menor_numero))
        break


