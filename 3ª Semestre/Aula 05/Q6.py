# for


import os

os.system("cls || clear")
contador_ney = 0
contador_messi = 0
contador_cr7 = 0



def menu():
    print("===== CANDIDATOS =====")
    print("1 - Neymar")
    print("2 - Messi")
    print("3 - CR7")
    
def limpar():
    os.system("cls || clear")
        
for i in range(5):
    limpar()
    menu()
    opcao = int(input("Escolha a opção: "))
    if opcao == 1:
        contador_ney += 1

    elif opcao == 2:
        contador_messi += 1

    elif opcao == 3:
        contador_cr7 += 1

    else:
        print("Digite uma opção válida")


limpar()
print("===== RESULTADO ===== ")
print(f"Vereador Neymar Fiel: {contador_ney}")
print(f"Vereador Messi Anão: {contador_messi}")
print(f"Vereador CR7 Robô: {contador_cr7}")
