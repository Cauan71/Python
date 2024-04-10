import os

os.system("cls || clear")
desconto = float
preco = float(input("Digite o preço do produto: R$ "))

desconto = preco*0.05
precoFinal = preco-desconto

#precoFinal = preco - (preco * 5 / 100 ) 
print("Preço do Produto com 5 % de desconto: R$ {:.2f}".format(precoFinal))
