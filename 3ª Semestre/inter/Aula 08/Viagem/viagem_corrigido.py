import customtkinter as ctk
from tkinter import * 


ctk.set_appearance_mode('dark')

#----------- Interface Janela -----------

viagem = ctk.CTk()
viagem.geometry("600x450")
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





viagem.mainloop()