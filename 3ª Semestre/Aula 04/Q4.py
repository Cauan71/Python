import os

def limpar():
    os.system("cls || clear")
    
limpar()

nomes = []

for i in range(5):
    nome = input("Digite um nome: ").lower()
    nomes.append(nome)
    
nomes.sort()


limpar()
print("===== RESULTADO =====")
for i in range(5):
    print(f"{nomes[i]}")