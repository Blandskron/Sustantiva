import tkinter as tk

class Calculadora:
    def __init__(self, master):
        """
        Constructor de la clase Calculadora.

        Args:
        - master: Ventana principal de la aplicación.
        """
        self.master = master
        master.title("Calculadora")  # Establece el título de la ventana

        # Crea un widget de entrada para mostrar y recibir datos
        self.display = tk.Entry(master, width=30, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Define los botones de la calculadora
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Crea los botones en la ventana
        for simbolo, fila, columna in botones:
            boton = tk.Button(master, text=simbolo, padx=20, pady=10,
                              command=lambda s=simbolo: self.presionar(s))
            boton.grid(row=fila, column=columna)

    def presionar(self, valor):
        """
        Método para manejar los eventos de presionar un botón.

        Args:
        - valor: Valor del botón presionado.
        """
        if valor == '=':  # Si se presiona el botón de igual
            try:
                resultado = eval(self.display.get())  # Evalúa la expresión en el campo de entrada
                self.display.delete(0, tk.END)  # Borra el contenido del campo de entrada
                self.display.insert(0, str(resultado))  # Inserta el resultado en el campo de entrada
            except:
                self.display.delete(0, tk.END)  # Borra el contenido del campo de entrada
                self.display.insert(0, "Error")  # Muestra "Error" en el campo de entrada en caso de error
        else:
            self.display.insert(tk.END, valor)  # Inserta el valor del botón presionado al final del campo de entrada

# Crea y ejecuta la aplicación
root = tk.Tk()  # Crea la ventana principal de la aplicación
app = Calculadora(root)  # Crea una instancia de la calculadora pasando la ventana principal como argumento
root.mainloop()  # Ejecuta el ciclo principal de la aplicación
