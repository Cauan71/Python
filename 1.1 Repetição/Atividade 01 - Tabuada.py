import os

os.system("cls || clear")

num = int(input("Digite um número para gerar a tabuada: "))

os.system("cls || clear")

print("="*15)

for i in range(1,11):
    print("{} x {} = {} ".format(num , i , num*i))

print("="*15)
