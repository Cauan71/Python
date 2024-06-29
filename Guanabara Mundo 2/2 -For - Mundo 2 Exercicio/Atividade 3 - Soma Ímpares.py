import os

os.system("cls || clear")
soma:int =0 
contador:int = 0 

for i in range(1,500,2):
    if i % 3 == 0:
       contador = contador + 1
       soma += i

print("Números contidos: {}".format(contador))
print("Soma Total: {}".format(soma))