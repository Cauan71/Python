from dataclasses import dataclass
import os

os.system("cls || clear")

def salvar(livros):
    arquivo = "Catálogo_Livros.txt"
    with open(arquivo , 'w') as arquivo:

        for Dados in livros:
            arquivo.write(f"{Dados.nome} , {Dados.autor}, {Dados.categoria}, {Dados.preco}\n")
        print("Dados salvos")

def exibir(arquivo):
    with open(arquivo, 'r') as arquivos:
        for linha in arquivos:
            nome, autor, categoria, preco = linha.strip().split(',')
            livros.append(Dados(nome=nome, autor=autor, categoria=categoria, preco=float(preco)))

    for i in livros:
        print(f"Nome: {i.nome}")
        print(f"Autor: {i.autor}")
        print(f"Categoria: {i.categoria}")
        print(f"Preço: {i.preco}")

QUANTIDADE_LIVROS = 1

@dataclass
class Dados:
    nome: str
    autor: str
    categoria: str
    preco: float

arquivo = "Catálogo_Livros.txt"
livros= []

print("Solicitando dados: ")
for i in range(QUANTIDADE_LIVROS):
    livro = Dados(
        nome = input("Digite o nome do livro : "),
        autor = input("Digite o autor: "),
        categoria = input("Digite a categoria: "),
        preco = float(input("Digite o preço: "))


    )
    livros.append(livro)

salvar(livros)

exibir(arquivo)