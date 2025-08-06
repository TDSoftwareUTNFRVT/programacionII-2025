import random
import time
import os

# Opcional: limpia la consola (funciona en Windows y Unix)
def limpia_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Dibujo de los dados del 1 al 6
dado_caras = {
    1: ["+-------+",
        "|       |",
        "|   o   |",
        "|       |",
        "+-------+"],
    2: ["+-------+",
        "| o     |",
        "|       |",
        "|     o |",
        "+-------+"],
    3: ["+-------+",
        "| o     |",
        "|   o   |",
        "|     o |",
        "+-------+"],
    4: ["+-------+",
        "| o   o |",
        "|       |",
        "| o   o |",
        "+-------+"],
    5: ["+-------+",
        "| o   o |",
        "|   o   |",
        "| o   o |",
        "+-------+"],
    6: ["+-------+",
        "| o   o |",
        "| o   o |",
        "| o   o |",
        "+-------+"]
}

def animacion_dado():
    for _ in range(10):  # cantidad de veces que simula rodar
        cara = random.randint(1, 6)
        limpia_console()
        for line in dado_caras[cara]:
            print(line)
        time.sleep(0.1)  # velocidad del "rodado"
    return cara

# # Programa principal
# print("Rodando el dado...")
# time.sleep(1)
# resultado = animacion_dado()
# print(f"\n¡Salió el número {resultado}!")
