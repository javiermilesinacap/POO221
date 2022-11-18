import tkinter

ventana = tkinter.Tk()
#ventana.geometry("1024x768")

caja = tkinter.Entry()
#caja.pack()
caja.place(x=100, y=100)
caja.grid(row=0, column=0)
etiqueta = tkinter.Label(text="Hola")
#etiqueta.pack()
etiqueta.grid(row=1, column=0)
lista = tkinter.Listbox(ventana)
lista.insert(1,"Hola")
lista.insert(2,"Mundo")
lista.option_add("*font", "Helvetica 20")
#lista.pack()
lista.grid(row=2, column=0)
radio = tkinter.Radiobutton(ventana, text="Opcion 1", value=1)
radio.grid(row=3, column=0)
radio = tkinter.Radiobutton(ventana, text="Opcion 2", value=2)
radio.grid(row=4, column=0) 
check = tkinter.Checkbutton(ventana, text="Opcion 1")
check.grid(row=5, column=0)
def guardar():
    f = open("datos.txt", "w")
    f.write("Nombre: " + caja.get())
    f.close()
boton= tkinter.Button(ventana, text="Boton", command=guardar)
boton.grid(row=6, column=0)
#boton.pack()
etiqueta1 = tkinter.Label(text="Ingresa un valor")
etiqueta1.grid(row=0, column=0)
caja1 = tkinter.Entry()
caja1.grid(row=0, column=1)
ventana.mainloop()

#Para un usuario, crea un formulario que pida 
#nombre, apellido, edad, sexo, correo, contraseña, username, hobbies.
#Al presionar el botón, almacena los datos en un diccionario, y posteriormente, genera la consulta 
#para insertar los datos en una tabla de una base de datos.