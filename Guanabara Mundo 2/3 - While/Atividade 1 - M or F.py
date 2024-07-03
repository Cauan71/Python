import os

os.system("cls || clear")

sexo = input("Digite seu sexo [ M / F]: ").upper()

while sexo not in "MmFf":
    sexo = str(input("Dados Inválidos. Informe novamente: ")).strip().upper()[0]
    

print("Sexo {} cadastrado !!".format(sexo))





