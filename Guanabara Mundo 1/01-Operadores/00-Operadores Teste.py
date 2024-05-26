# Operadores Aritméticos :

# + Soma 
# - Subtração
# * Multiplicação
# / Divisão
# ** Potência
# // Divisão Inteira
# % Resto da Divisão

# Ordem de Procedência

# 1 = () 
# 2 = **
# 3 = * , / , // , %
# 4 = + , - 

import os

os.system("cls || clear")


num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

soma = num1+num2
subtracao = num1 - num2
multiplicacao = num1*num2
divisao = num1/num2
potencia = num1**num2
resto = num1%num2
inteira = num1//num2

print("Soma: ",soma)
print("Subtração: ",subtracao)
print("Multiplicação: ",multiplicacao)
print("Divisão: ",divisao)
print("Potência: ",potencia)
print("Resto da Divisão: ",resto)
print("Divisão Inteira: ",inteira)

