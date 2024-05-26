import random
import os

os.system("cls || clear")


n1 = str(input("Digite o primeiro nome: "))
n2 = str(input("Digite o segundo nome: "))
n3 = str(input("Digite o terceiro nome: "))
n4 = str(input("Digite o quarto nome: "))

lista = [n1,n2,n3,n4]

escolhido = random.choice(lista)

#print("Aluno(a) escolhido(a): {}".format(escolhido))


#embaralhar ordem dos alunos

random.shuffle(lista)
print("Ordem de Apresentação: ")
print(lista)

