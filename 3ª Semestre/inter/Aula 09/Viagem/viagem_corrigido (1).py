import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

# Função para realizar o cálculo
# Quando o botao for acionado

# ---------- FUNÇÕES ------------
def calculo():
    # get() vem como uma String - Converter para float, int ou double
    d =int(distancia.get())
    c = int(consumo.get())
    p = float(preco.get())
    
    formula = (d/c)*p
    
    messagebox.showinfo("APP Gasolina",f"O Valor gasto para essa Viagem será de: R$ {formula:.2f}")

    
# ---------------------------------------------------------



ctk.set_appearance_mode('dark')

#----------- Interface Janela -----------

viagem = ctk.CTk()
viagem.geometry("570x500")
viagem.configure(fg_color = "beige")
viagem.resizable(False, False) #largura, altura
viagem.title("Sistema de Consumo de Gasolina")
viagem.iconbitmap('Viagem/biofuel_fuel_station_petrol_green_energy_ecology_icon_191926.ico')

# ---------------------------------------

# CTkEntry() = Cria a caixa
# CTkLabel() = Cria o Texto
# CTkButton = Cria o Botão

# Títulos
ctk.CTkLabel(viagem, text="APP Viagem Consumo", text_color='black',
            font=("verdana",30,"bold")).pack(pady=10)

ctk.CTkLabel(viagem, text="03/2025 - Senai Bahia", text_color='black',
            font=("verdana", 20)).pack(pady=10)

# Inicializadores ( Place / Pack )

# Distância
ctk.CTkLabel(viagem,text="Distância:",text_color="black",
             font=("verdana", 16,"bold")).place(x=20, y=120 )

distancia = ctk.CTkEntry(viagem, width=400,
                         height=30,placeholder_text="Informe a Distância em KM",placeholder_text_color="gray")

# Com variável NÃO utilizar a concatenação, sempre fora dos ajustes 
distancia.place(x=20, y=150)


# Consumo

ctk.CTkLabel(viagem, text="Consumo: ", text_color="Black", font=("verdana", 16, "bold")).place(x=20, y=210)

consumo = ctk.CTkEntry(viagem,height=30, width=400, placeholder_text="Informe o Consumo em LT",
                       placeholder_text_color="gray")

consumo.place(x=20, y=250)

#  Preço

ctk.CTkLabel(viagem, text="Preço: ", text_color="black", font=("verdana", 16, "bold")).place(x=20, y=296)

preco = ctk.CTkEntry(viagem, placeholder_text="Informe o Preço em R$ ", placeholder_text_color="gray",
                     width=400, height=30)

preco.place(x=20, y=330)

# Botão

botao = ctk.CTkButton(viagem, text="Calcular",fg_color="green", text_color="white",width=150,
                      height=35,command=calculo, hover_color="darkgreen").place(x=200, y=400)


viagem.mainloop()