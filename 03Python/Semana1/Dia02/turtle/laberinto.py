import turtle

# Definir el diseño del laberinto
laberinto = [
    "XXXXXXXXXX",
    "X        X",
    "X  XXXX  X",
    "X  X  X  X",
    "X  X  X  X",
    "X  X  X  X",
    "X  X  X  X",
    "X  XE    X",  # E representa la salida
    "XXXXXXX  X"
]

# Tamaño de los bloques del laberinto
ANCHO_BLOQUE = 20

# Inicializar la ventana
ventana = turtle.Screen()
ventana.title("Laberinto Turtle")
ventana.bgcolor("white")
ventana.setup(width=len(laberinto[0]) * ANCHO_BLOQUE, height=len(laberinto) * ANCHO_BLOQUE)

# Crear la tortuga
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.color("green")
tortuga.penup()

# Función para dibujar el laberinto
def dibujar_laberinto():
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            caracter = laberinto[i][j]
            x = -len(laberinto[0]) * ANCHO_BLOQUE / 2 + j * ANCHO_BLOQUE
            y = len(laberinto) * ANCHO_BLOQUE / 2 - i * ANCHO_BLOQUE

            if caracter == "X":
                tortuga.goto(x, y)
                tortuga.pendown()
                tortuga.begin_fill()
                for _ in range(4):
                    tortuga.forward(ANCHO_BLOQUE)
                    tortuga.right(90)
                tortuga.end_fill()
                tortuga.penup()

# Inicializar el laberinto
dibujar_laberinto()

# Funciones para el movimiento de la tortuga
def mover_arriba():
    nueva_posicion = (tortuga.xcor(), tortuga.ycor() + ANCHO_BLOQUE)
    if nueva_posicion not in posiciones_paredes:
        tortuga.sety(tortuga.ycor() + ANCHO_BLOQUE)

def mover_abajo():
    nueva_posicion = (tortuga.xcor(), tortuga.ycor() - ANCHO_BLOQUE)
    if nueva_posicion not in posiciones_paredes:
        tortuga.sety(tortuga.ycor() - ANCHO_BLOQUE)

def mover_izquierda():
    nueva_posicion = (tortuga.xcor() - ANCHO_BLOQUE, tortuga.ycor())
    if nueva_posicion not in posiciones_paredes:
        tortuga.setx(tortuga.xcor() - ANCHO_BLOQUE)

def mover_derecha():
    nueva_posicion = (tortuga.xcor() + ANCHO_BLOQUE, tortuga.ycor())
    if nueva_posicion not in posiciones_paredes:
        tortuga.setx(tortuga.xcor() + ANCHO_BLOQUE)

# Configurar teclas para el movimiento
ventana.listen()
ventana.onkey(mover_arriba, "Up")
ventana.onkey(mover_abajo, "Down")
ventana.onkey(mover_izquierda, "Left")
ventana.onkey(mover_derecha, "Right")

# Identificar posiciones de las paredes
posiciones_paredes = set()
for i in range(len(laberinto)):
    for j in range(len(laberinto[i])):
        if laberinto[i][j] == "X":
            x = -len(laberinto[0]) * ANCHO_BLOQUE / 2 + j * ANCHO_BLOQUE
            y = len(laberinto) * ANCHO_BLOQUE / 2 - i * ANCHO_BLOQUE
            posiciones_paredes.add((x, y))

# Mantener la ventana abierta
ventana.mainloop()
