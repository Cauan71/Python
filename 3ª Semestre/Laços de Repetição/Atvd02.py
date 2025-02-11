import os
import time
import random

def limpar():
    os.system("cls || clear")

nomes = []

limpar()
for i in range(10):
    nome = input(f"Digite o {i+1}ª Nome: ")
    nomes.append(nome)


nomeSorteado = random.choice(nomes)
limpar()
time.sleep(3)
print(f"Nome Sorteado : {nomeSorteado.capitalize}")