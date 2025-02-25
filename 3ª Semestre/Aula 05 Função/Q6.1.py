import os

def limpar():
    os.system("cls || clear")

limpar()
qt_eleitores = int(input("Digite a quantidade de eleitores: "))

candidato1 = 0
candidato2 = 0
candidato3 = 0

limpar()

for i in range(qt_eleitores):
    limpar()
    print("="*5, " CANDIDATOS ", "="*5)
    print("1 - Candidato 1")
    print("2 - Candidato 2 ")
    print("3 - Candidato 3")
    voto = int(input("Escolha sua opção: "))

    if voto == 1:
        candidato1+= 1

    elif voto == 2:
        candidato2+= 1

    elif voto == 3:
        candidato3+= 1
    
    else:
        print("Digite uma opção válida")
    
    limpar()

limpar()
print("===== RESULTADO ===== ")
if candidato1 > candidato2 and candidato1> candidato3:
    print(f"Vencedor da Eleição foi Candidato 1 com {candidato1} votos")
 
elif candidato2 > candidato1 and candidato3:
    print(f"Vencedor da Eleição foi o Candidato 2 com {candidato2} votos")

elif candidato3 > candidato1 and candidato2:
    print(f"Vencedor foi o Candidato 3 com {candidato3} votos")

else:
    print("Houve um Empate entre os Candidatos")