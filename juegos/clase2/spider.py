import pygame
import os

class Spider:
    def __init__(self, x, y, imagen_path='spider.png', ancho=50, alto=50):
        # Ruta absoluta a la imagen, relativa a este archivo
        self.imagen_path = os.path.join(os.path.dirname(__file__), imagen_path)
        self.ancho = ancho
        self.alto = alto
        self.cargar_imagen()
        self.rect = self.imagen.get_rect()
        self.rect.bottomleft = (x, y)
        self.velocidad_y = 0
        self.velocidad_x = 0
        self.GRAVEDAD = 1
        self.SALTO = -18
        self.SALTO_X = 10
        self.en_suelo = True

    def cargar_imagen(self):
        if not os.path.exists(self.imagen_path):
            self.imagen = pygame.Surface((self.ancho, self.alto))
            self.imagen.fill((128, 0, 128))
        else:
            self.imagen = pygame.image.load(self.imagen_path).convert_alpha()
            self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))

    def saltar(self):
        if self.en_suelo:
            self.velocidad_y = self.SALTO
            self.velocidad_x = 0
            self.en_suelo = False

    def saltar_adelante(self):
        if self.en_suelo:
            self.velocidad_y = self.SALTO
            self.velocidad_x = self.SALTO_X
            self.en_suelo = False

    def actualizar(self, ancho_pantalla, alto_pantalla):
        self.velocidad_y += self.GRAVEDAD
        self.rect.y += self.velocidad_y
        self.rect.x += self.velocidad_x
        if self.velocidad_x > 0:
            self.velocidad_x -= 1
        elif self.velocidad_x < 0:
            self.velocidad_x += 1
        # Colisión con el suelo
        if self.rect.bottom >= alto_pantalla:
            self.rect.bottom = alto_pantalla
            self.velocidad_y = 0
            self.velocidad_x = 0
            self.en_suelo = True
        # Colisión con los bordes
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x + self.rect.width > ancho_pantalla:
            self.rect.x = ancho_pantalla - self.rect.width
