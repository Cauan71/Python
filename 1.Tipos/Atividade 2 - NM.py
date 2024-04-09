import os

os.system("cls || clear")
soma = float = 0 
media = float = 0
multi = float = 0

nota1 = int(input("Digite a primeira Nota: "))
nota2 = int(input("Digite a segunda Nota: "))

soma = nota1+nota2
media = soma/2
multi = nota1*nota2

os.system("cls || clear")

print("====== M E N U ======")

print("Nota 1 : ",nota1)
print("Nota 2 : ",nota2)
print("Soma : ",soma)
print("Multiplicação : ",multi)
print("Média: ",media)


if nota1 > nota2:
    print("\nMaior Número: ",nota1)
elif nota2 > nota1:
    print("\nMaior Número: ",nota2)

if nota1 < nota2:
    print("\nMenor Número: ", nota1)
elif nota2 < nota1:
    print("\nMenor Número : ",nota2)

if nota1 == nota2:
    print("\nOs Números são iguais")

print("=================")