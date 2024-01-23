import turtle
import random
import math

# Configuración de la pantalla
wn = turtle.Screen()
wn.title("Turtle Collector")
wn.bgcolor("white")
wn.setup(width=600, height=600)

# Crear la tortuga del jugador
jugador = turtle.Turtle()
jugador.shape("turtle")
jugador.color("blue")
jugador.speed(0)
jugador.penup()
jugador.goto(0, -250)

# Crear lista para almacenar los objetos (círculos)
objetos = []

# Función para crear objetos (círculos) aleatorios en la pantalla
def crear_objeto():
    objeto = turtle.Turtle()
    objeto.shape("circle")
    objeto.color("red")
    objeto.speed(0)
    objeto.penup()
    x = random.randint(-290, 290)
    y = random.randint(100, 250)
    objeto.goto(x, y)
    objetos.append(objeto)

# Función para calcular la distancia entre dos puntos en el plano
def distancia(punto1, punto2):
    return math.sqrt((punto1[0] - punto2[0])**2 + (punto1[1] - punto2[1])**2)

# Evento de clic izquierdo para mover la tortuga
def mover_izquierda():
    x = jugador.xcor()
    x -= 20
    if x < -290:
        x = -290
    jugador.setx(x)

def mover_derecha():
    x = jugador.xcor()
    x += 20
    if x > 290:
        x = 290
    jugador.setx(x)

# Configurar eventos de teclado
wn.listen()
wn.onkey(mover_izquierda, "Left")
wn.onkey(mover_derecha, "Right")

# Bucle principal
while True:
    # Crear nuevos objetos de manera aleatoria
    if random.random() < 0.02:
        crear_objeto()

    # Mover los objetos hacia abajo
    for objeto in objetos:
        y = objeto.ycor()
        y -= 2
        objeto.sety(y)

        # Comprobar si la tortuga recoge el objeto
        if distancia(jugador.pos(), objeto.pos()) < 20:
            objeto.hideturtle()
            objetos.remove(objeto)

    # Limpiar objetos que han llegado al fondo de la pantalla
    for objeto in objetos:
        if objeto.ycor() < -290:
            objeto.hideturtle()
            objetos.remove(objeto)

    wn.update()
