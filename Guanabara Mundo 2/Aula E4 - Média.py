import os

os.system("cls || clear")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

os.system("cls || clear")

print("===== RESULTADO ===== ")
print("Média do aluno: {:.1f}".format(media))

if media < 5:
    print("Reprovado(a) !!")
elif media >=5 and media < 7:
    print("Em recuperação!! ")
else: 
    print("Aprovado(a)!! ")