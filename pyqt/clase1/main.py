import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QFont, QPalette, QColor

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Mi Primera Ventana PyQt5")
ventana.setGeometry(100, 100, 400, 200)

paleta = QPalette()
paleta.setColor(QPalette.Window, QColor("#E0F7FA"))
ventana.setPalette(paleta)
ventana.setAutoFillBackground(True)

etiqueta = QLabel("¡Bienvenido a PyQt5!", ventana)
etiqueta.setFont(QFont("Arial", 16, QFont.Bold))
etiqueta.setStyleSheet("color: #00796B")
etiqueta.move(80, 40)

boton = QPushButton("Aceptar", ventana)
boton.setFont(QFont("Arial", 12))
boton.setStyleSheet("background-color: #4CAF50; color: white;")
boton.move(150, 120)
boton.clicked.connect(app.quit)

ventana.show()
sys.exit(app.exec_())
