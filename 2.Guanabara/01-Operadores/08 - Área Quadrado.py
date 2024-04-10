import os

os.system("cls || clear")

area = int
base = int(input("Digite a largura da parede: "))
altura = int(input("Digite a altura da parede: "))

#1 litro de tinta = 2m²
area = base*altura
tinta = area/2


print("Área Total da Parede: ",area)
print("Litros de Tinta necessárias: ",tinta)

