import os

os.system("clear || cls")

#forçando a variável a entrar no while
nota =11

soma : float = 0
media: float = 0

while nota <0 or nota > 10:
    for i in range(1,3):
        nota = float(input("Digite sua {}ª Nota: ".format(i)))
        soma += nota      
        
        media = soma/i
        

print("Soma: {}".format(soma))
print("Média: {}".format(media))