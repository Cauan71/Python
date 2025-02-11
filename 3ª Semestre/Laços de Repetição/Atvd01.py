import os
import time

def limpar():
    os.system("cls || clear")

# Crie um Script que recebe vários nomes, e só para quando receber a palavra "Exit", ao Sair o Script imprime somente as pessoas que começam com a letra A

registro = []

while True:
    nome = input("Digite seu nome: ").lower() 
    # lower - para converter o nome sempre para minusculo
    # Upper - "" "" "" maiúsculo

    if ( nome == "exit"):
        print("Finalizando...")
        time.sleep(2.5)
        break
    else:
        registro.append(nome)

limpar()
print("="*5 , "Resultado" , "="*5)
for i in registro:
    if i.startswith("a"):
        print(i.capitalize())
        # capitalize  - para APENAS a primeira letra ser maiúscula

        