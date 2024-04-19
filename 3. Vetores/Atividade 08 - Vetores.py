import os

os.system("cls || clear")

notas = []

for i in range(3):
    nota = float(input(f"Digite sua {i+1}ª Nota: "))
    nota.append(nota)

print(f"Tamanh do Vetor: {len(nota)}")

for i in range(len(nota)):
    print(f"{i+1} Nota: {nota[i]}")