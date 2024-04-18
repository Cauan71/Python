import os

os.system("cls || clear")
soma: float = 0
nota: float = 0
contador: int = 0
media : float = 0 

while True:
    nota= float(input("Digite uma nota: "))

    if nota > 0:
        soma += nota
        contador = contador + 1

    else:
        media = soma/contador
        print("Média do Aluno: {}".format(media))
        break