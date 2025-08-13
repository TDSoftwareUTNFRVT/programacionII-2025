
import pygame  # Librería principal para juegos 2D
import sys     # Para salir del programa
from spider import Spider  # Clase Spider modularizada
import random  # Para posiciones y alturas aleatorias

# Inicializar pygame
pygame.init()

ANCHO, ALTO = 800, 600  # Tamaño de la ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))  # Crear ventana
pygame.display.set_caption('Spider: Salta Obstáculos')  # Título
BLANCO = (255, 255, 255)  # Color de fondo
ROJO = (255, 0, 0)        # Color de los obstáculos

# Clase para los obstáculos
class Obstaculo:

    def __init__(self, x, y, ancho=40, alto=60, velocidad=5):
        self.ancho = ancho  # Ancho del obstáculo
        self.alto = alto    # Alto del obstáculo
        self.rect = pygame.Rect(x, y - alto, ancho, alto)  # Rectángulo para colisiones y dibujo
        self.color = ROJO
        self.velocidad = velocidad  # Velocidad de desplazamiento

    def mover(self):
        self.rect.x -= self.velocidad  # Mover a la izquierda
        # Si sale de la pantalla, reaparece a la derecha con altura aleatoria
        if self.rect.right < 0:
            self.alto = random.randint(40, 120)
            self.rect.height = self.alto
            self.rect.x = ANCHO + random.randint(0, 200)
            self.rect.y = ALTO - self.alto

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, self.rect)

# Variables globales para doble salto y puntaje
TIEMPO_DOBLE_SALTO = 250  # milisegundos

def reiniciar_juego():
    global spider, obstaculos, doble_salto_disponible, ultimo_salto, puntaje
    spider = Spider(0, ALTO)  # Crear el personaje en la esquina inferior izquierda
    # Crear obstáculos con posiciones y alturas aleatorias
    obstaculos = [Obstaculo(random.randint(200, ANCHO-60), ALTO, 40, random.randint(40, 120)) for _ in range(5)]
    doble_salto_disponible = True  # Permitir doble salto al inicio
    ultimo_salto = 0  # Tiempo del último salto
    puntaje = 0  # Puntaje inicial

reiniciar_juego()

reloj = pygame.time.Clock()  # Controla los FPS
ejecutando = True           # Controla el bucle principal
game_over = False           # Estado del juego

