import os
import time
os.system("cls || clear")

def menu():

    print("\n===== M E N U ===== ")
    print(" 1 - Somar ")
    print(" 2 - Multiplicar ")
    print(" 3 - Maior  ")
    print(" 4 - Novos Números ")
    print(" 5 - Sair do Programa ")
    print("="*21)

num1 = int(input("Digite o primeiro Número: "))
num2 = int(input("Digite o segundo número: "))

os.system("cls || clear")        

while True:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        soma = num1 + num2
        print("A Soma de {} e {} é: {}".format(num1,num2,soma))
        time.sleep(3)
        os.system("cls || clear")
    elif opcao == 2:
        multiplicar = num1 * num2
        print("A Multiplicação de {} e {} é: {}".format(num1,num2,multiplicar))
        time.sleep(3)
        os.system("cls || clear")   
    elif opcao == 3:
        if num1 > num2:
            print("O número {} é maior que o número {}".format(num1,num2))
            time.sleep(3)
            os.system("cls || clear")
        elif num2 > num1 :
            print("O número {} é maior que o número {}".format(num2,num1))
            time.sleep(3)
            os.system("cls || clear")
        else:
            print("Os números são iguais")
            time.sleep(3)
            os.system("cls || clear")


    elif opcao == 4:
        num1 = int(input("Digite o primeiro Número: "))
        num2 = int(input("Digite o segundo número: "))
        os.system("cls || clear")

    elif opcao == 5:
        os.system("cls || clear")
        print("Saindo do Programa.....")
        time.sleep(3)
        break
    else:
        os.system("cls || clear")
        print("Opção Inválida, tente novamente.....")
        time.sleep(3)