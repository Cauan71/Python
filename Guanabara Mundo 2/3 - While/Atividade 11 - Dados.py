import os

os.system("cls || clear")

cont_idade = cont_mulher = cont_homem = 0
sexo = "F"

while True:
    nome = str(input("\nDigite seu nome: "))
    idade = int(input("Digite sua idade: "))

    while sexo not in "MF":
        sexo = str(input("Informe seu sexo [ M / F ]: ")).upper().strip()[0]
        

    if idade >= 18:
        cont_idade += 1
    if sexo == "M":
        cont_homem
    if sexo == "F" and idade < 20:
        cont_mulher += 1

    opcao = ''

    while opcao not in "SN":
        opcao = str(input("Deseja continuar? [ S / N ]: "))

    if opcao == "N":
        break

print("Pessoas acima de 18 anos: {}".format(cont_idade))
print("Homens Cadastrados: {}".format(cont_homem))
print("Mulheres abaixo de 20 anos: {}".format(cont_mulher))

