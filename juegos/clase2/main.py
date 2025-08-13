import pygame
import sys
from spider import Spider

# Inicializar pygame
pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Pygame OOP - Spider Modular')
BLANCO = (255, 255, 255)

spider = Spider(0, ALTO)

reloj = pygame.time.Clock()
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                spider.saltar()
            if evento.key == pygame.K_RIGHT:
                spider.saltar_adelante()

    spider.actualizar(ANCHO, ALTO)
    pantalla.fill(BLANCO)
    pantalla.blit(spider.imagen, spider.rect)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()
