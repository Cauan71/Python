import customtkinter as ctk
from tkinter import messagebox


def calcular():
    value = float(valor.get())
    
    conversao = value/5.67
    
    
    messagebox.showinfo("Conversor de Moeda",f"O Valor R$ {value} convertido para Dólar fica: US$ {conversao:.2f}")
    


ctk.set_appearance_mode("dark")

# --------------------------------------------

janela = ctk.CTk()
janela.configure(fg_color = "#0b111b")
janela.geometry("450x350")
janela.resizable(False, False)
janela.iconbitmap("Conversor/coin_money_icon-icons.com_51091.ico")
janela.title("Sistema de Conversão de Moedas")

# --------------------------------------------

# Inicio
ctk.CTkLabel(janela,text="Conversão de Moedas", text_color="white", font=("Verdana", 20, "bold")).pack(pady=10)


ctk.CTkLabel(janela,text="Valor em Real", font=("Verdana", 12, "bold")).place(x=20, y=100)


valor = ctk.CTkEntry(janela,placeholder_text="Informe o valor: ", placeholder_text_color="gray",
             text_color="white",width=300, height=30)

valor.place(x=20, y=140)


botao = ctk.CTkButton(janela,text="Calcular",hover_color="green",width=150,command=calcular, height=35).place(x=150,y=250)

janela.mainloop()