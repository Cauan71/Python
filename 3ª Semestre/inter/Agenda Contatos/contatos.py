import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

def add_contato():
    n = nome.get()
    t = telefone.get()
    e = email.get()
    
    if n and t and e:
        contato_format = (f"Nome: {n} / Telefone: {t} / E-mail: {e}")
        lista_contatos.insert(0,contato_format)
        nome.delete(0,'end')
        telefone.delete(0,'end')
        email.delete(0,'end')
        salvar_contatos()
    else:
        messagebox.showerror("ERRO",'O campo Contatos está Vazio')

def salvar_contatos():
    with open('contatos.txt','w') as ta:
        contatos = lista_contatos.get(0,END)

        for contato in contatos:
            ta.write(contato + "\n")
            
def carregar_contatos():
    
    if(salvar_contatos()):
        with open('contatos.txt','r') as ta:
            contatos = ta.readlines()
            for contato in contatos:
                lista_contatos.insert(0,contato.strip())
    else:
        with open('contatos.txt','w') as ta:
            contatos = lista_contatos.get(0,END)

            for x in contatos:
                ta.write(x+'\n')
            
def del_contatos():                 
    selecionada = lista_contatos.curselection()
    if(selecionada):
        lista_contatos.delete(selecionada)
        salvar_contatos()
    else:
        messagebox.showerror("ERRO",'selecione um contato !!!')
        
            
#------------------------------------Janela--------------------------------        
ctk.set_appearance_mode('dark')
janela = ctk.CTk()
janela.geometry('950x700')
janela.title('Agenda de Contatos')
janela.resizable(False,False)

#----------------------------------------------------------------------

ctk.CTkLabel (janela, text="Agenda de Contatos", font=("Verdana", 24,"bold"), text_color="White").pack(pady=20)

nome = ctk.CTkEntry(janela,
                    width=260,
                    height=40,
                    border_color='#4912df',
                    placeholder_text='Informe seu nome')
nome.place(x=40,y = 120)

telefone = ctk.CTkEntry(janela,
                    width=260,
                    height=40,
                    border_color='#4912df',
                    placeholder_text='Informe seu Telefone')
telefone.place(x= 320 , y = 120)

email = ctk.CTkEntry(janela,    
                    width=260,
                    height=40,
                    border_color='#4912df',
                    placeholder_text='Informe seu Email')
email.place(x= 600, y = 120)

adcionar = ctk.CTkButton(janela,
                      width=180,
                      height=40,
                      fg_color='blue',
                      hover_color='#1E8CE6',
                      text='Adicionar',
                      text_color='white',
                      cursor='hand2',
                      font=('arial',13,'bold'),
                      command=add_contato)

adcionar.place(x=205,y=200)

excluir = ctk.CTkButton(janela,
                      width=180,
                      height=40,
                      fg_color='red',
                      hover_color='darkred',
                      text='Excluir',
                      text_color='white',
                      cursor='hand2',
                      font=('arial',13,'bold'),
                      command=del_contatos)
excluir.place(x=520,y=200)


lista_contatos = Listbox(janela,
                         width=82,
                         height=20,
                         font=('verdana',12),
                         background='#363636',
                         highlightbackground='#4912df',
                         highlightthickness=2,
                         fg='white')
lista_contatos.place(x=20,y=270)


carregar_contatos()
janela.mainloop()
