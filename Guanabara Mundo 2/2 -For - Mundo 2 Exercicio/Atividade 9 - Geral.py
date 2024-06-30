import os

os.system("cls || clear")
soma:int = 0 
media:int = 0 
maior_idade_homem :int = 0
nome_velho = ''
contador_mulher: int = 0

for i in range(1,5):
    print(f"\n===== {i}ª Pessoa =====")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Sexo [M / F]: ").upper()

    soma = soma + idade
    media = soma / i

    if i == 1 and sexo in 'Mm':
        maior_idade_homem = idade 
        nome_velho = nome
    
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome 



    if sexo == "F" and idade < 20:
        contador_mulher = contador_mulher + 1


print("\nMédia de Idade: {}".format(media))
print("Mulheres abaixo de 20 Anos: {}".format(contador_mulher))
print("{} é o homem mais velho , e tem {} anos ".format(nome_velho, maior_idade_homem))




