import os

# IMC
os.system("cls || clear")

peso = int(input("Digite seu peso: "))

altura = float(input("Digite sua altura: "))

imc = peso/(altura*altura)

os.system("cls || clear")

print("---- RESULTADO ----")
print(f"Seu IMC é: {imc:.2f}")

if (imc < 18.5 ):
    print("Abaixo do Peso")
elif ( imc >= 18.5 and imc < 24.9):
    print("Peso Normal")
elif(imc >=25 and imc <29.9):
    print("SobrePeso")
elif(imc <=30 and imc <34.9):
    print("Obesidade Grau I")
elif(imc <=35 and imc <39.9):
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III")