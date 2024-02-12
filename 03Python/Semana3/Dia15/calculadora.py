import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.display = tk.Entry(master, width=30, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Crear botones
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for simbolo, fila, columna in botones:
            boton = tk.Button(master, text=simbolo, padx=20, pady=10,
                              command=lambda s=simbolo: self.presionar(s))
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
        else:
            self.display.insert(tk.END, valor)

# Crear y ejecutar la aplicación
root = tk.Tk()
app = Calculadora(root)
root.mainloop()
