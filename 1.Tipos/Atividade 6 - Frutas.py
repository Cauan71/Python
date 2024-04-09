import os

os.system("cls || clear")


qmorango = int(input("Digite a quantidade de Morangos em KG comprados: "))
qmaca = int(input("Digite a quantidade de maçãs em KG compradas: "))

if qmorango <=5:
    precoMorango = 2.50
else:
    precoMorango = 2.20

if qmaca <5:
    precoMaca = 1.80
else:
    precoMaca = 1.50

somaMorango = qmorango*precoMorango
somaMaca = qmaca*qmorango

valorFrutas = somaMorango+somaMaca
valorReais = float



if valorFrutas > 8 or valorReais > 25:
    desconto = 0.01

print("Valor Total a pagar: ",)

