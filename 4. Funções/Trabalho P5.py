import os
import time

os.system("cls || clear")

inss: float
irrf: float
transporte_desconto: float
ticket: float
plano_saude: float
salario_final: float 

def menu():
    print("="*5," M E N U ", "="*5)
    print("1 - Cadastrar Login e Senha Funcionário")
    print("2 - Entrar no Sistema ")
    print("3 - Sair do programa ")
    
def informacoes():
    print("="*5," S E N A I ","="*5)
    salario_usuario = float(input("Digite seu Salário Base : "))
    transporte = input("Deseja receber o Vale Transporte ( s / n ) ?")
    refeicao = float(input("Digite o valor do vale refeicao fornecido: "))
    
    
def salario_inss(salario_usuario):
    
    if salario_usuario < 1100:
        inss = salario_usuario - ( salario_usuario * 0.075)
        
    elif salario_usuario >= 1100 or salario_usuario < 2203.48:
        inss = salario_usuario - ( salario_usuario * 0.09)
        
    elif salario_usuario >= 2203.48 or salario_usuario < 3305.22:
        inss = salario_usuario - ( salario_usuario * 0.12)
        
    elif salario_usuario >= 3305.22 or salario_usuario < 6433.57:
        inss = salario_usuario - ( salario_usuario * 0.14)
        
        
def salario_irrf(salario_usuario):
    
    if salario_usuario >= 1903.98 or salario_usuario < 2826.65:
        irrf = salario_usuario - ( salario_usuario * 0.075)
        
    elif salario_usuario >= 2826.65 or salario_usuario < 3751.05:
        irrf = salario_usuario - (salario_usuario * 0.15)
    
    elif salario_usuario >= 3751.05 or salario_usuario < 4664.68:
        irrf = salario_usuario - ( salario_usuario* 0.225)
    
    elif salario_usuario >= 4664.68:
        irrf = salario_usuario - ( salario_usuario * 0.275)
        
    return irrf
        
    
def transporte(salario_usuario):
    if transporte == 's':
        transporte_desconto = salario_usuario - ( salario_usuario * 0.06)
        
    return transporte_desconto
    
def vale_refeicao(salario_usuario):
    ticket = salario_usuario - ( salario_usuario * 0.20)
    
    
    
def saude(salario_usuario):
    plano_saude = salario_usuario - 150
    
    
    
    
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
            
            informacoes() 
            os.system("cls || clear")
            
            print("Exibindo os dados!! ")
            print("Aguarde....")
            time.sleep(2)
            
            print("Login do Funcionário: {}".format(login))
            print("Senha do Usuário: {}\n".format(senha))
            salario_inss(salario_usuario)
            
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
        

    
