import random

class Casilla:
    def __init__(self, numero, accion=None):
        self.numero = numero
        self.accion = accion

    def ejecutar_accion(self, personaje, personajes):
        if self.accion:
            self.accion(personaje, personajes)

class Tablero:
    def __init__(self):
        self.casillas = self.crear_casillas()

    def crear_casillas(self):
        acciones = [
            None,
            lambda personaje, personajes: print(f"Nada sucede en la casilla 1"),
            lambda personaje, personajes: print(f"Nada sucede en la casilla 2"),
            lambda personaje, personajes: print(f"Pierde 1 turno"),
            lambda personaje, personajes: setattr(personaje, 'pierde_turno', True),
            lambda personaje, personajes: print(f"Avanza 5 casillas") or personaje.avanzar(5),
            lambda personaje, personajes: print(f"Vuelve al inicio") or personaje.ir_a(0),
            lambda personaje, personajes: print(f"Sigue hasta el final") or personaje.ir_a(14),
            lambda personaje, personajes: print(f"Nada sucede en la casilla 8"),
            lambda personaje, personajes: print(f"Vaya a la misma casilla del primero") or personaje.ir_a(max(personajes, key=lambda p: p.posicion).posicion),
            lambda personaje, personajes: print(f"Nada sucede en la casilla 10"),
            lambda personaje, personajes: print(f"Pierde 1 turno") or setattr(personaje, 'pierde_turno', True),
            lambda personaje, personajes: print(f"Avanza 3 casillas") or personaje.avanzar(3),
            lambda personaje, personajes: print(f"Nada sucede en la casilla 13"),
            lambda personaje, personajes: print(f"Vuelve al inicio") or personaje.ir_a(0),
            lambda personaje, personajes: print(f"Nada sucede en la casilla 15")
        ]
        return [Casilla(numero, acciones[numero]) for numero in range(15)]

    def mostrar_tablero(self, personajes):
        print("\nTablero:")
        for numero, casilla in enumerate(self.casillas):
            ocupantes = []
            for personaje in personajes:
                if personaje.posicion == numero:
                    ocupantes.append(personaje.nombre)
            if ocupantes:
                print(f"Casilla {numero}: {', '.join(ocupantes)})")
            else:
                print(f"Casilla {numero}: -")
