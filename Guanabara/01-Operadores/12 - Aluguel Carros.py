import os

os.system("cls || clear")

km = float(input("Digite o KM percorridos: "))
dias = int(input("Digite a quantidade de dias alugado: "))

valorKm = km*0.15
valorDias = dias*60
valorTotal = valorDias+valorKm

#valorTotal = (dias * 60) + (km * 0.15)

os.system("cls || clear")

print("Valor a pagar em KM: R$ {:.2f}".format(valorKm))
print("Valor a pagar em Dias: R$ {:.2f}".format(valorDias))
print("Valor Total á pagar: R$ {:.2f}".format(valorTotal))
