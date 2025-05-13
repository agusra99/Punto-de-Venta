from tkinter import *
import tkinter as tk
import webbrowser

class Informacion(tk.Frame):

    def __init__(self, padre):
        super().__init__(padre)
        self.widgets()

    def widgets(self):
        # Título principal - sin fondo (bg por defecto)
        self.titulo = Label(self, text="AR ELECTRÓNICA", font=("Arial", 25, "bold"), bg="#C6D9E3")
        self.titulo.pack(pady=20)

        #Subtítulo - sin fondo (bg por defecto)
        self.titulo = Label(self, text="SOPORTE TÉCNICO", font=("Candara", 16, "bold"), bg="#C6D9E3")
        self.titulo.pack(pady=20)
        
        # Frame contenedor para alinear a la izquierda
        frame_contenido = Frame(self, bg="#C6D9E3")
        frame_contenido.pack(fill=X, padx=30)
        
        # Botón para WhatsApp redondeado
        self.btn_whatsapp = Button(frame_contenido, text="Enviar Mensaje", command=self.abrir_whatsapp, bg="#25D366", fg="white", width=15, height=2, font=("Arial", 12), relief=GROOVE, borderwidth=2)
        self.btn_whatsapp.pack(pady=5, anchor=W)
        
        # Número de WhatsApp - sin fondo
        self.lbl_numero = Label(frame_contenido, text="+54 11 69829517",bg="#C6D9E3", font=("Arial", 12))
        self.lbl_numero.pack(pady=5, anchor=W)
        
        # Espacio entre secciones - sin fondo
        Label(frame_contenido, text="", bg="#C6D9E3",pady=10)
        
        # Botón para Email redondeado
        self.btn_email = Button(frame_contenido, text="Enviar Email", command=self.abrir_email, bg="#4285F4", fg="white", width=15, height=2, font=("Arial", 12), relief=GROOVE, borderwidth=2)
        self.btn_email.pack(pady=5, anchor=W)
        
        # Dirección de email - sin fondo
        self.lbl_email = Label(frame_contenido, text="Email: agustin.ignacio.ranea@gmail.com", bg="#C6D9E3", font=("Arial", 12))
        self.lbl_email.pack(pady=5, anchor=W)
    
    def abrir_whatsapp(self):
        # Formato URL de WhatsApp Web con el número especificado
        numero = "541169829517"  # Sin el + y espacios
        url = f"https://web.whatsapp.com/send?phone={numero}"
        webbrowser.open(url)
    
    def abrir_email(self):
        # Abrir aplicación de correo con la dirección especificada
        correo = "agustin.ignacio.ranea@gmail.com"
        webbrowser.open(f"mailto:{correo}")