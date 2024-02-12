import tkinter as tk
from tkinter import messagebox

class RegistroContactos:
    def __init__(self, master):
        self.master = master
        master.title("Registro de Contactos")

        self.lista_contactos = []

        self.label_nombre = tk.Label(master, text="Nombre:")
        self.label_nombre.grid(row=0, column=0)

        self.entry_nombre = tk.Entry(master)
        self.entry_nombre.grid(row=0, column=1)

        self.label_telefono = tk.Label(master, text="Teléfono:")
        self.label_telefono.grid(row=1, column=0)

        self.entry_telefono = tk.Entry(master)
        self.entry_telefono.grid(row=1, column=1)

        self.boton_agregar = tk.Button(master, text="Agregar contacto", command=self.agregar_contacto)
        self.boton_agregar.grid(row=2, column=0, columnspan=2, pady=10)

        self.boton_mostrar = tk.Button(master, text="Mostrar contactos", command=self.mostrar_contactos)
        self.boton_mostrar.grid(row=3, column=0, columnspan=2)

    def agregar_contacto(self):
        nombre = self.entry_nombre.get()
        telefono = self.entry_telefono.get()

        if nombre and telefono:
            self.lista_contactos.append((nombre, telefono))
            messagebox.showinfo("Éxito", "Contacto agregado correctamente.")
            self.entry_nombre.delete(0, tk.END)
            self.entry_telefono.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Por favor, ingresa el nombre y el teléfono del contacto.")

    def mostrar_contactos(self):
        if self.lista_contactos:
            info_contactos = "Lista de contactos:\n"
            for nombre, telefono in self.lista_contactos:
                info_contactos += f"Nombre: {nombre}, Teléfono: {telefono}\n"
            messagebox.showinfo("Contactos", info_contactos)
        else:
            messagebox.showinfo("Contactos", "No hay contactos en el registro.")


# Crear y ejecutar la aplicación
root = tk.Tk()
app = RegistroContactos(root)
root.mainloop()
