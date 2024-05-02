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
    altura = float(input("Digite a altura do usuário (Ex: 1.75): "))
    peso = float(input("Digite o peso do usuário em KG : "))


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

    imc = pesos[i] / (alturas[i] ** 2)
    print(f"IMC do {i+1}ª Usuário(a):  {imc:.2f}")

    if imc < 18.5:
        print("Abaixo do peso")
    elif imc >= 18.5 and imc < 25:
        print("Peso Ideal")
    elif imc >= 25 and imc < 30:
        print("Sobrepeso")
    elif imc >=30 and imc < 35:
        print("Obesidade Grau 1")
    elif imc >=35 and imc <40:
        print("Obesidade Grau 2")
    else: 
        print("Obesidade Grau 3 ( Mórbida)")

    



    
