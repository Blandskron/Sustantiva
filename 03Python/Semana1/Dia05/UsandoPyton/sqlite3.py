import tkinter as tk
import sqlite3

class VentanaIngresoDatos(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Ingreso de Datos")
        self.geometry("300x200")

        # Conexión a la base de datos
        self.conexion = sqlite3.connect('usuarios.db')
        self.cursor = self.conexion.cursor()

        # Verificar si la tabla de usuarios no existe y crearla
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                                id INTEGER PRIMARY KEY,
                                nombre TEXT,
                                edad INTEGER)''')

        # Etiquetas y entradas de texto
        tk.Label(self, text="Nombre:").pack()
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack()

        tk.Label(self, text="Edad:").pack()
        self.entry_edad = tk.Entry(self)
        self.entry_edad.pack()

        # Botón para guardar datos
        tk.Button(self, text="Guardar", command=self.guardar_usuario).pack()

    def guardar_usuario(self):
        # Obtener los datos ingresados por el usuario
        nombre = self.entry_nombre.get()
        edad = self.entry_edad.get()

        # Verificar que los campos no estén vacíos
        if nombre and edad:
            try:
                # Insertar datos en la tabla
                self.cursor.execute('''INSERT INTO usuarios (nombre, edad) VALUES (?, ?)''', (nombre, edad))
                self.conexion.commit()

                print("Usuario guardado en la base de datos.")

                # Limpiar las entradas de texto
                self.entry_nombre.delete(0, tk.END)
                self.entry_edad.delete(0, tk.END)
            except Exception as e:
                print(f"Error al guardar el usuario en la base de datos: {str(e)}")
        else:
            print("Por favor, ingrese todos los campos.")

    def __del__(self):
        # Cerrar conexión a la base de datos
        if self.conexion:
            self.conexion.close()

if __name__ == "__main__":
    app = VentanaIngresoDatos()
    app.mainloop()
