import os 

os.system("cls || clear")

nota : float = -1
soma : float = 0
quantidadeNotas = 0

while True:
    nota= float(input("Digite uma nota: "))
    
    resposta = input("Deseja continuar ?")


    if resposta == 's':
         soma += nota
         quantidadeNotas += 1
    else:
         break
    os.system("cls || clear")

media = soma / quantidadeNotas
print("Soma: {}".format(soma))
print(f"Média : {media}")

if media >=7:
    print("Aprovado!! ")
    print("="*15)
elif media >= 5 or media <7:
    print("Recuperação!!")
    print("="*15)
else:
    print("Reprovado!!")
    print("="*15)