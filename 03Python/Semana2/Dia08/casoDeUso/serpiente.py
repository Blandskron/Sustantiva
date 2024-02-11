import pygame
import random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20

# Colores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Configuración de la pantalla
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clase Snake
class Snake:
    def __init__(self):
        self.body = [(WIDTH / 2, HEIGHT / 2)]
        self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])

    def move(self):
        x, y = self.body[0]
        dx, dy = self.direction
        new_head = ((x + dx * GRID_SIZE) % WIDTH, (y + dy * GRID_SIZE) % HEIGHT)
        if new_head in self.body[1:]:
            return False
        self.body.insert(0, new_head)
        return True

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) == self.direction:
            return
        self.direction = direction

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

# Clase Food
class Food:
    def __init__(self):
        self.position = (random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE, random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))

# Función principal
def main():
    snake = Snake()
    food = Food()
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))

        # Movimiento de la serpiente
        if not snake.move():
            running = False

        # Comprobar si la serpiente ha comido la comida
        if snake.body[0] == food.position:
            food = Food()
        else:
            snake.body.pop()

        # Dibujar en la pantalla
        win.fill(WHITE)
        snake.draw(win)
        food.draw(win)
        pygame.display.update()

    pygame.quit()

# Iniciar el juego
if __name__ == "__main__":
    main()
