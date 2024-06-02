import os


os.system("cls || clear")

valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite o valor do salário: "))
anos = int(input("Digite a quantidade de anos que irá pagar: "))

prestacao =  valor / (anos * 12)
minimo = salario * 30 / 100

if prestacao <= minimo:
    print("Empréstimo aprovado !!")
else:
    print("Empréstimo negado!! ")

print("Valor da Casa: {}".format(valor))
print("Quantidade de Anos: {}".format(anos))
print("Valor da Prestação : {:.2f}".format(prestacao))
print("Minimo: {}".format(minimo))
