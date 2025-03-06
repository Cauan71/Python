# Baixar ( pip install customtkinter )
# Importar o customtkinter para ctk 

import customtkinter as ctk


ctk.set_appearance_mode('dark')

# Criando variavel janela(div(caixa)) e introduzindo a resolução de tela
janela = ctk.CTk('gray')
janela.geometry('500x300')

# Inicializando (janela)
# 1 parametro(largura , altura)
janela.resizable(False, False)

# Titulo da janela
janela.title("Sistema de Acesso 2025")


ctk.CTkLabel(janela,text='Sistema de Acesso 2025',
             font=('Arial',30,'bold'),
             text_color='white').pack(pady=30)


login = ctk.CTkEntry(janela, width=400,height=35,
                    placeholder_text='Digite seu Login',font=('Arial',15),text_color='white')
login.pack(pady=10)


senha = ctk.CTkEntry(janela,width=400,height=35,
                    placeholder_text='Digite sua senha', show = "*",font=('Arial',15),
                    text_color='white')

senha.pack(pady= 10)

botao = ctk.CTkButton(janela, width=200, height=20,
                      bg_color='white',font=('Arial',16,'bold',),
                      text='Acessar',border_color=('green','bold'),hover_color='green')

botao.pack(pady=20)






janela.mainloop()