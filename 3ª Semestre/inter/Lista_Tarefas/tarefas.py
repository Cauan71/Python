import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

#  ------ Funções ------

def add_tarefas():
    t = str(tarefa.get())
    
    # Checando se a variável está vazia
    if(t):
        # Se o ( t )  existe, adicione o ( t ) no listbox na posição 0
        lista_tarefas.insert(0,t)
        tarefa.delete(0, 'end')
        salvar_tarefas()
        
    else:
        messagebox.showerror("[ERRO]", "O Campo de Tarefas está vazio!!!")
        
        

def del_tarefas():   
    selecionada = lista_tarefas.curselection() 
    
    if (selecionada):
        lista_tarefas.delete(selecionada)
        
    else:
        messagebox.showerror("[ERRO]","Selecione uma tarefa!!")
        

def salvar_tarefas():
    with open("tarefas.txt","w") as ta:
        tarefas = lista_tarefas.get(0, END)
        
        for x in tarefas:
            ta.write(x+"\n")
        

def carregar_tarefas():
    with open("tarefas.txt","r") as ta:
        tarefa = ta.readlines()
        
        for x in tarefa:
            lista_tarefas.insert(0,x.strip())
            
# ------ JANELA -------

janela = ctk.CTk()
ctk.set_appearance_mode("dark")

janela.title("Lista de Tarefas - Versão 1.0")
janela.iconbitmap("clipboard_notes_list_tasks_icon_191193.ico")
janela.configure(fg_color = "#00354e")
janela.resizable(False, False)
janela.geometry("600x400")



ctk.CTkLabel(janela, text="Lista de Tarefas", font=("Verdana", 22, "bold"), text_color="white").pack(pady=10)

# ----- Entry para o usuário digitar a tarefa

tarefa = ctk.CTkEntry(janela, width=350, height=30, border_color="lightblue", 
                            placeholder_text="Informe a tarefa a ser criada: ", 
                            font=("Verdana", 12 ))

tarefa.pack(pady=20)


# ------- Botão Adicionar ---------

btadicionar = ctk.CTkButton(janela, width=140, height=40, text="Adicionar Tarefa", 
                                text_color="black", fg_color="lightblue",cursor = "hand2", command= add_tarefas)

btadicionar.place(x=125, y = 115)

# ---- Botão Deletar ------------

btdeletar = ctk.CTkButton(janela, width=140, height=40, text="Deletar Tarefa", 
                                text_color="black", fg_color="#ee1414",hover_color="#6d0b0b",cursor = "hand2", command=del_tarefas)

btdeletar.place(x=335, y = 115)

#  ----- List Box - Lista de Tarefas

lista_tarefas = Listbox(janela, width=55, height=12, font=("Verdana", 12 ), background="#4c5357",highlightbackground="lightblue", highlightthickness=2, fg = "white")

lista_tarefas.place(x=30, y = 160)






janela.mainloop()
