import pygame
import random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 30
ROWS = HEIGHT // GRID_SIZE
COLS = WIDTH // GRID_SIZE

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Configuración de la pantalla
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman Game")

# Clase Pacman
class Pacman:
    def __init__(self):
        self.x = random.randint(1, COLS - 2) * GRID_SIZE
        self.y = random.randint(1, ROWS - 2) * GRID_SIZE
        self.radius = GRID_SIZE // 2

    def draw(self, surface):
        pygame.draw.circle(surface, YELLOW, (self.x + self.radius, self.y + self.radius), self.radius)

# Clase Ghost
class Ghost:
    def __init__(self):
        self.x = random.randint(1, COLS - 2) * GRID_SIZE
        self.y = random.randint(1, ROWS - 2) * GRID_SIZE
        self.radius = GRID_SIZE // 2

    def draw(self, surface):
        pygame.draw.circle(surface, RED, (self.x + self.radius, self.y + self.radius), self.radius)

# Clase Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 3

    def draw(self, surface):
        pygame.draw.circle(surface, BLUE, (self.x + GRID_SIZE // 2, self.y + GRID_SIZE // 2), self.radius)

# Función principal
def main():
    pacman = Pacman()
    ghosts = [Ghost() for _ in range(3)]
    points = [Point(x * GRID_SIZE, y * GRID_SIZE) for x in range(COLS) for y in range(ROWS) if (x, y) != (pacman.x // GRID_SIZE, pacman.y // GRID_SIZE)]

    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pacman.x -= GRID_SIZE
        if keys[pygame.K_RIGHT]:
            pacman.x += GRID_SIZE
        if keys[pygame.K_UP]:
            pacman.y -= GRID_SIZE
        if keys[pygame.K_DOWN]:
            pacman.y += GRID_SIZE

        # Comprobar si Pacman atrapó a un fantasma
        for ghost in ghosts:
            if (pacman.x, pacman.y) == (ghost.x, ghost.y):
                running = False

        # Dibujar en la pantalla
        win.fill(BLACK)
        for point in points:
            point.draw(win)
        pacman.draw(win)
        for ghost in ghosts:
            ghost.draw(win)
        pygame.display.update()

    pygame.quit()

# Iniciar el juego
if __name__ == "__main__":
    main()
