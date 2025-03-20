# 25% de (qtd horas da matéria)

# Resultado em dias = 4 horas

import customtkinter as ctk
from tkinter import messagebox

from tkinter import messagebox

def calcular(): 
    carga_horaria = int(ch.get())  
    ft = int(faltas.get())  
    

    total_faltas_permitidas = carga_horaria * 0.25
    
   
    if ft == total_faltas_permitidas:
     
        horas_restantes = carga_horaria - (total_faltas_permitidas * carga_horaria / 100)
        return messagebox.showinfo("APP Calculadora de Faltas", f"Você não pode mais faltar, você tem {horas_restantes} horas para faltar.")
    
   
    elif ft > total_faltas_permitidas:
        return messagebox.showinfo("App Calculadora de Faltas", "Você está reprovado")
    
   
    else:
    
        horas_restantes = total_faltas_permitidas - ft
        porcentagem_restante = (horas_restantes * 100) / carga_horaria
        
        dias_restantes = horas_restantes / 2 
        return messagebox.showinfo(
            "APP Calculadora de Faltas",
            f"Você ainda tem {horas_restantes} horas de faltas disponíveis, o que corresponde a {porcentagem_restante:.2f}% de horas disponíveis. "
            f"Você tem {dias_restantes:.2f} dias restantes para faltar."
        )


ctk.set_appearance_mode("dark")


janela = ctk.CTk()
janela.geometry("500x400")
janela.resizable(False, False)
janela.configure(fg_color="black") #a9a9a9
janela.title("Calculadora de Faltas")
janela.iconbitmap("3069198-cap-education-hat-school_112714.ico")


ctk.CTkLabel(janela, text="Calculadora de Faltas", text_color="white",font=("Verdana",16,"bold")).pack(pady=10)

ctk.CTkLabel(janela, text="Carga Horária", text_color="White", font=("Verdana", 16, "bold")).pack(pady=10)

ch = ctk.CTkEntry(janela, placeholder_text="Informe a carga horária da matéria: ", placeholder_text_color="gray", font=("Verdana", 12),width=300)

ch.pack(pady=10)

ctk.CTkLabel(janela, text="Horas de Faltas", text_color="white", font=("Verdana", 16,"bold")).pack(pady=10)

faltas = ctk.CTkEntry(janela, placeholder_text="Informe a quantidade de Faltas em Horas: ", placeholder_text_color="gray", width=300)

faltas.pack(pady=10)

# ---------------------- BOTÃO --------------

botao = ctk.CTkButton(janela,text="Calcular", command=calcular,font=("Verdana",14,"bold"),width=100,height=30)

botao.pack(pady=20)









janela.mainloop()

