import os


def limpar():
    os.system("cls || clear")

def calculo(d,c,p):
    total = (d/c)*p

    return total


limpar()
dist = int(input("Digite a distância da viagem : "))
consumo = float(input("Digite o valor do consumo do veículo : "))
preco = float(input("Digite o preço do combustivel: "))


limpar()

total1 = calculo(dist, consumo, preco)


print("="*5, " RESULTADO ", "="*5)
print(f"Total Viagem: {total1}")



