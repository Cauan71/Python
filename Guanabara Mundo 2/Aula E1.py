import os


os.system("cls || clear")

valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite o valor do salário: "))
anos = int(input("Digite a quantidade de anos que irá pagar: "))

tempo = anos * 12
taxa = 0.3

pagamento_mensal = valor / tempo
porcentagem = salario * taxa 



os.system("cls || clear")
print("===== Curso em Vídeo =====")

if pagamento_mensal > porcentagem:
    print("Empréstimo foi reprovado !! ")
else: 
    print("Parabéns, Empréstimo foi aprovado!! ")

print("Valor da Casa: {}".format(valor))
print("Quantidade de Anos : {}".format(anos))
print("Salário do Usuário : {}\n".format(salario))
print("Pagamento Mensal : {:.2f}".format(pagamento_mensal))
print("Valor Máximo que o usuário conseguirá pagar: {}".format(porcentagem))
