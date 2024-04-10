import os

os.system("cls || clear")
desconto = float
preco = float(input("Digite o preço do produto: "))

desconto = preco*0.05
precoFinal = preco-desconto


print("Preço do Produto com 5 % de desconto: ",precoFinal)