import pygame
import sys
import os

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Ejemplo Pygame - Personaje con Imagen')

# Colores
BLANCO = (255, 255, 255)

# Cargar imagen del personaje (debe estar en la misma carpeta)
# Puedes usar cualquier imagen PNG pequeña, por ejemplo "personaje.png"
RUTA_IMAGEN = os.path.join(os.path.dirname(__file__), 'personaje.png')
if not os.path.exists(RUTA_IMAGEN):
    # Si no existe, crea un cuadrado temporal
    personaje_img = pygame.Surface((50, 50))
    personaje_img.fill((0, 128, 255))
else:
    personaje_img = pygame.image.load(RUTA_IMAGEN).convert_alpha()

personaje_rect = personaje_img.get_rect()
personaje_rect.center = (ANCHO // 2, ALTO // 2)
velocidad = 5

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        personaje_rect.x -= velocidad
    if teclas[pygame.K_RIGHT]:
        personaje_rect.x += velocidad
    if teclas[pygame.K_UP]:
        personaje_rect.y -= velocidad
    if teclas[pygame.K_DOWN]:
        personaje_rect.y += velocidad

    # Detectar colisión con los bordes
    if personaje_rect.x < 0:
        personaje_rect.x = 0
    if personaje_rect.x + personaje_rect.width > ANCHO:
        personaje_rect.x = ANCHO - personaje_rect.width
    if personaje_rect.y < 0:
        personaje_rect.y = 0
    if personaje_rect.y + personaje_rect.height > ALTO:
        personaje_rect.y = ALTO - personaje_rect.height

    pantalla.fill(BLANCO)
    pantalla.blit(personaje_img, personaje_rect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
