import os

def limpar():
    os.system("cls || clear")

def calculo(pp):
    multa = pp - 50
    multaF = (multa*4) + pp

    return multaF


limpar()
# Valor Limite = 50 kg
# > 50 = + 4,00 de Multa

peso_peixe = float(input("Digite o Peso do Peixe em KG: "))

limpar()
if peso_peixe > 50:
    precoF = calculo(peso_peixe)
    print(f"Limite em Excesso , Preço Total : {precoF}")

else:
    print(f"Valor Normal: R$ {peso_peixe}")



