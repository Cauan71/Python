import os

os.system("cls || clear")

nota = []

for i in range(3):
    nota = float(input(f"Digite sua {i+1}ª Nota: "))
    nota.append(nota)


for i in range(3):
    print(f"{i+1}ª Nota: {nota[i]}")
