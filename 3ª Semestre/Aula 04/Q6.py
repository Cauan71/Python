import os
import random
import time

def limpar():
    os.system("cls || clear")
    
nomes = []    

limpar()
for i in range(10):
    nome = input("Digite um nome: ")
    nomes.append(nome)
    

nomeSorteado = random.choice(nomes)
limpar()
print("===== RESULTADO =====")
time.sleep(3)
print(f"Nome Sorteado: {nomeSorteado}")