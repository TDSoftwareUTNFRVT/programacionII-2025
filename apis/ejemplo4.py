import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLabel, QMessageBox

# Función para obtener episodios de la API de Rick and Morty

def obtener_episodios():
    url = "https://rickandmortyapi.com/api/episode"
    episodios = []
    pagina = 1
    while True:
        params = {"page": pagina}
        resp = requests.get(url, params=params)
        if resp.status_code != 200:
            break
        datos = resp.json()
        episodios.extend(datos.get("results", []))
        if datos.get("info", {}).get("next"):
            pagina += 1
        else:
            break
    return episodios

class VentanaEpisodios(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Episodios de Rick and Morty")
        self.setGeometry(100, 100, 500, 400)
        layout = QVBoxLayout()
        self.lista = QListWidget()
        self.detalle = QLabel("Selecciona un episodio para ver detalles.")
        self.btn_cargar = QPushButton("Cargar episodios")
        self.btn_cargar.clicked.connect(self.cargar_episodios)
        self.lista.currentItemChanged.connect(self.mostrar_detalle)
        layout.addWidget(self.btn_cargar)
        layout.addWidget(self.lista)
        layout.addWidget(self.detalle)
        self.setLayout(layout)
        self.episodios = []

    def cargar_episodios(self):
        self.lista.clear()
        self.episodios = obtener_episodios()
        if not self.episodios:
            QMessageBox.warning(self, "Error", "No se pudieron obtener los episodios.")
            return
        for ep in self.episodios:
            self.lista.addItem(f"{ep['episode']} - {ep['name']}")

    def mostrar_detalle(self):
        idx = self.lista.currentRow()
        if idx < 0 or idx >= len(self.episodios):
            self.detalle.setText("Selecciona un episodio para ver detalles.")
            return
        ep = self.episodios[idx]
        texto = f"<b>{ep['episode']} - {ep['name']}</b><br>Fecha: {ep['air_date']}<br>Personajes: {len(ep['characters'])}"
        self.detalle.setText(texto)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaEpisodios()
    ventana.show()
    sys.exit(app.exec_())
