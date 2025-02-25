# Função 

import os
def limpar():
    os.system("cls || clear")


def calcular(q,d):
    formula_KM = 0.15*km
    formula_dia = 60*dias

    total = formula_dia+formula_KM

    return total


limpar()
km = int(input("Digite a quantidade de KM Percorridos: "))
dias = int(input("Digite a quantidade de Dias Usado: "))


totalF = calcular(km,dias)
limpar()


print("===== TOTAL =====")
print(f"Valor da Viagem: R$ {totalF:.2f}")

