import os

os.system("cls || clear")

numero = float(input("Digite um Número em Metros: "))

cm = numero*100
mili = numero*1000

print("Número Digitado {:.1f}".format(numero))

print("\nCentímetros: ",cm)
print("Milímetros: ",mili)
