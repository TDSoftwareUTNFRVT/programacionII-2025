from personaje import Personaje
from dado import animacion_dado
from tablero import Tablero
import time

MAX_JUGADORES = 6

def obtener_jugadores():
    jugadores = []
    n = 0
    while n < MAX_JUGADORES:
        nombre = input(f"Ingrese el nombre del jugador {n+1} (o ENTER para terminar): ").strip()
        if not nombre:
            break
        jugadores.append(Personaje(nombre))
        n += 1
    return jugadores

def determinar_orden(jugadores):
    tiradas = {}
    print("\nTirando el dado para determinar el orden...")
    for jugador in jugadores:
        input(f"{jugador.nombre}, presiona ENTER para tirar el dado...")
        tirada = animacion_dado()
        print(f"{jugador.nombre} sacó un {tirada}")
        tiradas[jugador] = tirada
        time.sleep(1)
    orden = sorted(jugadores, key=lambda j: tiradas[j], reverse=True)
    print("\nOrden de juego:")
    for i, jugador in enumerate(orden):
        print(f"{i+1}. {jugador.nombre} (dado: {tiradas[jugador]})")
    return orden

def main():
    print("Bienvenido al Juego Avanzado!")
    jugadores = obtener_jugadores()
    if len(jugadores) < 2:
        print("Se necesitan al menos 2 jugadores.")
        return
    orden = determinar_orden(jugadores)
    tablero = Tablero()
    ganador = None
    while not ganador:
        for jugador in orden:
            if jugador.pierde_turno:
                print(f"{jugador.nombre} pierde este turno!")
                jugador.pierde_turno = False
                continue
            input(f"\nTurno de {jugador.nombre}. Presiona ENTER para tirar el dado...")
            tirada = animacion_dado()
            print(f"{jugador.nombre} avanza {tirada} casillas.")
            jugador.avanzar(tirada)
            tablero.casillas[jugador.posicion].ejecutar_accion(jugador, orden)
            jugador.mostrar_estado()
            tablero.mostrar_tablero(orden)
            if jugador.posicion == 14:
                ganador = jugador
                print(f"\n🎉 ¡{jugador.nombre} ha llegado a la meta y ganó!")
                break
            time.sleep(1.5)

if __name__ == "__main__":
    main()
