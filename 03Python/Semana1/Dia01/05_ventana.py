# Contenido del archivo ventana.py
# Importamos el módulo tkinter y lo renombramos como tk para facilitar su uso.
import tkinter as tk

# Definimos una función llamada mostrar_mensaje, que cambiará el texto del label cuando se llame.
def mostrar_mensaje():
    # Configuramos el texto del label para que muestre un nuevo mensaje.
    label.config(text="¡Hola desde ventana.py!")

# Creamos una instancia de la clase Tk() para crear la ventana principal.
ventana = tk.Tk()

# Establecemos el título de la ventana.
ventana.title("Ventana.py")

# Creamos un widget Label para mostrar un texto en la ventana, y lo empaquetamos en la ventana con un margen vertical de 10 píxeles.
label = tk.Label(ventana, text="¡Presiona el botón!")
label.pack(pady=10)

# Creamos un widget Button que llamará a la función mostrar_mensaje cuando se haga clic en él, y lo empaquetamos en la ventana con un margen vertical de 10 píxeles.
boton = tk.Button(ventana, text="Mostrar Mensaje", command=mostrar_mensaje)
boton.pack(pady=10)

# Llamamos al método mainloop() para que la ventana esté en un bucle y pueda responder a eventos.
ventana.mainloop()
