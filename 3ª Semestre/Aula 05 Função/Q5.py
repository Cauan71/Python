import os

def limpar():
    os.system("cls || clear")

limpar()


num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

# Determinando qual o MENOR e MAIOR número: 
inicio = min(num1,num2) 
fim = max(num1, num2)

limpar()
# Exibindo Resultado
print(f"Números entre {inicio} e {fim}: ")
for i in range(inicio +1, fim):
    print(i, end= " ")

