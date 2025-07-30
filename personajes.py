class Personaje:
    def __init__(self, nombre:str, fuerza:int, inteligencia:int, defensa:int):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = 100

    def getFuerza(self):
        print(f'La Fuerza de {self.nombre} es de {self.fuerza}')

    def getValorFuerza(self):
        return self.fuerza
    
    def getValorDefensa(self):
        return self.defensa

    def __str__(self):
        print(f'Nombre del personaje {self.nombre}')
        print(f'Fuerza actual {self.fuerza}')
        print(f'Inteligencia actual: {self.inteligencia}')
        print(f'Defensa actual: {self.defensa}')
        print(f'Vida actual {self.vida}')

    def subir_nivel(self, fuerza: int, inteligencia: int, defensa: int):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(f'{self.nombre} ha muerto. GAME OVER!')

    def danio(self, enemigo):
        return self.fuerza - enemigo.getValorDefensa()
    
    def atacar(self, enemigo):
        danio = self.danio(enemigo)
        enemigo.vida = enemigo.vida - danio
        if enemigo.esta_vivo():
            print('El daño no fue letal!!')
        else:
            enemigo.morir()


personaje_1 = Personaje('Goku', 10, 5, 25)
enemigo = Personaje('Freeze', 10, 5, 5)

print(personaje_1.danio(enemigo))



