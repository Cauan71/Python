import os
import time

os.system("cls || clear")

login_cadastrado = "admin"
senha_cadastrada = 123

lista = []

class addProduto:
    def __init__(self, descricao, tamanho, preco, cor):
        self.descricao = descricao
        self.tamanho = tamanho
        self.preco = preco
        self.cor = cor


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
                lista.append(addProduto(descricao,tamanho,preco,cor))

            elif escolha == 2:
                logo()
                descricao = input("Digite a descrição do Short: ")
                tamanho = int(input("Digite o tamanho do Short: EX: 38"))
                cor= input("Digite a cor do Short: ")


        else:
            os.system("cls || clear")
            print("Login e senha Inválidos, tente novamente...")
            time.sleep(2)
            os.system("cls || clear")
    if opcao == 2:
        logo()

    if opcao == 3:
        for addProduto in lista:
            print("Descrição do Produto: ")
            print("Tamanho")
            print("")
            print("")

    if opcao == 4:
        os.system("cls || clear")
        logo()
        print("Finalizando do programa ....")
        time.sleep(3)
        break