import os
import time

def limpar():
    os.system("cls || clear")

lista = [1,2,3,4,5,6]
registro = [4,5,6,7,8,9]


limpar()

lista3 = list(set(lista+registro))

print(f"Novos Números: {lista3}")
   