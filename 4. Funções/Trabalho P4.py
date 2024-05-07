import os
import time

class Reserva:
    def __init__(self, numero_aviao, nome_passageiro):
        self.numero_aviao = numero_aviao
        self.nome_passageiro = nome_passageiro

avioes = [None] * 4
assentos_disponiveis = [0] * 4
reservas = []

def registrar_avioes():
    print("Informe o número do Avião: ")
    for i in range(4):
        avioes[i] = input(f"Avião {i+1}: ")
        os.system("cls || clear")

def registrar_assentos_disponiveis():
    os.system("cls || clear")
    print("Informe a quantidade de assentos disponíveis para cada avião: ")
    for i in range(4):
        assentos_disponiveis[i] = int(input(f"Assento disponíveis para o avião {avioes[i]}: "))

def realizar_reserva():
    if len(reservas) >=10:
        os.system("cls || clear")
        print("Limites de reservas atingido!")
        return
    
    os.system("cls || clear")
    numero_aviao = input("Informe o número do avião: ")
    
    if numero_aviao not in avioes:
        os.system("cls || clear")
        print("Este avião não existe!")
        return
    
    indice_aviao = avioes.index(numero_aviao)
    if assentos_disponiveis[indice_aviao] == 0:
        os.system("cls || clear")
        print("Não há assentos disponíveis para este avião!")
        return
    
    nome_passageiro = input("Informe o nome do passageiro: ")
    reservas.append(Reserva(numero_aviao, nome_passageiro))
    assentos_disponiveis[indice_aviao] -=1
    os.system("cls || clear")
    print("Reserva realizada com sucesso! ")

def consulta_aviao():
    os.system("cls || clear")
    numero_aviao = input("Digite o número do avião que deseja consultar: ")

    if numero_aviao not in avioes:
        os.system("cls || clear")
        print("Esse avião não existe, tente novamente!!")
        return

    indice_aviao = avioes.index(numero_aviao)
    os.system("cls || clear")
    print("Avião:", numero_aviao)
    print("Assentos Disponíveis:", assentos_disponiveis[indice_aviao])

def consulta_passageiro():

    os.system("cls || clear")
    nome_passageiro = input("Digite o nome do passageiro que deseja consultar: ")

    localizar_passageiro = False
    
    for reserva in reservas:
        if reserva.nome_passageiro == nome_passageiro:
            os.system("cls || clear")
            print(f"O passageiro {nome_passageiro} está no avião {reserva.numero_aviao}")
            localizar_passageiro = True
        else:
            os.system("cls || clear")
            print(f"O passageiro {nome_passageiro} não possui reserva em nenhum avião!! ")


def menu():

    print("\n===== Menu Sweet Flight =====")
    print("\n1 . Registrar número de cada avião ")
    print("2. Registrar quantitativo de assentos disponíveis em cada avião ")
    print("3. Realizar passagem aérea")
    print("4. Realizar consulta por avião")
    print("5. Realizar consulta por passageiro")
    print("6. Encerrar")

while True:
    
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        registrar_avioes()
    
    elif opcao == 2:
        registrar_assentos_disponiveis()

    elif opcao == 3:
        realizar_reserva()
    
    elif opcao == 4:
        consulta_aviao()

    elif opcao == 5:
        consulta_passageiro()

    elif opcao == 6:
        os.system("cls || clear")
        print("Encerrando o programa...")
        time.sleep(3)
        break
    else:
        print("Opção Inválida !! Por favor, escolha uma opção válida.")





