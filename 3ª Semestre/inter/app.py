from tkinter import * 


def on_enter(e):
    button["background"] = "purple"

def on_leave(e):
    button["background"] = "white"



# Criação da Janela Principal
app = Tk()
app.title("Sistema de Login")
app.geometry("700x300")
app.configure(bg="#260436")

# Criação de Campo

# Usuário
text_usuario = Label(app, text="Usuário",font=("Arial", 12, "bold"),bg="#260436",fg="white")
text_usuario.pack(pady=10) 

entry_usuario = Entry(app,width=30,fg="gray")
entry_usuario.pack(pady=10)




# Senha
# fg = text_color
# bg = background-color

text_senha = Label(app, text="Senha",font=("Arial",12,"bold"),bg="#260436",fg="white")
text_senha.pack(pady=10)

entry_senha = Entry(app,show="*",width=30)
entry_senha.pack(pady=10)


# Button

button = Button(app, text="Clique Aqui",background="white",font=("Arial", 12, "bold"))
button.pack(pady=10)


# Adicionando evento hover

button.bind("<Enter>",on_enter)
button.bind("<Leave>",on_leave)

# Iniciar a aplicação
app.mainloop()


