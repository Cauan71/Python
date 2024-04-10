import os

os.system("cls || clear")

salarioFinal = float
salarioAtual = float(input("Digite seu salário atual: "))

aumento = 0.15
reajuste = salarioAtual*aumento
salarioFinal = salarioAtual+reajuste

print("Salário Atual com aumento de 15 % :",salarioFinal)