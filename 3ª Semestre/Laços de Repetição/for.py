import os 

os.system("cls || clear")

nomes = []
SIZE = 5

for i in range(SIZE):
    nome = input(f"Digite o {i+1}ª Nome: ")
    nomes.append(nome)


for i in range(len(nomes)):
    print(f"{i+1}ª Nome: {nomes[i]}")