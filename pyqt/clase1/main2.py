import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont, QPalette, QColor

# Crear la aplicación principal de PyQt5
app = QApplication(sys.argv)  # Inicializa la aplicación Qt

# Crear la ventana principal
ventana = QWidget()  # Crea el widget principal (ventana)
ventana.setWindowTitle("Ventana con Layout Vertical")  # Establece el título de la ventana
ventana.setGeometry(100, 100, 400, 200)  # Posición (x, y) y tamaño (ancho, alto)

# Configurar color de fondo usando paleta
paleta = QPalette()  # Crea una paleta de colores
paleta.setColor(QPalette.Window, QColor("#FFF8E1"))  # Define el color de fondo (amarillo claro)
ventana.setPalette(paleta)  # Asigna la paleta a la ventana
ventana.setAutoFillBackground(True)  # Aplica el color de fondo personalizado

# Crear un layout vertical para organizar los widgets
layout = QVBoxLayout()  # Crea un layout vertical (de arriba hacia abajo)

# Crear una etiqueta (QLabel) con formato
etiqueta = QLabel("¡Bienvenido con Layout!")  # Crea una etiqueta de texto
etiqueta.setFont(QFont("Arial", 16, QFont.Bold))  # Establece fuente, tamaño y negrita
etiqueta.setStyleSheet("color: #6A1B9A")  # Cambia el color del texto
layout.addWidget(etiqueta)  # Agrega la etiqueta al layout

# Crear un botón (QPushButton) con formato
boton = QPushButton("Aceptar")  # Crea un botón con el texto "Aceptar"
boton.setFont(QFont("Arial", 12))  # Establece la fuente y tamaño del botón
boton.setStyleSheet("background-color: #8BC34A; color: white;")  # Color de fondo y texto del botón
layout.addWidget(boton)  # Agrega el botón al layout

boton.clicked.connect(app.quit)  # Conecta el clic del botón para cerrar la app

ventana.setLayout(layout)  # Asigna el layout vertical a la ventana
ventana.show()  # Muestra la ventana en pantalla
sys.exit(app.exec_())  # Ejecuta el bucle principal de la aplicación
