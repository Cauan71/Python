#comando para limpar a tela
import os

os.system("clear")

#input = entrada p usuário
#solicitando os dados ao usuário

nome = input("Digite seu Nome: ")
idade = int(input("Digite sua Idade: "))
peso = float(input("Digite seu peso: "))

print(f"\n")

#resultado 
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso:.1f}")

#Verificar se é maior ou menor de Idade
if idade < 18 or idade >=65:
    print("Não Precisa votar")

else:
    print("Precisa Votar")