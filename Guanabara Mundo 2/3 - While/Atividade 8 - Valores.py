import os

os.system("cls || clear")

soma  = num = contador = 0
termo = 999

while num != termo:
    num = int(input("Digite um número: "))
    
    if num != termo:
        soma += num
        contador +=1
    else:
        print("Você digitou {} números!! ".format(contador))
        print("A soma deles deu: {}".format(soma))
        break