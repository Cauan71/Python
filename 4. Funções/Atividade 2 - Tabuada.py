import os

os.system("cls || clear")

def menu():
    os.system("cls || clear")
    print("="*5, "S E N A I ", "="*5)

def tabuada(n1):
    for i in range(1,11):
        print("{} x {} = {}".format(n1 , i, n1*i))

menu()
num1 = int(input("Digite um Número para gerar a tabuada: "))

menu()
tabuada(num1)
