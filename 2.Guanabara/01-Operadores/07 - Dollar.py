import os

os.system("cls || clear")

real = float(input("Digite quanto de dinheiro você tem: R$ "))
dolar = real/3.27

print("Com R$ {:.2f} você pode comprar US$ {:.2f}".format(real,dolar))
