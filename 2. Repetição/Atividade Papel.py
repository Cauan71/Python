import os

os.system("cls || clear")

contador: int = 0 
menorIdade = 9999
maiorIdade = 0
somarSalario: float = 0
mediaSalario: float =0 
contadorSalario: int = 0

lista = []

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
            for i in range(lista):
        
                if idade[i] > maiorIdade:
                    maiorIdade = idade[i]
            
                if idade[i] < menorIdade:
                    menorIdade = idade[i]

       

            print(f"Média Salarial: {mediaSalario}")
            print(f"Maior Idade: {maiorIdade}")
            print(f"Menor Idade: {menorIdade}")
        
            if sexo == 'f' and salario > 5000:
                contador = contador + 1
            print("Quantidade de Mulheres com salário acima de R$ 5.000: {}".format(contador))
        
    if opcao == 3:
        os.system("cls || clear")
        print("Finalizando.....")
        break