import os

os.system("cls || clear")

def menu():
    os.system("cls || clear")
    print("===== S E N A I =====")

def somar(n1,n2):
    resultado = n1+n2
    return resultado

def multiplicar(n1,n2):
    resultado = n1*n2
    return resultado

def dividir(n1,n2):
    resultado = n1/n2
    return resultado

def diminuir(n1,n2):
    resultado = n1-n2
    return resultado

menu()
primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))

soma = somar(primeiroNumero,segundoNumero)
multiplicacao = multiplicar(primeiroNumero,segundoNumero)
divisao = dividir(primeiroNumero,segundoNumero)
subtracao = diminuir(primeiroNumero,segundoNumero)

menu()
print("Soma: {}".format(soma))
print("Subtração: {}".format(subtracao))
print("Divisão: {}".format(divisao))
print("Multiplicação: {}".format(multiplicacao))
