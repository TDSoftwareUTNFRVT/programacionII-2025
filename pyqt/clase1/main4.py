import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont, QPalette, QColor

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Primera Ventana PyQt5")  # Título de la ventana
        self.setGeometry(100, 100, 400, 200)             # Posición y tamaño

        # Configurar color de fondo
        paleta = QPalette()
        paleta.setColor(QPalette.Window, QColor("#E0F7FA"))
        self.setPalette(paleta)
        self.setAutoFillBackground(True)

        # Crear layout vertical
        layout = QVBoxLayout()

        # Etiqueta con formato
        etiqueta = QLabel("¡Bienvenido a PyQt5!")
        etiqueta.setFont(QFont("Arial", 16, QFont.Bold))
        etiqueta.setStyleSheet("color: #00796B")
        layout.addWidget(etiqueta)

        # Botón aceptar
        boton = QPushButton("Aceptar")
        boton.setFont(QFont("Arial", 12))
        boton.setStyleSheet("background-color: #4CAF50; color: white;")
        boton.clicked.connect(QApplication.instance().quit)
        layout.addWidget(boton)

        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
