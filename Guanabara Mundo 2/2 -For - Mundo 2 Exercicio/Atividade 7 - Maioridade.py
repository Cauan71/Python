import os
from datetime import date
os.system("cls || clear")

cont_maior:int = 0 
cont_menor:int = 0
data_atual = date.today().year

for i in range(7):

    ano = int(input(f"Digite o ano da {i+1}ª pessoa: "))
    idade = data_atual - ano 

    if idade >=18:
        cont_maior += 1
    else:
        cont_menor += 1

print("\nPessas com Maior Idade: {}".format(cont_maior))
print("Pessas com Menor Idade: {}".format(cont_menor))
