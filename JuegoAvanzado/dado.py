import random
import time
import os

def limpia_console():
    os.system('cls' if os.name == 'nt' else 'clear')

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
    for _ in range(10):
        cara = random.randint(1, 6)
        limpia_console()
        for line in dado_caras[cara]:
            print(line)
        time.sleep(0.1)
    return cara
