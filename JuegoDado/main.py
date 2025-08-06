from personaje import Personaje
from dado import animacion_dado


def main():
    jugador1 = Personaje("César", turno=1)
    jugador2 = Personaje("Mariana", turno=2)

    print("¡Comienza la carrera hasta la casilla 10!")
    # Aquí continúa la lógica del juego...

    resultado = animacion_dado()

    print(f"\n¡Salió el número {resultado}!")
   

if __name__ == "__main__":
    main()