import os

os.system("cls || clear")

soma:int = 0
contador: int = 0 

for i in range(1,7):
    num = int(input(f"Digite o {i}ª Número: "))

    if num % 2 == 0:
        contador = contador + 1
        soma = soma + num

print("Soma dos Números Pares: {}".format(soma))
print("Quantidade de Números Pares: {}".format(contador))