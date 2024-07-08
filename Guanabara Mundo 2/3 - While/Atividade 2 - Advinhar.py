import os
from random import randint


os.system("cls || clear")

computador = randint(0,10)

acertou = False
palpites = 0

while not acertou:
    jogador = int(input("Qual é seu palpite? "))
    palpites += 1

    if jogador == computador:
        acertou = True
    else:
        if jogador < computador :
            print("Um pouco mais, Tente Novamente...")
        elif jogador > computador:
            print("Um pouco menos, Tente Novamente..")
print("Acertou com {} tentativas. Parabéns !".format(palpites))
