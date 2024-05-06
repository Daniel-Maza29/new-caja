#DANIEL MAZA RUIZ
import tkinter as tk
from PIL import Image, ImageTk

class VentanaLogin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DanielApp")
        self.geometry("800x500")
        self.config(bg=("#23BAC4"))
        
        path = Image.open("D:\logo.png")
        icono = ImageTk.PhotoImage(path)
        self.iconphoto(True, icono)

        

        self.marco_izquierdo = tk.Frame(self, width=400, height=500)
        self.marco_izquierdo.grid(row=0, column=0, sticky="nsew")

        self.logo = tk.Label(self.marco_izquierdo, text="Se supone \n que aquí iba la \n Imágen\n :)", font=("Time New Roman", 18))
        self.logo.grid(row=0, column=0, padx=20, pady=200, sticky="nsew")


        self.marco_derecho = tk.Frame(self, width=400, height=500)
        self.marco_derecho.grid(row=0, column=1, sticky="nsew")

        self.etiqueta_titulo = tk.Label(self.marco_derecho, text="Ingrese Usuario y Contraseña: ", font=("Time New Roman", 18))
        self.etiqueta_titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=80, sticky="nsew")
#DANIEL MAZA RUIZ
        self.etiqueta_usuario = tk.Label(self.marco_derecho, text="Usuario:")
        self.etiqueta_usuario.grid(row=1, column=0, padx=20, pady=5, sticky="w")

        self.entrada_usuario = tk.Entry(self.marco_derecho)
        self.entrada_usuario.grid(row=1, column=1, padx=20, pady=5, sticky="ew")

        self.etiqueta_clave = tk.Label(self.marco_derecho, text="Clave:")
        self.etiqueta_clave.grid(row=2, column=0, padx=20, pady=5, sticky="w")

        self.entrada_clave = tk.Entry(self.marco_derecho, show="*")
        self.entrada_clave.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

        self.boton_ingresar = tk.Button(self.marco_derecho, text="Ingresar datos")
        self.boton_ingresar.grid(row=3, column=0, columnspan=2, padx=20, pady=50, sticky="nsew")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.resizable(False, False)


ventana_login = VentanaLogin()
ventana_login.mainloop()
#DANIEL MAZA RUIZ 