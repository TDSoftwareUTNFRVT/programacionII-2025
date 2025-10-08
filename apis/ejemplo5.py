import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLabel, QHBoxLayout, QScrollArea, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import io

# Función para obtener personajes de la API de Rick and Morty

def obtener_personajes():
    url = "https://rickandmortyapi.com/api/character"
    personajes = []
    pagina = 1
    while True:
        params = {"page": pagina}
        resp = requests.get(url, params=params)
        if resp.status_code != 200:
            break
        datos = resp.json()
        personajes.extend(datos.get("results", []))
        if datos.get("info", {}).get("next"):
            pagina += 1
        else:
            break
    return personajes

class VentanaPersonajes(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Personajes de Rick and Morty")
        self.setGeometry(100, 100, 600, 500)
        layout = QVBoxLayout()
        self.lista = QListWidget()
        self.detalle = QLabel("Selecciona un personaje para ver detalles.")
        self.detalle.setWordWrap(True)
        self.imagen = QLabel()
        self.imagen.setAlignment(Qt.AlignCenter)
        self.btn_cargar = QPushButton("Cargar personajes")
        self.btn_cargar.clicked.connect(self.cargar_personajes)
        self.lista.currentItemChanged.connect(self.mostrar_detalle)
        layout.addWidget(self.btn_cargar)
        layout.addWidget(self.lista)
        layout.addWidget(self.imagen)
        layout.addWidget(self.detalle)
        self.setLayout(layout)
        self.personajes = []

    def cargar_personajes(self):
        self.lista.clear()
        self.personajes = obtener_personajes()
        if not self.personajes:
            QMessageBox.warning(self, "Error", "No se pudieron obtener los personajes.")
            return
        for p in self.personajes:
            self.lista.addItem(f"{p['name']}")

    def mostrar_detalle(self):
        idx = self.lista.currentRow()
        if idx < 0 or idx >= len(self.personajes):
            self.detalle.setText("Selecciona un personaje para ver detalles.")
            self.imagen.clear()
            return
        p = self.personajes[idx]
        texto = f"<b>{p['name']}</b><br>Estado: {p['status']}<br>Especie: {p['species']}<br>Género: {p['gender']}<br>Origen: {p['origin']['name']}"
        self.detalle.setText(texto)
        # Descargar y mostrar imagen
        img_url = p['image']
        try:
            img_data = requests.get(img_url).content
            pixmap = QPixmap()
            pixmap.loadFromData(img_data)
            self.imagen.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        except Exception:
            self.imagen.setText("No se pudo cargar la imagen.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPersonajes()
    ventana.show()
    sys.exit(app.exec_())
