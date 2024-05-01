import os

def menu():
    os.system("cls || clear")
    print("===== S E N A I =====")

def notas(n1,n2):
    somar = n1+n2
    media = somar/2

    if media >=7:
        print("Aprovado!! ")
    elif media <5:
        print("Reprovado!!")
    else:
        print("Em recuperação!!")

    return media
   
menu()
nota1 = float(input("Digite a primeira Nota: "))
nota2 = float(input("Digite a segunda Nota: "))

menu()
media = notas(nota1, nota2)
print("Média do Aluno: {:.1f}".format(media))
