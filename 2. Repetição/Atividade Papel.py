import os

os.system("cls || clear")

contador: int = 0 
menorIdade: int = 9999
maiorIdade: int = 0
somarSalario: float = 0
mediaSalario: float =0 
contadorSalario: int = 0

def menu():
    print("="*4 ," M E N U ", "="*4)
    print("1 - Adicionar ")
    print("2 - Exibir resultados ")
    print("3 - Sair ")

while True:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        idade = int(input("Digite sua idade: "))
        sexo = input("Digite seu sexo M ou F : ")
        salario = float(input("Digite seu salário: "))
        contadorSalario = contadorSalario + 1
        os.system("cls || clear")
        
    if opcao == 2:
        somarSalario = somarSalario + salario
        mediaSalario = somarSalario/contadorSalario
        print("Média Salarial: {}".format(mediaSalario))
        
        if idade > maiorIdade:
            maiorIdade = idade
            
        if idade < menorIdade:
            menorIdade = idade
            
        print("Maior Idade: ",maiorIdade)
        print("Menor Idade: ", menorIdade)
        
        if sexo == 'f' and salario > 5000:
            contador = contador + 1
        print("Quantidade de Mulheres com salário acima de R$ 5.000: {}".format(contador))
        
    if opcao == 3:
        os.system("cls || clear")
        print("Finalizando.....")
        break