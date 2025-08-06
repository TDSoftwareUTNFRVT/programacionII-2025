import random
import time

# Clase Personaje
class Personaje:
    def __init__(self, nombre, turno):
        self.nombre = nombre
        self.turno = turno
        self.posicion = 0

    def avanzar(self, cantidad):
        self.posicion += cantidad
        if self.posicion > 10:
            self.posicion = 10  # No pasa del final

    def mostrar_estado(self):
        print(f"{self.nombre} está en la casilla {self.posicion}")

# Función para tirar el dado
def tirar_dado():
    return random.randint(1, 6)

# Crear personajes
jugador1 = Personaje("🐱 Gato", turno=1)
jugador2 = Personaje("🐶 Perro", turno=2)

# Iniciar el juego
print("¡Comienza la carrera hasta la casilla 10!\n")
time.sleep(1)

juego_terminado = False

while not juego_terminado:
    for jugador in [jugador1, jugador2]:
        input(f"Turno de {jugador.nombre}. Presiona ENTER para tirar el dado...")
        dado = tirar_dado()
        print(f"{jugador.nombre} tiró un {dado}")
        jugador.avanzar(dado)
        jugador.mostrar_estado()
        print("-" * 30)
        time.sleep(1)

        if jugador.posicion >= 10:
            print(f"🎉 ¡{jugador.nombre} ha llegado a la meta y ganó!")
            juego_terminado = True
            break
 
 