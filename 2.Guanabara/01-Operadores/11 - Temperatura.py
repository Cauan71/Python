import os

os.system("cls || clear")

celsius = float(input("Digite a temperatura em Celsius °C : "))

conversao = float
conversao = celsius*1.8 + 32

print("Temperatura em Celsius {:.2f}°C , convertida em Fahrenheit {:.1f}°F ".format(celsius,conversao))