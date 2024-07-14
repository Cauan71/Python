import os

os.system("cls || clear")

while True:
    num = int(input("\nDigite um número para tabuada: "))
    os.system("cls || clear")

    if num < 0 :
        break
    
    for i in range(1,11):
        print("{} x {} = {}".format(num, i, num*i))
print("Fim do Programa ;) !! ")