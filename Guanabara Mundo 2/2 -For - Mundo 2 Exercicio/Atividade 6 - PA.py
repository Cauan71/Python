import os

os.system("cls || clear")

print("===== Progressão Aritmética =====")
print("\t   10 Termos \t")
print("="*33)

termo1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
decimo = termo1 + (10-1) * razao

for i in range(termo1, decimo + razao , razao):
    print(i)

print("Fim")