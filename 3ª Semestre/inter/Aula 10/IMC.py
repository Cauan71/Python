import customtkinter as ctk



# ------------ Funções ------------

def calcular():
    p = int(peso.get())
    a = float(altura.get())
    # get() - traz os dados como String 
    #converter de String para int ou float
    
    imc = p/(a*a)
    
    if (imc < 18.5):
        resultado.configure(text=f"Sr(a) {nome.get()}, o seu IMC é {imc:.1f}\n Você está Magro(a)!! ",text_color = "orange")
    
    elif (imc >= 18.5 and imc < 25):
        resultado.configure(text=f"Sr(a) {nome.get()}, o seu IMC é {imc:.1f}\n Você está Saudável!! ",text_color = "green")
        
    elif (imc >= 25 and imc < 30):
        resultado.configure(text=f"Sr(a) {nome.get()}, o seu IMC é {imc:.1f}\n Você está com Sobrepeso!! ",text_color = "orange")
    
    else:
        resultado.configure(text=f"Sr(a) {nome.get()}, o seu IMC é {imc:.1f}\n Você está com OBESIDADE!! ",text_color = "RED")
        

def limpar():
    resultado.configure(text = "")
    nome.delete(0, 'end') #apagar o ctkEntry
    peso.delete(0, 'end')
    altura.delete(0, 'end')

# ----------- Interface Janela -------------

ctk.set_appearance_mode("dark")

janela = ctk.CTk()
janela.geometry("600x400")
janela.configure(fg_color = "beige")
janela.resizable(False, False)
janela.title("Aplicativo de Saúde")



# ----- Título Da Página -----
ctk.CTkLabel (janela,text="Aplicativo de Saúde",text_color = "black",
                font=("verdana",18,"bold")).pack(pady=10)


# 
nome = ctk.CTkEntry (janela, placeholder_text="Digite seu nome",placeholder_text_color="gray",font=("Arial",12),
                     width=300, height=30)
nome.pack(pady=20)

peso = ctk.CTkEntry (janela, placeholder_text="Digite o seu Peso",placeholder_text_color="gray",font=("Arial",12),
                     width=300,height=30)
peso.pack(pady=20)

altura = ctk.CTkEntry(janela,placeholder_text="Digite sua altura",placeholder_text_color="gray",font=("Arial",12),
                      width=300,height=30)
altura.pack(pady=20)


botao_calc = ctk.CTkButton(janela,text="Calcular",text_color="White",fg_color="blue",
                           height=35,width=130,command=calcular).place(x=140,y=270)

botao_limpar = ctk.CTkButton(janela,text="Limpar",text_color="white",fg_color="red",
                             height=35,width=130,command=limpar).place(x=300,y=270)



resultado = ctk.CTkLabel(janela,text="",text_color="black",font=("Verdana",18,"bold"))
resultado.place(x=160,y=330)


#python -m auto_py_to_exe 
# Localização do Script - Arquivo Python já feito
# Arquivo Único - Baseado em janelas 



janela.mainloop()