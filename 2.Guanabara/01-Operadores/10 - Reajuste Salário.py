import os

os.system("cls || clear")

salarioFinal = float
salarioAtual = float(input("Digite seu salário atual: R$ "))

aumento = 0.15
reajuste = salarioAtual*aumento
salarioFinal = salarioAtual+reajuste

# salarioFinal = salarioAtual + (salarioAtual * 15 / 100)

print("Salário Atual com aumento de 15 % : R$ {:.2f}".format(salarioFinal))