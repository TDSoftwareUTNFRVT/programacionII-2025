class Taza:
    def __init__(self):
        self.__volumen = 0
        self.__liquido = ''
        self.__color = ''

    def getColor(self):
        print(self.__color)

    def getVolumen(self):
        print(self.__volumen)

    def getLiquido(self):
        print('este objeto contiene ',self.__liquido)
    
    def setLiquido(self):
        liquido = input('Ingrese el liquido: ')
        self.__liquido = liquido

pocillo = Taza()
pocillo.setLiquido()
pocillo.getLiquido()