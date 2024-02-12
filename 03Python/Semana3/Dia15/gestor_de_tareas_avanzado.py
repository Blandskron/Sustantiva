import tkinter as tk
from tkinter import messagebox

class GestorTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        self.tareas = {}

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.label_nombre = tk.Label(self.frame, text="Nombre de la tarea:")
        self.label_nombre.grid(row=0, column=0, sticky="w")
        self.entry_nombre = tk.Entry(self.frame)
        self.entry_nombre.grid(row=0, column=1)

        self.label_fecha = tk.Label(self.frame, text="Fecha de vencimiento:")
        self.label_fecha.grid(row=1, column=0, sticky="w")
        self.entry_fecha = tk.Entry(self.frame)
        self.entry_fecha.grid(row=1, column=1)

        self.label_prioridad = tk.Label(self.frame, text="Prioridad:")
        self.label_prioridad.grid(row=2, column=0, sticky="w")
        self.entry_prioridad = tk.Entry(self.frame)
        self.entry_prioridad.grid(row=2, column=1)

        self.button_agregar = tk.Button(self.frame, text="Agregar Tarea", command=self.agregar_tarea)
        self.button_agregar.grid(row=3, column=0, columnspan=2, pady=10)

        self.button_mostrar = tk.Button(self.frame, text="Mostrar Tareas", command=self.mostrar_tareas)
        self.button_mostrar.grid(row=4, column=0, columnspan=2, pady=10)

    def agregar_tarea(self):
        nombre = self.entry_nombre.get()
        fecha = self.entry_fecha.get()
        prioridad = self.entry_prioridad.get()

        if nombre and fecha and prioridad:
            self.tareas[nombre] = {"Fecha de vencimiento": fecha, "Prioridad": prioridad}
            messagebox.showinfo("Tarea Agregada", f"Tarea '{nombre}' agregada con éxito.")
        else:
            messagebox.showwarning("Campos Vacíos", "Por favor complete todos los campos.")

    def mostrar_tareas(self):
        if self.tareas:
            tarea_texto = ""
            for nombre, detalles in self.tareas.items():
                tarea_texto += f"Nombre: {nombre}, Fecha de vencimiento: {detalles['Fecha de vencimiento']}, Prioridad: {detalles['Prioridad']}\n"
            messagebox.showinfo("Tareas", tarea_texto)
        else:
            messagebox.showinfo("Tareas", "No hay tareas registradas.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GestorTareasApp(root)
    root.mainloop()
