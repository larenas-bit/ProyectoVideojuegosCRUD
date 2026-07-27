print("Interfaz iniciada")
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from crud import *

ventana = tk.Tk()
ventana.configure(bg="#6588A5")
ventana.title("Gestor de Videojuegos")

ventana.geometry("900x550")

tk.Label(ventana,text="Título").grid(row=0,column=0,padx=10,pady=5)

tk.Label(ventana,text="Género").grid(row=1,column=0,padx=10,pady=5)

tk.Label(ventana,text="Clasificación").grid(row=2,column=0,padx=10,pady=5)

tk.Label(ventana,text="Plataforma").grid(row=3,column=0,padx=10,pady=5)

titulo=tk.Entry(ventana,width=35)
titulo.grid(row=0,column=1)

genero=tk.Entry(ventana,width=35)
genero.grid(row=1,column=1)

clasificacion=tk.Entry(ventana,width=35)
clasificacion.grid(row=2,column=1)

plataforma=tk.Entry(ventana,width=35)
plataforma.grid(row=3,column=1)

tabla=ttk.Treeview(
    ventana,
    columns=("ID","Titulo","Genero","Clasificacion","Plataforma"),
    show="headings"
)

tabla.heading("ID",text="ID")
tabla.heading("Titulo",text="Título")
tabla.heading("Genero",text="Género")
tabla.heading("Clasificacion",text="Clasificación")
tabla.heading("Plataforma",text="Plataforma")

tabla.grid(row=6,column=0,columnspan=5,padx=15,pady=20)

def cargar():

    for fila in tabla.get_children():
        tabla.delete(fila)

    videojuegos=mostrar_videojuegos()

    for juego in videojuegos:
        tabla.insert("",tk.END,values=juego)

#Agregar

def agregar():

    agregar_videojuego(

        titulo.get(),

        genero.get(),

        clasificacion.get(),

        plataforma.get()

    )

    messagebox.showinfo("Correcto","Videojuego agregado")

    limpiar()

    cargar()


#limpiar

def limpiar():

    titulo.delete(0,tk.END)

    genero.delete(0,tk.END)

    clasificacion.delete(0,tk.END)

    plataforma.delete(0,tk.END)


#Select

def seleccionar(event):

    seleccionado=tabla.focus()

    datos=tabla.item(seleccionado)

    fila=datos["values"]

    if fila:

        titulo.delete(0,tk.END)
        genero.delete(0,tk.END)
        clasificacion.delete(0,tk.END)
        plataforma.delete(0,tk.END)

        titulo.insert(0,fila[1])
        genero.insert(0,fila[2])
        clasificacion.insert(0,fila[3])
        plataforma.insert(0,fila[4])

#Actualizar

def actualizar():

    seleccionado=tabla.focus()

    datos=tabla.item(seleccionado)

    fila=datos["values"]

    if fila:

        actualizar_videojuego(

            fila[0],

            titulo.get(),

            genero.get(),

            clasificacion.get(),

            plataforma.get()

        )

        cargar()

        limpiar()

        messagebox.showinfo("Actualizado","Registro actualizado")

#eliminar

def eliminar():

    seleccionado=tabla.focus()

    datos=tabla.item(seleccionado)

    fila=datos["values"]

    if fila:

        eliminar_videojuego(fila[0])

        cargar()

        limpiar()

        messagebox.showinfo("Eliminado","Registro eliminado")

#Botones

tk.Button(

    ventana,

    text="Agregar",

    command=agregar,

    width=15

).grid(row=5,column=0,pady=15)



tk.Button(

    ventana,

    text="Actualizar",

    command=actualizar,

    width=15

).grid(row=5,column=1)



tk.Button(

    ventana,

    text="Eliminar",

    command=eliminar,

    width=15

).grid(row=5,column=2)



tk.Button(

    ventana,

    text="Mostrar",

    command=cargar,

    width=15

).grid(row=5,column=3)


#evento 

tabla.bind("<<TreeviewSelect>>",seleccionar)

cargar()

ventana.mainloop()