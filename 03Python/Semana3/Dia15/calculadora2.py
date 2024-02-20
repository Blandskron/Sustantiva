import tkinter as tk
import math

class CalculadoraAvanzada:
    def __init__(self, master):
        """
        Constructor de la clase CalculadoraAvanzada.

        Args:
        - master: Ventana principal de la aplicación.
        """
        self.master = master
        master.title("Calculadora Avanzada")  # Establece el título de la ventana

        # Crea un widget de entrada para mostrar y recibir datos
        self.display = tk.Entry(master, width=40, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        # Botones para operaciones básicas
        botones_basicos = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Crea y coloca los botones básicos en la ventana
        for simbolo, fila, columna in botones_basicos:
            boton = tk.Button(master, text=simbolo, padx=20, pady=10,
                              command=lambda s=simbolo: self.presionar(s))
            boton.grid(row=fila, column=columna)

        # Botones para operaciones avanzadas
        botones_avanzados = [
            ('sin', 'sin', 1, 4), ('cos', 'cos', 1, 5),
            ('tan', 'tan', 2, 4), ('log', 'log', 2, 5),
            ('sqrt', 'sqrt', 3, 4), ('^', '**', 3, 5),
            ('(', '(', 4, 4), (')', ')', 4, 5),
            ('AC', 'AC', 5, 4), ('π', 'pi', 5, 5)
        ]

        # Crea y coloca los botones avanzados en la ventana
        for texto, funcion, fila, columna in botones_avanzados:
            boton = tk.Button(master, text=texto, padx=20, pady=10,
                              command=lambda f=funcion: self.avanzado(f))
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
        elif valor == 'AC':  # Si se presiona el botón AC (limpiar todo)
            self.display.delete(0, tk.END)  # Borra el contenido del campo de entrada
        else:
            self.display.insert(tk.END, valor)  # Inserta el valor del botón presionado al final del campo de entrada

    def avanzado(self, funcion):
        """
        Método para manejar las funciones avanzadas.

        Args:
        - funcion: Función avanzada seleccionada.
        """
        if funcion == 'pi':  # Si se presiona el botón π (pi)
            self.display.insert(tk.END, math.pi)  # Inserta el valor de pi al final del campo de entrada
        elif funcion == 'sqrt':  # Si se presiona el botón sqrt (raíz cuadrada)
            self.display.insert(tk.END, 'sqrt(')  # Inserta 'sqrt(' al final del campo de entrada
        else:
            self.display.insert(tk.END, f'{funcion}(')  # Inserta la función avanzada al final del campo de entrada


# Crear y ejecutar la aplicación
root = tk.Tk()  # Crea la ventana principal de la aplicación
app = CalculadoraAvanzada(root)  # Crea una instancia de la calculadora pasando la ventana principal como argumento
root.mainloop()  # Ejecuta el ciclo principal de la aplicación
