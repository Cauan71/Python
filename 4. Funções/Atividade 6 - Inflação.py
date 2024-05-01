import os

def menu():
    os.system("cls || clear")
    print("===== S E N A I =====")

def inflacionar(pedido):
    if pedido < 100:
        resultado = pedido * 0.10
        final = resultado + pedido
        print("Produto com 10% de Inflação")
    
    else:
        resultado = pedido * 0.20
        final = resultado + pedido
        print("Produto com 20% de Inflação")

    return final

menu()
produto = float(input("Digite o preço do produto: "))

menu()
preco = inflacionar(produto)
print("Valor Total do produto : {:.1f}".format(preco))

