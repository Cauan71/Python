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
    dependente = int(input("Digite a quantidade de dependentes: "))

    return salario_usuario, transporte, refeicao,dependente


def salario_inss(salario_usuario):
    if salario_usuario < 1100:
        return salario_usuario * 0.075
        
    elif salario_usuario <= 1100 and salario_usuario < 2203.48:
        return salario_usuario * 0.09
    
    elif salario_usuario <= 2203.48 and salario_usuario < 3305.22:
        return salario_usuario * 0.12
    
    elif salario_usuario <= 3305.22 and salario_usuario < 6433.57:
        return salario_usuario * 0.14
    
    else:
        return 854.36
    
def deducao_inss(salario_usuario):
    if salario_usuario >= 1100 and salario_usuario < 2203.48:
        return 21.18
    
    if salario_usuario >= 2203.48 and salario_usuario < 3305.22:
        return 101.18
    
    if salario_usuario >= 3305.22 and salario_usuario < 6433.57:
        return 181.18
    
    if salario_usuario < 1100:
        return 0


def salario_irrf(salario_usuario):
    
    if salario_usuario >= 2259.20 and salario_usuario < 2826.65:
       return salario_usuario * 0.075
    
    elif salario_usuario >= 2826.65 and salario_usuario < 3751.05:
        return salario_usuario * 0.15
    
    elif salario_usuario >= 3751.05 and salario_usuario < 4664.68:
        return salario_usuario * 0.225
    
    elif salario_usuario >= 4664.68:
        return salario_usuario * 0.275

    else: 
        return 0   

def deducao(salario_usuario):
    if salario_usuario >= 2259.20 and salario_usuario < 2826.65:
       return 169.44
    
    elif salario_usuario >= 2826.65 and salario_usuario < 3751.05:
        return 381.44
    
    elif salario_usuario >= 3751.05 and salario_usuario < 4664.68:
        return 662.77
     
    elif salario_usuario >= 4664.68:
        return 896
    else:
        return 0 

def dependentes(dependente):
    return dependente* 189.59


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

            salario_usuario, transporte_opcao, refeicao, dependente = informacoes()
            os.system("cls || clear")

            print("Exibindo os dados!! ")
            print("Aguarde....")
            time.sleep(2)
            os.system("cls || clear")
            
            print("="*5," S E N A I ","="*5)
            print("Login do Funcionário: {}".format(login))
            print("Senha do Usuário: {}\n".format(senha))

            desconto_inss = salario_inss(salario_usuario)
            desconto_deducao_inss = deducao_inss(salario_usuario)
            imposto_inss = salario_inss(salario_usuario) - deducao_inss(salario_usuario)

            desconto_irrf = salario_irrf(salario_usuario)
            desconto_deducao = deducao(salario_usuario)
            desconto_imposto = desconto_irrf - desconto_deducao
            valor_dependente = dependentes(dependente)

            desconto_transporte = transporte(salario_usuario, transporte_opcao)
            desconto_refeicao = vale_refeicao(refeicao)
            desconto_saude = saude()
            

            salario_final = salario_usuario - imposto_inss - desconto_imposto - desconto_transporte - desconto_refeicao - desconto_saude - valor_dependente

            print("Salário Bruto: R$ {:.2f}\n".format(salario_usuario))
            print("Desconto INSS: R$ {:.2f}".format(imposto_inss))
            print("Desconto IRRF R$ {:.2f}".format(desconto_imposto))
            print("Desconto Vale Transporte: R$ {:.2f}".format(desconto_transporte))
            print("Desconto Vale Refeição: R$ {:.2f}".format(desconto_refeicao))
            print("Desconto Plano de Saúde: R$ {:.2f}".format(desconto_saude))
            print("Valor por dependente: {:.2f}\n".format(valor_dependente))

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



