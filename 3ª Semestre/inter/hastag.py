

from tkinter import *

# Criar a janela principal

janela = Tk()
# janela.geometry('500x300')
janela.title('Cotação Atual da Moeda')

# Label - Texto que irá colocar na janela

texto_orientacao = Label(janela,text='Clique no Botão para obter os valores das moedas')
# Grid - escolhe a posição do texto

texto_orientacao.grid(column=0,row=0)

botao = Button(janela,text='Pesquisar',background='Green')
botao.grid(column=0,row=3)




janela.mainloop()







