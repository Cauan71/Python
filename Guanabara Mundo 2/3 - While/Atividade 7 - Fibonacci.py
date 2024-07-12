import os

os.system("cls || clear")

t1 = 0
t2 = 1

print("="*5," Sequência de Fibonacci ","="*5)
num = int(input("Quantos termos deseja inserir? "))
print("{} - {} ".format(t1,t2),end ="")

contador = 3 
while contador <= num:
    t3 = t1+t2
    print("- {} ".format(t3), end="")
    t1 = t2
    t2 = t3
    contador +=1