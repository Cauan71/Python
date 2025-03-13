from tkinter import *

def on_enter(e):
    botao["background"] = "#109e7f"
    
def on_leave(e):
    botao["background"] = "#14cca4"



viagem = Tk()
viagem.geometry("600x450")
viagem.configure(bg="#161414")
viagem.title("APP Gasolina 2025")
viagem.resizable(False, False)


inicio_text = Label(viagem, text="APP Gasolina 2025", fg="white", bg="#161414", font=("Arial", 16 , "bold"))
ic_text = Label(viagem, text="03/2025 - Senai Bahia", font=("Arial", 14), bg="#161414", fg="white")

inicio_text.pack(pady=5) 
ic_text.pack(pady=0)

# Distância

distancia = Label(viagem, text="Distância: ",font=("Arial",14,"bold"),fg="white",bg="#161414")
distancia.pack(pady=10)

dig_distancia = Entry(viagem,font=("Arial", 12), fg="black",bg="white",width=40)
dig_distancia.pack(pady=10)


# Consumo

consumo = Label(viagem, text="Consumo: ",anchor="w", fg="white",bg="#161414", font=("Arial",14,"bold"))
consumo.pack(pady=10)

dig_consumo = Entry(viagem,fg="black", font=("Arial", 12),width=40)
dig_consumo.pack(pady=10)

# Preço

preco = Label(viagem, text="Preço: ", bg="#161414", fg="white", font=("Arial", 14, "bold"))
preco.pack(pady=10)

dig_preco = Entry(viagem, fg="black", font=("Arial", 12),width=40)
dig_preco.pack(pady=10)

# Botão

botao = Button(viagem,text="Calcular o Valor da Viagem", fg="black", font=("Arial", 14, "bold"),bg="#14cca4")
botao.pack(pady=20)


botao.bind("<Enter>", on_enter)
botao.bind("<Leave>", on_leave)

viagem.mainloop()