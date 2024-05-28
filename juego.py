import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir algunos colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definir las dimensiones de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CodeRunner: Aventuras en el Reino del Código")

# Definir la clase del jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect += self.speed

# Crear el grupo de sprites para el jugador
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Bucle principal del juego
running = True
while running:
    # Procesar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar
    all_sprites.update()

    # Dibujar / renderizar
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Limitar la velocidad de fotogramas
    pygame.time.Clock().tick(60)

# Salir del juego
pygame.quit()
sys.exit()
