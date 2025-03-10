import os
import time

os.system("cls || clear")

login_cadastrado = "admin"
senha_cadastrada = 123

lista = []
cartao = 0.10
aVista = 0.10

class addProduto:
    def __init__(self, descricao, tamanho, preco, cor, quantidade,tipo):
        self.descricao = descricao
        self.tamanho = tamanho
        self.preco = preco
        self.cor = cor
        self.quantidade = quantidade
        self.tipo = tipo

def limpar():
    os.system("cls || clear")

def pagar():
    print("1 - Á Vista ( 10% de desconto)")
    print("2 - Cartão de Crédito (10% de acréscimo) ")

def logo():
    print("="*5, "URBAN OUTFIT ", "="*5)

def opcoes_cadastro():
    print("1 - Camisas")
    print("2 - Shorts")
    print("3 - Sapatos")
    
def cadastrar_produto(tipo):
    descricao = input("Digite a descrição do produto: ")
    tamanho = input("Digite o tamanho : ")
    preco = float(input("Digite o preço :"))
    cor = input("Digite a cor :")
    quantidade = int(input("Digite a quantidade desejada: "))
    lista.append(addProduto(descricao,tamanho,preco,cor,quantidade,tipo))
    limpar()
    print(f"{tipo} cadastrado(a) com sucesso !! ")
    
    
def comprar_produto():
    if not lista:
        print("Não há Itens disponíveis para compra ..")
        return
    
    print("Produtos Disponíveis:")
    for i in range(len(lista)):
        addProduto = lista[i]
        print(f"{i+1} - {addProduto.tipo} - {addProduto.descricao} - ({addProduto.tamanho} , {addProduto.cor}) - R$ {addProduto.preco} - {addProduto.quantidade} Unidades Disponíveis.")
    
    escolha = int(input("Escolha o número do Item que deseja: ")) - 1
    
    if 0 <= escolha < len(lista):
        
        quantidade = int(input("Digite a quantidade desejada: "))
        addProduto = lista[escolha]
        
        limpar()
        logo()
        pagar()
        pagamento = int(input("Digite a forma de pagamento desejada: "))

        if quantidade <= addProduto.quantidade:
            custoTotal = addProduto.preco * quantidade
            addProduto.quantidade -= quantidade

            if pagamento == 1:
                desconto = custoTotal * aVista
                total =  custoTotal - desconto

                limpar()
                logo()
                print(f"Você comprou {quantidade} {addProduto.tipo}. Custo Total : R$ {total :.2f}")

            
            elif pagamento == 2:
                acrescimo = custoTotal * cartao
                total = custoTotal + acrescimo

                limpar()
                logo()
                print(f"Você comprou {quantidade} {addProduto.tipo}. Custo Total : R$ {total :.2f}")
                

            else:
                limpar()
                logo()
                print("Opção Inválida, tente novamente...")
                time.sleep(2)
                limpar()
        
        else:
            print("Produto não está disponível no estoque..")
            
    else:
        print("Opção Inválida, tente Novamente...")
        

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
        limpar()
        logo()
        login = input("Informe o seu login: ")
        senha = int(input("Informe a sua senha: "))

        if login == login_cadastrado and senha == senha_cadastrada:
            limpar()
            logo()
            print("Verificando dados...")
            time.sleep(2)
            print("Bem - Vindo(a) !! ")
            limpar()

            logo()
            opcoes_cadastro()
            escolha = int(input("Escolha a opção que deseja cadastrar: "))
            
            if escolha == 1:
                cadastrar_produto("Camisa")
            elif escolha == 2:
                cadastrar_produto("Short")
            elif escolha == 3:
                cadastrar_produto("Sapato")
            else:
                print("Opção Inválida, tente novamente...")
                time.sleep(2)
                limpar()
        else:
            limpar()
            logo()
            print("Login e senha Inválidos, tente novamente...")
            time.sleep(2)
            limpar()
    elif opcao == 2:
        limpar()
        logo()
        comprar_produto()
        time.sleep(3)
        limpar()
        

    elif opcao == 3:
        os.system("cls || clear")
        logo()
        if lista:
            for produto in lista:
                print("===== PRODUTO =====")
                print(f"Tipo: {produto.tipo}")
                print(f"Descrição: {produto.descricao}")
                print(f"Preço: R$ {produto.preco}")
                print(f"Cor: {produto.cor}")
                print(f"Tamanho: {produto.tamanho}")
                print(f"Quantidade: {produto.quantidade}\n")
        else:
            print("Nenhum produto cadastrado.")
        input("Pressione Enter para continuar...")
        os.system("cls || clear")
    elif opcao == 4:
        os.system("cls || clear")
        logo()
        print("Finalizando o programa...\n")
        print("Aluno(s): Iuri Cauan\n\t  João Luiz")
        time.sleep(5)
        break
    else:
        print("Opção inválida. Tente novamente.")
        os.system("cls || clear")

