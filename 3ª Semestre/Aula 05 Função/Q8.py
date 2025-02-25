import os
import time

def limpar():
    os.system("cls || clear")

lista = [7,8,3,4,5,6]
registro = [2,5,6,7,8,9]


limpar()
# SET - IMPEDE A DUPLICAÇÃO
lista3 = list(set(lista+registro))
print("Analisando.......")
time.sleep(3)
limpar()
print(f"Novos Números: {lista3}")
   