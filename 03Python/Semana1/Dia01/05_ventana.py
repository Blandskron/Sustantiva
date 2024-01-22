# Contenido del archivo ventana.py
import tkinter as tk

def mostrar_mensaje():
    label.config(text="¡Hola desde ventana.py!")

ventana = tk.Tk()
ventana.title("Ventana.py")

label = tk.Label(ventana, text="¡Presiona el botón!")
label.pack(pady=10)

boton = tk.Button(ventana, text="Mostrar Mensaje", command=mostrar_mensaje)
boton.pack(pady=10)

ventana.mainloop()
