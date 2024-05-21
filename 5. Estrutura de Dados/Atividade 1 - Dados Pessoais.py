import os
from dataclasses import dataclass
import time

os.system("cls || clear")

@dataclass
class informacoes:
    nome: str
    idade : int
    peso: float
    altura: float

quantidade = 2
coletar = []

    
for i in range(quantidade):
    dados = informacoes(
        nome = input("Digite seu nome: "),
        idade = int(input("Digite sua idade: ")),
        peso = float(input("Digite seu peso: ")),
        altura = float(input("Digite sua altura: "))
    )
    coletar.append(dados)

arquivo = "dados_pessoais.txt"

with open(arquivo, "w") as arquivoDeDados:
    for dados in coletar:
        arquivoDeDados.write(f"{dados.nome}, {dados.idade} , {dados.peso} , {dados.altura}\n")
os.system("cls || clear")
print("Dados coletados com sucesso..")
time.sleep(2)
os.system("cls || clear")