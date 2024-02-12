import tkinter as tk
import math

class CalculadoraAvanzada:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Avanzada")

        self.display = tk.Entry(master, width=40, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        # Botones para operaciones básicas
        botones_basicos = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

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

        for texto, funcion, fila, columna in botones_avanzados:
            boton = tk.Button(master, text=texto, padx=20, pady=10,
                              command=lambda f=funcion: self.avanzado(f))
            boton.grid(row=fila, column=columna)

    def presionar(self, valor):
        if valor == '=':
            try:
                resultado = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(resultado))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif valor == 'AC':
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, valor)

    def avanzado(self, funcion):
        if funcion == 'pi':
            self.display.insert(tk.END, math.pi)
        elif funcion == 'sqrt':
            self.display.insert(tk.END, 'sqrt(')
        else:
            self.display.insert(tk.END, f'{funcion}(')


# Crear y ejecutar la aplicación
root = tk.Tk()
app = CalculadoraAvanzada(root)
root.mainloop()
