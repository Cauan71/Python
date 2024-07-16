import os

os.system("cls || clear")

cont_idade = cont_homem = cont_mulher = 0 

while True:

    print("="*5, " Curso em Vídeo ", "="*5)
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo [ M / F ]: ")).upper().strip()[0]
    opcao = str(input("Deseja continuar [ S / N ]: ")).upper().strip()[0]

    os.system("cls || clear")

    if idade > 18:
        cont_idade += 1

    if sexo == "M":
        cont_homem += 1

    if sexo == "F" and idade < 20:
        cont_mulher += 1

    if opcao == "N":
        break

print("="*5, " Curso em Vídeo ", "="*5)
print("Pessoas acima de 18 anos: {} ".format(cont_idade))
print("Homens cadastrados: {} ".format(cont_homem))
print("Mulheres abaixo de 20 anos: {} ".format(cont_mulher))