# Bucle principal del juego
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if not game_over:
                if evento.key == pygame.K_UP:
                    ahora = pygame.time.get_ticks()
                    if spider.en_suelo:
                        spider.saltar()
                        doble_salto_disponible = True
                        ultimo_salto = ahora
                    elif doble_salto_disponible and ahora - ultimo_salto < TIEMPO_DOBLE_SALTO:
                        spider.velocidad_y = spider.SALTO * 1.5  # salto más alto
                        doble_salto_disponible = False
                if evento.key == pygame.K_RIGHT:
                    if spider.en_suelo:
                        spider.saltar_adelante()
                if evento.key == pygame.K_LEFT:
                    if spider.en_suelo:
                        # Salto hacia atrás
                        spider.velocidad_y = spider.SALTO
                        spider.velocidad_x = -spider.SALTO_X
                        spider.en_suelo = False
            else:
                # Reiniciar juego al presionar cualquier tecla
                reiniciar_juego()
                game_over = False


    if not game_over:
        spider.actualizar(ANCHO, ALTO)
        spider_en_suelo = False
        for obstaculo in obstaculos:
            obstaculo.mover()
            # Verificar si Spider cae sobre el obstáculo
            if (spider.velocidad_y >= 0 and
                spider.rect.bottom <= obstaculo.rect.top + 10 and
                spider.rect.right > obstaculo.rect.left + 5 and
                spider.rect.left < obstaculo.rect.right - 5 and
                spider.rect.bottom + spider.velocidad_y >= obstaculo.rect.top):
                spider.rect.bottom = obstaculo.rect.top
                spider.velocidad_y = 0
                spider.en_suelo = True
                spider_en_suelo = True
            # Si choca de costado o por abajo, termina el juego
            elif spider.rect.colliderect(obstaculo.rect):
                game_over = True
        # Si no está sobre ningún obstáculo ni el suelo, está en el aire
        if not spider_en_suelo and spider.rect.bottom < ALTO:
            spider.en_suelo = False
        # Puntaje: avanzar suma puntos
        if spider.rect.x > 0:
            puntaje = max(puntaje, spider.rect.x)

    pantalla.fill(BLANCO)
    for obstaculo in obstaculos:

        # Bucle principal del juego
        while ejecutando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    ejecutando = False  # Salir del juego
                if evento.type == pygame.KEYDOWN:
                    if not game_over:
                        if evento.key == pygame.K_UP:
                            ahora = pygame.time.get_ticks()
                            # Salto normal si está en el suelo
                            if spider.en_suelo:
                                spider.saltar()
                                doble_salto_disponible = True
                                ultimo_salto = ahora
                            # Doble salto si se pulsa rápido
                            elif doble_salto_disponible and ahora - ultimo_salto < TIEMPO_DOBLE_SALTO:
                                spider.velocidad_y = spider.SALTO * 1.5  # salto más alto
                                doble_salto_disponible = False
                        if evento.key == pygame.K_RIGHT:
                            if spider.en_suelo:
                                spider.saltar_adelante()  # Salto parabólico hacia adelante
                        if evento.key == pygame.K_LEFT:
                            if spider.en_suelo:
                                # Salto hacia atrás
                                spider.velocidad_y = spider.SALTO
                                spider.velocidad_x = -spider.SALTO_X
                                spider.en_suelo = False
                    else:
                        # Reiniciar juego al presionar cualquier tecla
                        reiniciar_juego()
                        game_over = False

            if not game_over:
                spider.actualizar(ANCHO, ALTO)  # Actualiza posición y física del personaje
                spider_en_suelo = False
                for obstaculo in obstaculos:
                    obstaculo.mover()  # Mover obstáculo de derecha a izquierda
                    # Verificar si Spider cae sobre el obstáculo
                    if (spider.velocidad_y >= 0 and
                        spider.rect.bottom <= obstaculo.rect.top + 10 and
                        spider.rect.right > obstaculo.rect.left + 5 and
                        spider.rect.left < obstaculo.rect.right - 5 and
                        spider.rect.bottom + spider.velocidad_y >= obstaculo.rect.top):
                        # Spider aterriza sobre el obstáculo
                        spider.rect.bottom = obstaculo.rect.top
                        spider.velocidad_y = 0
                        spider.en_suelo = True
                        spider_en_suelo = True
                    # Si choca de costado o por abajo, termina el juego
                    elif spider.rect.colliderect(obstaculo.rect):
                        game_over = True
                # Si no está sobre ningún obstáculo ni el suelo, está en el aire
                if not spider_en_suelo and spider.rect.bottom < ALTO:
                    spider.en_suelo = False
                # Puntaje: avanzar suma puntos
                if spider.rect.x > 0:
                    puntaje = max(puntaje, spider.rect.x)

            pantalla.fill(BLANCO)  # Limpiar pantalla
            for obstaculo in obstaculos:
                obstaculo.dibujar(pantalla)  # Dibujar cada obstáculo
            pantalla.blit(spider.imagen, spider.rect)  # Dibujar personaje
            # Mostrar puntaje
            fuente = pygame.font.SysFont(None, 36)
            texto = fuente.render(f'Puntaje: {puntaje}', True, (0,0,0))
            pantalla.blit(texto, (10, 10))
            if game_over:
                texto2 = fuente.render('¡Game Over! Presiona cualquier tecla para reiniciar', True, (200,0,0))
                pantalla.blit(texto2, (ANCHO//2-250, ALTO//2))
            pygame.display.flip()  # Actualizar pantalla
            reloj.tick(60)         # Limitar a 60 FPS

        pygame.quit()  # Cerrar Pygame
        sys.exit()     # Salir del programa