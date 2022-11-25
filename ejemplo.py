#Login
from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("Ventas")
ventana.geometry("400x400")

#Frame
frame = Frame(ventana)
frame.pack()
username_entry = Entry(frame)
username_entry.grid(row=1, column=1, padx=5, pady=5)
username_entry.config(justify="center")
password_entry = Entry(frame)
password_entry.grid(row=2, column=1, padx=5, pady=5)
password_entry.config(justify="center", show="*")
#Boton
def login():
    username_info = username_entry.get()
    password_info = password_entry.get()
    print(username_info, password_info)
    print("Conectando a Base de datos ----")
    #conectar y validar
    menu = Menu(ventana)
    ventana.config(menu=menu)
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(frame, text="Registro Exitoso", fg="green", font=("calibri", 11)).grid(row=3, column=0, columnspan=2, sticky=W+E)
button = Button(frame, text="Login", command=login)
button.grid(row=3, column=0, sticky=W, padx=5, pady=5)
button.config(padx=5, pady=5)

class Menu():
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Menu")
        self.ventana.geometry("400x400")
        self.ventana.config(bg="blue")
        #Frame
        frame = Frame(self.ventana)
        frame.pack()
        #Boton
        button = Button(frame, text="Salir", command=self.ventana.destroy)
        button.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        button.config(padx=5, pady=5)

ventana.mainloop()

