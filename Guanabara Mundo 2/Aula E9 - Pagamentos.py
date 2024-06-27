import os

os.system("cls || clear")
print("===== Guanabara =====")
valor = float(input("Digite o valor da compra: "))

os.system("cls || clear")


print("===== PAGAMENTO =====")
print("1 - Á Vista (Dinheiro ou cheque)")
print("2 - Á Vista (Cartão)")
print("3 - 2x no Cartão")
print("4 - 3x ou mais no cartão")
pagar = int(input("Escolha uma forma de pagamento: "))

os.system("cls || clear")

if pagar == 1:
    total = valor - (valor*0.10)

elif pagar == 2:
    total = valor - (valor*0.05)

elif pagar == 3:
    total = valor

elif pagar == 4:
    parcelas = int(input("Digite a quantidade de parcelas:  "))
    total = valor + (valor * 0.20)
    totalprc = total /parcelas
    print(f"\nSua Compra sera parcelada em {parcelas} vezes, a um valor de {totalprc} mensais! ")

else:
    print("Digite uma opção válida!! ")


print("Valor a Pagar: {}".format(total))
