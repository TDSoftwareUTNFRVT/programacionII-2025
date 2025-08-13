import pygame
import sys
import os

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Pygame - Spider Salta')

# Colores
BLANCO = (255, 255, 255)

# Cargar imagen del personaje
RUTA_IMAGEN = os.path.join(os.path.dirname(__file__), 'spider.png')
if not os.path.exists(RUTA_IMAGEN):
    spider_img = pygame.Surface((50, 50))
    spider_img.fill((128, 0, 128))
else:
    spider_img = pygame.image.load(RUTA_IMAGEN).convert_alpha()
    spider_img = pygame.transform.scale(spider_img, (50, 50))

spider_rect = spider_img.get_rect()
spider_rect.bottomleft = (0, ALTO)  # vértice inferior izquierdo

velocidad_y = 0
velocidad_x = 0
GRAVEDAD = 1
SALTO = -18
SALTO_X = 10  # velocidad horizontal del salto parabólico
en_suelo = True

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and en_suelo:
                velocidad_y = SALTO
                velocidad_x = 0
                en_suelo = False
            if evento.key == pygame.K_RIGHT and en_suelo:
                velocidad_y = SALTO
                velocidad_x = SALTO_X
                en_suelo = False


    # Aplicar gravedad y movimiento horizontal
    velocidad_y += GRAVEDAD
    spider_rect.y += velocidad_y
    spider_rect.x += velocidad_x

    # Frenar el movimiento horizontal gradualmente (simula fricción del aire)
    if velocidad_x > 0:
        velocidad_x -= 1
    elif velocidad_x < 0:
        velocidad_x += 1

    # Colisión con el suelo
    if spider_rect.bottom >= ALTO:
        spider_rect.bottom = ALTO
        velocidad_y = 0
        velocidad_x = 0
        en_suelo = True


    pantalla.fill(BLANCO)
    pantalla.blit(spider_img, spider_rect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
