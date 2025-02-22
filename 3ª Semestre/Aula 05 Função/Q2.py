import os

def limpar():
    os.system("cls || clear")

def menu():
    print("="*6, " MENU ", "="*6)
    print("\n1 - Matutino")
    print("2 - Vespertino")
    print("3 - Noturno")

limpar()    
menu()
op = int(input("Escolha uma opção: "))

if op == 1:
    print("Turno Matutino - Bom Dia!!")
elif op == 2:
    print("Turno Vespertino - Boa Tarde!!")
elif op == 3:
    print("Turno Noturno - Boa Noite!!")
else:
    print("Digite uma opção válida!")







