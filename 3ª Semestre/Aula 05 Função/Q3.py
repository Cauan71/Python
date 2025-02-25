import os

def limpar():
    os.system("cls || clear")

def calculo(salario):
    
    if salario < 280:
        rj = 0.20
        percentual = 20
        
    elif salario >= 280 and salario <700:
        rj = 0.15
        percentual = 15
        
    elif salario >=700 and salario < 1500:
        rj = 0.10
        percentual = 10
        
    else:
        rj = 0.05
        percentual = 5
    return rj, percentual

limpar()
salario_colab = float(input("Digite o seu salário: "))

rj, percentual = calculo(salario_colab)

valor_aumento = salario_colab*rj
novo_salario = salario_colab+valor_aumento



limpar()
print("===== MENU =====")
print(f"Salário Antes do Reajuste: {salario_colab:.1f}")
print(f"Percentual Aplicado: {percentual}%")
print(f"Valor do Aumento: {valor_aumento:.1f}")
print(f"Novo Salário: {novo_salario:.1f}")