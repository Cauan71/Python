import os
import time
import random

# Crie um jogo de Advinhação de um número, o usuário terá de advinhar um número entre 1 e 100,
# O script te ajudar, ele avisa , se o número é MAIOR ou MENOR , ele vai ficar avisando
# quantas  chances você gastou até acertar.

def limpar():
    os.system("cls || clear")

contador = 0

limpar()

numeroSorteado = random.randint(1,100)

while True:
    valor = int(input("Digite um número: "))
    contador = contador + 1

    
    if numeroSorteado == valor:
        limpar()
        print("="*5 , "PARABÉNS", "="*5)
        print(f"Você realizou {contador} tentativas !!! ")
        print(f"O número Sorteado é {numeroSorteado}")
        break

    elif numeroSorteado < valor:
        print("MENOS")
        
    elif numeroSorteado > valor:
        print("Mais")
    
