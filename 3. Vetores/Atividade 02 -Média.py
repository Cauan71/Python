import os

os.system("cls || clear")

notas = []
soma: float = 0 
media: float = 0

for i in range(4):
    nota = float(input(f"Digite sua {i+1}ª Nota: "))
    notas.append(nota)

    soma = soma + nota
    media = soma/4



for i in range(len(notas)):
    print(f"{i+1}ª Nota: {notas[i]}")
print("Média:{:.2f}".format(media)) 


if media >= 7:
    print("Aprovado!! ")
elif media >=5 and media <7 :
    print("Em recuperação")
else:
    print("Reprovado!!")