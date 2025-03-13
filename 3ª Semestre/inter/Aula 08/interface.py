from tkinter import *

def on_enter(e):
    button["background"] = "lightblue"
    
def on_leave(e):
    button["background"] = "gray"
    
janela = Tk()

janela.configure(bg="gray")
janela.geometry("500x300")
janela.title("Sistema de Login 2.0")


text_user = Label(janela,text="Usuário: ", bg="gray", font=("Arial", 12, "bold"),fg="white")
text_user.pack(pady=10)

user = Entry(janela, bg="gray", font=("Arial", 12, "bold"),fg="yellow",width=30)
user.pack(pady=10)

text_senha = Label(janela, text="Senha", bg="gray", font=("Arial", 12 , "bold"), fg="white")
text_senha.pack(pady=10)

senha = Entry(janela, show="*", font=("Arial",12, "bold"),width=30,bg="gray",fg="yellow")
senha.pack(pady=10)


button = Button(janela, bg="gray", font=("Arial", 12 ,"bold"), text="Entrar")
button.pack(pady=20)


button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

janela.mainloop()
