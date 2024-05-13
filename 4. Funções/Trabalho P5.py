import os
import time

os.system("cls || clear")


def menu():
    print("="*5," M E N U ", "="*5)
    print("1 - Cadastrar Login e Senha Funcionário")
    print("2 - Entrar no Sistema ")
    print("3 - Sair do programa ")


def informacoes():
    print("="*5," S E N A I ","="*5)
    salario_usuario = float(input("Digite seu Salário Base : "))
    transporte = input("Deseja receber o Vale Transporte (s/n)? ")
    refeicao = float(input("Digite o valor do vale refeição fornecido: "))
    return salario_usuario, transporte, refeicao


def salario_inss(salario_usuario):
    if salario_usuario < 1100:
        return salario_usuario * 0.075
    elif 1100 <= salario_usuario < 2203.48:
        return salario_usuario * 0.09
    elif 2203.48 <= salario_usuario < 3305.22:
        return salario_usuario * 0.12
    elif 3305.22 <= salario_usuario < 6433.57:
        return salario_usuario * 0.14
    else:
        return 751.99


def salario_irrf(salario_usuario):
    if 1903.98 <= salario_usuario < 2826.65:
        return salario_usuario * 0.075
    elif 2826.65 <= salario_usuario < 3751.05:
        return salario_usuario * 0.15
    elif 3751.05 <= salario_usuario < 4664.68:
        return salario_usuario * 0.225
    elif salario_usuario >= 4664.68:
        return salario_usuario * 0.275
    else:
        return 0


def transporte(salario_usuario, transporte):
    if transporte == 's':
        return salario_usuario * 0.06
    else:
        return 0


def vale_refeicao(refeicao):
    return refeicao * 0.20


def saude():
    return 150


while True:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        os.system("cls || clear")
        print("="*5," CADASTRO ","="*5)
        loginUsuario = input("Digite o login para cadastrar: ")
        senhaUsuario = int(input("Digite sua senha: "))
        os.system("cls || clear")

    if opcao == 2:
        os.system("cls || clear")
        print("="*5," S E N A I ","="*5)
        login = input("Digite seu login: ")
        senha = int(input("Digite sua senha: "))

        if login == loginUsuario and senha == senhaUsuario:
            os.system("cls || clear")
            print("="*5," S E N A I ","="*5)
            print("Bem Vindo(a) !!")
            time.sleep(2)
            os.system("cls || clear")

            salario_usuario, transporte_opcao, refeicao = informacoes()
            os.system("cls || clear")

            print("Exibindo os dados!! ")
            print("Aguarde....")
            time.sleep(2)
            os.system("cls || clear")
            
            print("="*5," S E N A I ","="*5)
            print("Login do Funcionário: {}".format(login))
            print("Senha do Usuário: {}\n".format(senha))

            desconto_inss = salario_inss(salario_usuario)
            desconto_irrf = salario_irrf(salario_usuario)
            desconto_transporte = transporte(salario_usuario, transporte_opcao)
            desconto_refeicao = vale_refeicao(salario_usuario)
            desconto_saude = saude()

            salario_final = salario_usuario - desconto_inss - desconto_irrf - desconto_transporte - desconto_refeicao - desconto_saude

            print("Salário Bruto: R$ {:.2f}".format(salario_usuario))
            print("Desconto INSS: R$ {:.2f}".format(desconto_inss))
            print("Desconto IRRF: R$ {:.2f}".format(desconto_irrf))
            print("Desconto Vale Transporte: R$ {:.2f}".format(desconto_transporte))
            print("Desconto Vale Refeição: R$ {:.2f}".format(desconto_refeicao))
            print("Desconto Plano de Saúde: R$ {:.2f}\n".format(desconto_saude))
            print("Salário Líquido: R$ {:.2f}".format(salario_final))

        else:
            os.system("cls || clear")
            print("Login e senha inválidos!! ")
            time.sleep(2)
            os.system("cls || clear")

    elif opcao == 3:
        os.system("cls || clear")
        print("Finalizando o programa...")
        time.sleep(3)
        break

