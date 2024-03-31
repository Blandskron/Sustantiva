import turtle
import random

# Configuración de la ventana
wn = turtle.Screen()
wn.title("Adivina la dirección")
wn.bgcolor("white")

# Crear la tortuga
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.color("blue")
tortuga.speed(0)

# Función para girar la tortuga en una dirección aleatoria
def girar_aleatorio():
    angulo = random.randint(0, 360)
    tortuga.left(angulo)

# Evento de clic en la ventana
def clic_izquierdo(x, y):
    # Girar la tortuga en una dirección aleatoria
    girar_aleatorio()

# Configurar el evento de clic izquierdo
wn.onclick(clic_izquierdo)

# Mensaje de inicio
mensaje_inicio = turtle.Turtle()
mensaje_inicio.color("black")
mensaje_inicio.penup()
mensaje_inicio.hideturtle()
mensaje_inicio.goto(0, 250)
mensaje_inicio.write("¡Adivina la dirección de la tortuga!", align="center", font=("Arial", 16, "normal"))

# Mensaje de instrucciones
mensaje_instrucciones = turtle.Turtle()
mensaje_instrucciones.color("black")
mensaje_instrucciones.penup()
mensaje_instrucciones.hideturtle()
mensaje_instrucciones.goto(0, -250)
mensaje_instrucciones.write("Haz clic en la ventana. ¿Hacia dónde crees que se moverá la tortuga?", align="center", font=("Arial", 14, "normal"))

# Bucle principal
wn.mainloop()
