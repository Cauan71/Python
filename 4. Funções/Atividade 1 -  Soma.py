import os

os.system("cls || clear")

def menu():
    os.system("cls || clear")
    print("===== S E N A I =====")
    
def conta(n1,n2):
    somar = n1+n2
    resultado = somar/2
    return resultado
    
primeiroNumero = int(input("Digite o Primeiro Número: "))
segundoNumero = int(input("Digite o Segundo Número: "))

media = conta(primeiroNumero,segundoNumero)

print("Média: {:.1f}".format(media))

