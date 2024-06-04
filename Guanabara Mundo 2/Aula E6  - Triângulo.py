import os

os.system("cls || clear")

n1 = int(input("Digite o primeiro segmento: "))
n2 = int(input("Digite o segundo segmento: "))
n3 = int(input("Digite o terceiro segmento: "))


if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("\nOs segmentos podem formar um triângulo !! ")

    if n1 == n2 == n3:
        print("\nTriângulo Equilátero ")
    elif n1 != n2 != n3 != n1:
        print("\nTriângulo Escaleno ")
    else: 
        print("\nTriângulo Isósceles")
else: 
    print("\nOs segmentos não podem formar um triângulo! ")
