import os

os.system("cls || clear")

primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))

termo = primeiro
contador = 1
total = 0
adicionar = 10

while adicionar != 0 :
    total += adicionar
    while contador <= total:
        print("-> {}".format(termo), end="")
        termo += razao
        contador += 1
    adicionar = int(input("\nQuantos termos deseja inserir? "))
print("\nVocê inseriu {} termos nessa Progressão Aritmética !! ".format(total))
print("Fim")

