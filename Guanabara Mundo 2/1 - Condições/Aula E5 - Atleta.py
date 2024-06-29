import os

from datetime import date
ano_atual = date.today().year

os.system("cls || clear")

ano_nascimento = int(input("Digite o seu ano de nascimento: "))

idade_usuario = ano_atual - ano_nascimento

print("O atleta tem {} anos ".format(idade_usuario))

if idade_usuario <= 9 :
    print("Mirim")
elif  idade_usuario > 9 and idade_usuario <= 14:
    print("Infantil")

elif idade_usuario > 14 and idade_usuario <= 19:
    print("Júnior")

elif  idade_usuario > 19 and idade_usuario <= 25:
    print("Sênior")

elif idade_usuario > 25:
    print("Master ")

