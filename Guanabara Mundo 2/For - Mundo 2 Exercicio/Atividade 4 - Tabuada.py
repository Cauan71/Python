import os

os.system("cls || clear")

numero = int(input("Digite um número para gerar a tabuada: "))

for i in range(1,11):
    print(f"{numero} x {i} = {i*numero}")
