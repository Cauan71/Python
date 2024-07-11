import os 

os.system("cls || clear")

num = int(input("Digite um número: "))
c = num
fat = 1 

while c > 0:
    print("{}".format(c))
    print(" x " if c > 1 else "=", end="")
    fat*= c
    c -= 1

print("{}".format(f))

