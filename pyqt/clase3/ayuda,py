# Ayuda PyQt5: Interacción y paso de información entre dos ventanas
# ------------------------------------------------------------------
#
# Teoría
# ======================================
#
# En PyQt5, es común tener una ventana principal y una ventana de herramientas.
# Para que ambas interactúen y compartan información, la forma más directa es:
#
# 1. Crear la ventana secundaria (herramientas) pasándole como argumento la instancia de la ventana principal.
# 2. Guardar esa referencia en la secundaria para poder llamar métodos o modificar atributos de la principal.
# 3. Así, la ventana de herramientas puede modificar el estado de la principal (y viceversa si se desea).
#
# Ventajas:
# - Es simple, directo y muy útil para aplicaciones pequeñas y medianas.
# - Permite manipular widgets y datos de una ventana desde otra.
#
# Ejemplo práctico: Contador compartido entre dos ventanas
# -------------------------------------------------------
# Ventana principal: muestra el valor de un contador.
# Ventana de herramientas: tiene botones para incrementar y resetear el contador de la principal.
#
# Código completo y comentado:

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Principal")
        self.setGeometry(100, 100, 300, 150)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.contador = 0
        self.label = QLabel(f"Contador: {self.contador}")
        layout.addWidget(self.label)
        # Crear la ventana de herramientas y pasarle la referencia a esta ventana
        self.ventana_herramientas = VentanaHerramientas(self)
        boton_abrir = QPushButton("Abrir herramientas")
        boton_abrir.clicked.connect(self.ventana_herramientas.show)
        layout.addWidget(boton_abrir)

    def incrementar_contador(self):
        self.contador += 1
        self.label.setText(f"Contador: {self.contador}")

    def resetear_contador(self):
        self.contador = 0
        self.label.setText(f"Contador: {self.contador}")

class VentanaHerramientas(QWidget):
    def __init__(self, ventana_principal):
        super().__init__()
        self.setWindowTitle("Herramientas")
        self.setGeometry(450, 100, 200, 120)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.ventana_principal = ventana_principal  # Guardar la referencia
        # Botón para incrementar el contador de la principal
        boton_inc = QPushButton("Incrementar contador")
        boton_inc.clicked.connect(self.ventana_principal.incrementar_contador)
        layout.addWidget(boton_inc)
        # Botón para resetear el contador de la principal
        boton_reset = QPushButton("Reset contador")
        boton_reset.clicked.connect(self.ventana_principal.resetear_contador)
        layout.addWidget(boton_reset)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())

# Resumen:
# --------
# - Se crea la ventana de herramientas pasándole la principal como argumento.
# - La secundaria puede llamar métodos públicos de la principal.
# - Así, ambas ventanas pueden interactuar y compartir información fácilmente.