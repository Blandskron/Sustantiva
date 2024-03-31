import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la ventana
width = 800
height = 600
window_size = (width, height)

# Crear la ventana
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Mi ventana de Pygame")

# Definir el color de fondo
background_color = (255, 255, 255)

# Bucle principal del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar la pantalla con el color de fondo
    screen.fill(background_color)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()
