# Importar la biblioteca tkinter para interfaces gráficas y el módulo messagebox para mostrar mensajes
import tkinter as tk
from tkinter import messagebox

# Definir la clase RegistroContactos para gestionar los contactos
class RegistroContactos:
    # Método de inicialización que recibe el widget principal (master) como argumento
    def __init__(self, master):
        # Asignar el widget principal a la instancia de la clase
        self.master = master
        # Establecer el título de la ventana principal
        master.title("Registro de Contactos")

        # Inicializar una lista para almacenar los contactos
        self.lista_contactos = []

        # Crear etiqueta y campo de entrada para el nombre del contacto
        self.label_nombre = tk.Label(master, text="Nombre:")
        self.label_nombre.grid(row=0, column=0)
        self.entry_nombre = tk.Entry(master)
        self.entry_nombre.grid(row=0, column=1)

        # Crear etiqueta y campo de entrada para el teléfono del contacto
        self.label_telefono = tk.Label(master, text="Teléfono:")
        self.label_telefono.grid(row=1, column=0)
        self.entry_telefono = tk.Entry(master)
        self.entry_telefono.grid(row=1, column=1)

        # Crear botón para agregar un nuevo contacto y asociarlo con el método agregar_contacto
        self.boton_agregar = tk.Button(master, text="Agregar contacto", command=self.agregar_contacto)
        self.boton_agregar.grid(row=2, column=0, columnspan=2, pady=10)

        # Crear botón para mostrar todos los contactos y asociarlo con el método mostrar_contactos
        self.boton_mostrar = tk.Button(master, text="Mostrar contactos", command=self.mostrar_contactos)
        self.boton_mostrar.grid(row=3, column=0, columnspan=2)

    # Método para agregar un nuevo contacto a la lista
    def agregar_contacto(self):
        # Obtener el nombre y el teléfono ingresados por el usuario
        nombre = self.entry_nombre.get()
        telefono = self.entry_telefono.get()

        # Verificar si se ingresaron valores válidos para el nombre y el teléfono
        if nombre and telefono:
            # Agregar el contacto a la lista
            self.lista_contactos.append((nombre, telefono))
            # Mostrar un mensaje de éxito utilizando el módulo messagebox
            messagebox.showinfo("Éxito", "Contacto agregado correctamente.")
            # Limpiar los campos de entrada después de agregar el contacto
            self.entry_nombre.delete(0, tk.END)
            self.entry_telefono.delete(0, tk.END)
        else:
            # Mostrar un mensaje de error si falta algún dato
            messagebox.showerror("Error", "Por favor, ingresa el nombre y el teléfono del contacto.")

    # Método para mostrar todos los contactos almacenados
    def mostrar_contactos(self):
        # Verificar si hay contactos en la lista
        if self.lista_contactos:
            # Crear una cadena con la información de los contactos para mostrar en el messagebox
            info_contactos = "Lista de contactos:\n"
            for nombre, telefono in self.lista_contactos:
                info_contactos += f"Nombre: {nombre}, Teléfono: {telefono}\n"
            # Mostrar la información de los contactos utilizando el módulo messagebox
            messagebox.showinfo("Contactos", info_contactos)
        else:
            # Mostrar un mensaje si no hay contactos registrados
            messagebox.showinfo("Contactos", "No hay contactos en el registro.")

# Crear una instancia de la aplicación de registro de contactos y ejecutarla
root = tk.Tk()
app = RegistroContactos(root)
root.mainloop()
