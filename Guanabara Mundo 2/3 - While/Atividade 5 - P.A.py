import os

os.system("cls || clear")

print("="*5,"Termos P.A","="*5)
num = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))

contador = 1
#termo = num

while contador <= 10:
    print("{}".format(num)) #(TERMO)
    num += razao #termo += razao
    contador +=1
