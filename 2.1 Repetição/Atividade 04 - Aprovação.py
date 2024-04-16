import os

os.system("cls || clear")
nota1 : int  = 11
nota2 : int = 11
nota3: int = 11


while nota1 <0 or nota1 > 10:
    nota1 = int(input("Digite a primeira nota: "))

while nota2 <0 or nota2 > 10:
    nota2 = int(input("Digite a segunda nota: "))

while nota3 < 0 or nota3 > 10:
    nota3 = int(input("Digite a terceira nota: "))


os.system("cls || clear")

soma = nota1+nota2+nota3
media = soma/3

print("="*15)
print("Soma: {}".format(soma))
print("Média: {}".format(media))

if media >=7:
    print("Aprovado!! ")
    print("="*15)
elif media >= 5 or media <7:
    print("Recuperação!!")
    print("="*15)
else:
    print("Reprovado!!")
    print("="*15)