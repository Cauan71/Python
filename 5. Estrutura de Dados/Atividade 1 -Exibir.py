from dataclasses import dataclass
import os

os.system("cls || clear")

@dataclass
class informacoes:
    nome: str
    idade: int
    peso: float
    altura: float

arquivo = "dados_pessoais.txt"

coletar= []

with open(arquivo , 'r') as arquivos:
    for linha in arquivos:
        nome, idade, peso, altura = linha.strip().split(',')
        coletar.append(informacoes(nome = nome, idade = int(idade), peso = float(peso) , altura = float(altura)))

print("\nExibindo Dados")
for i in coletar:
    print("===== Usuário =====")
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")
    print(f"Peso: {i.peso}")
    print(f"Altura: {i.altura}\n")