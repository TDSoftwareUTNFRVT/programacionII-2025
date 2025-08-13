class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.posicion = 0
        self.pierde_turno = False

    def avanzar(self, cantidad):
        self.posicion += cantidad
        if self.posicion > 14:
            self.posicion = 14

    def ir_a(self, casilla):
        self.posicion = casilla

    def mostrar_estado(self):
        print(f"{self.nombre} está en la casilla {self.posicion}")
