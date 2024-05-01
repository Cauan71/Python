import os

def menu():
    os.system("cls || clear")
    print("===== S E N A I =====")

def medir(n1):
    medicao = n1*100
    return medicao

menu()
num1 = int(input("Digite um número em Metros : "))

cm = medir(num1)

print("Valor de Metros para Centímetros: {}".format(cm))
