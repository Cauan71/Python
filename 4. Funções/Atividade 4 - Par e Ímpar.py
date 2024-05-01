import os
 
def menu():
    os.system("cls  || clear")
    print("===== S E N A I =====")

def verificar(n1):
    if n1 %2 == 0:
        print("Número Par")
    else:
        print("Número Ímpar")

menu()
num1 = int(input("Digite um número: "))

verificar(num1)
