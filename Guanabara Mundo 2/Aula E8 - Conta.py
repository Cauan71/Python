import os

os.system("cls || clear")
def pagar():
    print("1 - Á Vista Dinheiro / Cheque ")
    print("2 - Á Vista no Cartão ")
    print("3 - Cartão")

def logo():
    print("===== Curso em Vídeo =====")

aVista = 0.10
cartao = 0.10
valor_pagar : float 

valor = float(input("Digite o valor total da compra do produto: "))
logo()
pagar()
condicao_pagamento = input("Escolha a forma de pagamento: ")

if condicao_pagamento == 1:
    valor_pagar = (valor * aVista) - valor

elif condicao_pagamento == 2:
    valor_pagar = (valor * 0.05) - valor

elif condicao_pagamento == 3:
    parcelas =  int(input("Quantas parcelas irá pagar? "))
    
    if parcelas <= 2:
        valor_pagar = valor
    else:
        valor_pagar = (valor * 0.20) + valor

else:
    print("Digite uma opção válida!! ")

logo()
print("Valor Total do Produto: R$ {}".format(valor_pagar))



