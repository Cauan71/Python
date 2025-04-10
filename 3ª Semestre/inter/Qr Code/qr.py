import customtkinter as ctk
import qrcode
from PIL import ImageTk, Image


def gerar_qrcode():
    texto = entry.get() 
    if texto:
        
        qr = qrcode.QRCode(
            version=2, 
            box_size=10,
            border=3,
            
            
        )
        qr.add_data(texto)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')

        
        img_tk = ImageTk.PhotoImage(img)
        
       
        label_img.configure(image=img_tk)
        label_img.image = img_tk  



ctk.set_appearance_mode("dark")

janela = ctk.CTk()  
janela.title("Gerador de QR Code")
janela.geometry("700x500") 
janela.resizable(False,False)


label_instrução = ctk.CTkLabel(janela, text="Digite o texto para gerar o QR code:", font=("Verdana",16,"bold"))
label_instrução.pack(pady=10)


entry = ctk.CTkEntry(janela, width=300, font=("Arial",14),height=40)
entry.pack(pady=10)


btn_gerar = ctk.CTkButton(janela, text="Gerar QR Code", command=gerar_qrcode,fg_color="green",hover_color="#00b167")
btn_gerar.pack(pady=20)


label_img = ctk.CTkLabel(janela,text="")
label_img.pack(pady=20)

janela.mainloop()