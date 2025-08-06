class Personaje:
    def __init__(self, nombre, turno):
        self.nombre = nombre
        self.turno = turno
        self.posicion = 0

    def avanzar(self, cantidad):
        self.posicion += cantidad
        if self.posicion > 10:
            self.posicion = 10

    def mostrar_estado(self):
        print(f"{self.nombre} está en la casilla {self.posicion}")