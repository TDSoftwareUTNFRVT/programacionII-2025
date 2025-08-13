import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Ejemplo Pygame - Movimiento con Flechas')

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Personaje
personaje = pygame.Rect(ANCHO // 2, ALTO // 2, 50, 50)
velocidad = 5

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        personaje.x -= velocidad
    if teclas[pygame.K_RIGHT]:
        personaje.x += velocidad
    if teclas[pygame.K_UP]:
        personaje.y -= velocidad
    if teclas[pygame.K_DOWN]:
        personaje.y += velocidad

    pantalla.fill(BLANCO)
    pygame.draw.rect(pantalla, ROJO, personaje)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
