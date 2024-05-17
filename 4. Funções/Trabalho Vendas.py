import os
import time

os.system("cls || clear")

login_cadastrado = "admin"
senha_cadastrada = 123

lista = []

class addProduto:
    def __init__(self, descricao, tamanho, preco, cor, quantidade):
        self.descricao = descricao
        self.tamanho = tamanho
        self.preco = preco
        self.cor = cor
        self.quantidade = quantidade


def logo():
    print("="*5, "URBAN OUTFIT ", "="*5)

def opcoes_cadastro():
    print("1 - Camisas")
    print("2 - Shorts")
    print("3 - Sapatos")

def menu():
    print("="*5, "URBAN OUTFIT ", "="*5)
    print("1 - Cadastrar Produto ")
    print("2 - Comprar um Produto")
    print("3 - Verificar Estoque ")
    print("4 - Sair do Página ")

while True:
    menu()
    opcao = int(input("Escolha a opção desejada: "))


    if opcao == 1:
        os.system("cls || clear")
        logo()
        login = input("Informe o seu login: ")
        senha = int(input("Informe a sua senha: "))

        if login == login_cadastrado and senha == senha_cadastrada:
            os.system("cls || clear")
            logo()
            print("Bem Vindo!! ")
            time.sleep(2)
            os.system("cls || clear")
            logo()
            opcoes_cadastro()
            escolha = int(input("Escolha a opção que deseja cadastrar: "))
            
            if escolha == 1:
                descricao = input("Digite a descrição da camisa: ")
                tamanho = input("Digite o tamanho da camisa: ")
                preco = float(input("Digite o preço :"))
                cor= input("Digite a cor da camisa: ")
                quantidade = int(input("Digite a quantidade desejada: "))
                lista.append(addProduto(descricao,tamanho,preco,cor,quantidade))
                os.system("cls || clear")

            elif escolha == 2:
                logo()
                descricao = input("Digite a descrição do Short: ")
                tamanho = int(input("Digite o tamanho do Short( Ex = 38): " ))
                cor= input("Digite a cor do Short: ")
                os.system("cls || clear")


        else:
            os.system("cls || clear")
            print("Login e senha Inválidos, tente novamente...")
            time.sleep(2)
            os.system("cls || clear")
    if opcao == 2:
        logo()
        opcoes_cadastro()
        escolha = int(input("Escolha a opção desejada : "))    
        
    if opcao == 3:
        for addProduto in lista:
            print("===== PRODUTO =====")
            print("Descrição do Produto: {}".format(addProduto.descricao))
            print("Preço: {}".format(addProduto.preco))
            print("Cor: {}".format(addProduto.cor))
            print("Tamanho: {}".format(addProduto.tamanho))
            print("Quantidade: {}\n".format(addProduto.quantidade))
            time.sleep(10)
            os.system("cls || clear")

    if opcao == 4:
        os.system("cls || clear")
        logo()
        print("Finalizando do programa ....")
        time.sleep(3)
        break