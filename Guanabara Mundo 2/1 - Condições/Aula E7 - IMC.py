import os

os.system("cls || clear")

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

os.system("cls || clear")
print("="*5, " Curso em Vídeo ", "="*5)
print("Dados do Usuário: ")
print("Nome: {}".format(nome))
print("Imc: {:.2f}".format(imc))

if imc < 18.5:
    print("Abaixo do Peso")
elif imc >= 18.5 and imc < 25:
    print("Peso Ideal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30 and imc < 40:
    print("Obesidade ")
elif imc >= 40:
    print("Obesidade Mórbida")
