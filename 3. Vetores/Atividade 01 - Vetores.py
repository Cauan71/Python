import os

os.system("cls || clear")

notas = []

for i in range(3):
    nota = float(input(f"Digite sua {i+1}ª Nota: "))
    notas.append(nota)

print(f"Tamanho do Vetor: {len(notas)}")

for i in range(len(notas)):
    print(f"{i+1} Nota: {notas[i]}")