from nis import match
import os

os.system("cls || clear")

numero = int(input("Digite um número: "))

dobro = numero*2
triplo = numero*3
raiz = numero**0.5 ## ou numero ** (1/2)

print("Dobro : ",dobro)
print("Triplo: ",triplo)
print("Raiz Quadrada {:.2f}".format(raiz))
