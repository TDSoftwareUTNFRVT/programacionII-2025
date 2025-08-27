# Ayuda PyQt5: Compartir elementos entre ventanas distintas
# ---------------------------------------------------------
#
# Teoría detallada:
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

# Primero definimos la ventana secundaria


# Ventana secundaria limpia y funcional
class VentanaSecundaria(QWidget):
    def __init__(self, ventana_principal):
        super().__init__()
        self.setWindowTitle("Ventana Secundaria")
        self.setGeometry(450, 100, 200, 100)
        self.ventana_principal = ventana_principal  # Guardar la referencia

        layout = QVBoxLayout()

        boton_incrementar = QPushButton("Incrementar contador principal")
        boton_incrementar.clicked.connect(self.incrementar)
        layout.addWidget(boton_incrementar)

        boton_reset_sec = QPushButton("Reset contador principal")
        boton_reset_sec.clicked.connect(self.resetear)
        layout.addWidget(boton_reset_sec)

        self.setLayout(layout)

    def incrementar(self):
        self.ventana_principal.incrementar_contador()

    def resetear(self):
        self.ventana_principal.resetear_contador()

    def incrementar(self):
        # Llama al método de la ventana principal
        self.ventana_principal.incrementar_contador()

    def resetear(self):
        # Llama al método de reset de la ventana principal
        self.ventana_principal.resetear_contador()

# Ahora definimos la ventana principal
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
        # Crear la ventana secundaria y pasarle la referencia a esta ventana
        self.ventana_secundaria = VentanaSecundaria(self)
        boton_abrir = QPushButton("Abrir ventana secundaria")
        boton_abrir.clicked.connect(self.ventana_secundaria.show)
        layout.addWidget(boton_abrir)



    def incrementar_contador(self):
        self.contador += 1
        self.label.setText(f"Contador: {self.contador}")

    def resetear_contador(self):
        self.contador = 0
        self.label.setText(f"Contador: {self.contador}")
        self.setLayout(layout)

        boton_incrementar = QPushButton("Incrementar contador principal")
        boton_incrementar.clicked.connect(self.incrementar)
        layout.addWidget(boton_incrementar)

        # Botón Reset en la ventana secundaria
        boton_reset_sec = QPushButton("Reset contador principal")
        boton_reset_sec.clicked.connect(self.resetear)
        layout.addWidget(boton_reset_sec)

    def incrementar(self):
        # Llama al método de la ventana principal
        self.ventana_principal.incrementar_contador()

    def resetear(self):
        # Llama al método de reset de la ventana principal
        self.ventana_principal.resetear_contador()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())

# Resumen:
# --------
# - Se crea la ventana secundaria pasándole como argumento la ventana principal.
# - La ventana secundaria guarda esa referencia y puede llamar métodos o modificar atributos de la principal.
# - Así, puedes compartir y manipular datos entre ventanas de forma sencilla.
#
# Este patrón se puede aplicar a cualquier tipo de interacción entre ventanas en PyQt5.
