import os

os.system("cls || clear")

def menu():
    print("-"*30)
    print(" \tLoja Baratão ")
    print("-"*30)

total = cont_preco = 0
menor_preco = 9999999


while True:
    menu()
    produto = input("Nome do produto: ")
    preco = float(input("Preço : "))
    opcao = str(input("Deseja continuar? [ S / N ]: ")).upper().strip()[0]

    total += preco

    if preco > 1000:
        cont_preco += 1

    if preco < menor_preco:
        menor_preco = preco
        barato = produto 

    if opcao == "N":
        break


print("\nHá {} produto(s) acima de R$ 1000 ".format(cont_preco))
print("Preço Total da compra: R$ {} ".format(total))
print("Produto mais barato foi {} que custa R$ {} ".format(barato, menor_preco))





