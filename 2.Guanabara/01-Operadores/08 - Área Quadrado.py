import os

os.system("cls || clear")

area = float
largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

#1 litro de tinta = 2m²
area = largura*altura
tinta = area/2


print("\nÁrea Total da Parede: {:.2f} m²".format(area))
print("Litros de Tinta necessárias: {:.2f} Litros de Tinta".format(tinta))

