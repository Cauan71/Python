import os
import time
from dataclasses import dataclass


os.system("cls || clear")

@dataclass
class dados:
    nome: str
    autor: str
    categoria: str
    preco: float

livros = 3
armazenar = []

#
#
#

for i in range(livros):
    informacao = dados(
        nome = input("Digite o nome do Livro: "),
        autor = input("Digite o nome do autor: "),
        categoria = input("Digite a categoria "),
        preco = float(input("Digite o preço: "))

    )
    armazenar.append(informacao)

arquivo = "Catálogo_Livros.txt"

with open(arquivo , 'w') as arquivoDados:
    for informacao in armazenar:
        arquivoDados.write(f"{informacao.nome} -  {informacao.autor} - {informacao.categoria} = R$ {informacao.preco} ")

os.system("cls || clear")
print("Dados coletados com sucesso!! ")
time.sleep(2)
os.system("cls || clear")
