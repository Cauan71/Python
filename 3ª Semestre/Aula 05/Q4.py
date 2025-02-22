import os

def limpar():
    os.system("cls || clear")

def calculo(nt):
    total = soma / SIZE
    return total



lista = []
SIZE = 5

limpar()
for i in range(SIZE):
    print("===== NOTAS =====")
    nota = int(input(f"Digite a {i+1}ª Nota: "))
    lista.append(nota)
    limpar()

    soma = sum(lista)


total = calculo(nota)

limpar()
print("===== MENU =====")
print(f"Soma das Notas: {soma}")
print(f"Média das Notas: {total}")