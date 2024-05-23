from dataclasses import dataclass
import os
import time

def salvar(lista):
    arquivo = "Funcionarios.txt"
    with open(arquivo, 'w') as arquivo:

        for Dados in lista:
            arquivo.write(f"{Dados.nome} , {Dados.data_nascimento}, {Dados.rg}, {Dados.cpf} \n")
        print("Dados do(s) Usuário(s) Salvos!! ")

def exibir(arquivo):
    with open(arquivo, 'r') as arquivos:
        for linha in arquivos:
            nome, data_nascimento, rg, cpf = linha.strip().split(',')
            lista_exibir.append(Dados(nome= nome, data_nascimento= data_nascimento, rg= int(rg), cpf= int(cpf)))

        for i in lista_exibir:
            print("="*5, "Usuário", "="*5)
            print(f"Nome: {i.nome}")
            print(f"Data de Nascimento: {i.data_nascimento}")
            print(f"RG: {i.rg}")
            print(f"CPF: {i.cpf}\n")






@dataclass
class Dados:
    nome: str
    data_nascimento: str
    rg: int
    cpf: int

os.system("cls || clear")

arquivo = "Funcionarios.txt"
QUANTIDADE_USUARIOS = 5
lista = []
lista_exibir = []

for i in range(QUANTIDADE_USUARIOS):
    print("="*5, "S E N A I ", "="*5)
    inf = Dados(
        nome = input("Digite seu nome: "),
        data_nascimento = str(input("Digite sua data de nascimento: ")),
        rg = int(input("Digite seu RG: ")),
        cpf = int(input("Digite seu CPF: "))
    )
    lista.append(inf)
    os.system("cls || clear")

salvar(lista)
time.sleep(2)
os.system("cls || clear")
exibir(arquivo)