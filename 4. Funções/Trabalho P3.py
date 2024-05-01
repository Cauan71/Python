import os

#Função sem retorno
def logoSenai():
    os.system("cls || clear")
    print("=== S E N A I ===")


#Definindo listas vazias para armazenar os dados dos usuários
nomes = []
idades = []
alturas = []
pesos = []
sobrenomes = []

#Solicitando os dados dos usuários em um loop 
while True:
    logoSenai()
    
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    #Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break

    sobrenome = input("Digite seu sobrenome do usuário : ")
    idade = int(input("Digite a idade do usuário : "))
    altura = float(input("Digite a altura do usuário : "))
    peso = float(input("Digite o peso do usuário : "))

    #Adicionando os dados ás listas
    nomes.append(nome)
    sobrenomes.append(sobrenome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)

#Exibindo os dados armazenados
logoSenai()
print("Dados dos Usuários: ")

for i in range(len(nomes)):
    print(f"\nUsuário {i+1}: ")
    print("Nome: ",nomes[i], sobrenomes[i])
    print("Idade: ",idades[i])
    print("Altura: ",alturas[i], "metros")
    print("Peso: ",pesos[i], "quilogramas")

    
