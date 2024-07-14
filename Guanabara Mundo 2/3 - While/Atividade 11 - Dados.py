import os

os.system("cls || clear")

contador_idade = 0
contador_sexo = 0
mulheres_cont = 0

opcao = "S"

while opcao == "S":
    print("="*5,"Curso em Vídeo","="*5)
    nome = str(input("\nDigite seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo [ M / F ]: ")).upper().strip()[0]

    opcao = str(input("Deseja continuar [ S / N ]? ")).upper().strip()[0]
    
    os.system("cls || clear")

    if idade > 18:
        contador_idade += 1

    if sexo == "M":
        contador_sexo += 1

    if sexo == "F" and idade < 20:
        mulheres_cont += 1 

print("="*5," RESULTADO ", "="*5)
print("Pessoas com mais de 18 anos: {}".format(contador_idade))
print("Quantidade Homens cadastrados: {}".format(contador_sexo))
print("Quantidade de mulheres abaixo de 20 anos: {}".format(mulheres_cont))
