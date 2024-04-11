import os

os.system("cls || clear")

soma: int = 0

for i in range(1,6):
    numero = int(input("Digite o {}ª número: ".format(i)))
    soma += numero
    

print("Soma dos Números: {}".format(soma))

