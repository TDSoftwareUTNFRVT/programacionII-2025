import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLabel, QLineEdit, QComboBox, QSpinBox, QMessageBox, QFrame
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

API_URL = "https://rickandmortyapi.com/api/character"

class CardPersonaje(QFrame):
    def __init__(self, personaje):
        super().__init__()
        self.setFrameShape(QFrame.Box)
        self.setLineWidth(2)
        self.setStyleSheet("background-color: #e6f7ff; border-radius: 12px; border: 2px solid #8ecae6;")
        self.layout_card = QHBoxLayout()
        self.img = QLabel()
        self.img.setFixedSize(140, 140)
        self.img.setAlignment(Qt.AlignCenter)
        self.info = QLabel()
        self.info.setFont(QFont("Arial", 11))
        self.info.setWordWrap(True)
        self.layout_card.addWidget(self.img)
        self.layout_card.addWidget(self.info)
        self.setLayout(self.layout_card)
        self.actualizar(personaje)

    def actualizar(self, personaje):
        # Actualiza la imagen y los datos del personaje
        if personaje.get('image'):
            try:
                img_data = requests.get(personaje['image']).content
                pixmap = QPixmap()
                pixmap.loadFromData(img_data)
                self.img.setPixmap(pixmap.scaled(140, 140, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            except Exception:
                self.img.setText("Sin imagen")
        else:
            self.img.clear()
            self.img.setText("Sin imagen")
        self.info.setText(
            f"<div style='padding:8px;'>"
            f"<span style='font-size:16px;'><b>{personaje.get('name','-')}</b></span><br>"
            f"<b>Estado:</b> {personaje.get('status','-')}<br>"
            f"<b>Especie:</b> {personaje.get('species','-')}<br>"
            f"<b>Género:</b> {personaje.get('gender','-')}<br>"
            f"<b>Origen:</b> {personaje.get('origin',{}).get('name','-')}"
            f"</div>"
        )

class VentanaPersonajes(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Personajes de Rick and Morty - Filtros y Paginación")
        self.setGeometry(100, 100, 700, 600)
        main_layout = QVBoxLayout()
        # Filtros
        filtro_layout = QHBoxLayout()
        self.txt_nombre = QLineEdit()
        self.txt_nombre.setPlaceholderText("Filtrar por nombre...")
        self.cmb_estado = QComboBox()
        self.cmb_estado.addItems(["", "Alive", "Dead", "unknown"])
        self.cmb_especie = QLineEdit()
        self.cmb_especie.setPlaceholderText("Filtrar por especie...")
        self.btn_filtrar = QPushButton("Filtrar")
        self.btn_filtrar.clicked.connect(self.cargar_personajes)
        filtro_layout.addWidget(QLabel("Nombre:"))
        filtro_layout.addWidget(self.txt_nombre)
        filtro_layout.addWidget(QLabel("Estado:"))
        filtro_layout.addWidget(self.cmb_estado)
        filtro_layout.addWidget(QLabel("Especie:"))
        filtro_layout.addWidget(self.cmb_especie)
        filtro_layout.addWidget(self.btn_filtrar)
        main_layout.addLayout(filtro_layout)
        # Paginación
        pag_layout = QHBoxLayout()
        self.spin_pagina = QSpinBox()
        self.spin_pagina.setMinimum(1)
        self.spin_pagina.setValue(1)
        self.lbl_total = QLabel("Total páginas: ?")
        self.btn_prev = QPushButton("Anterior")
        self.btn_next = QPushButton("Siguiente")
        self.btn_prev.clicked.connect(self.pagina_anterior)
        self.btn_next.clicked.connect(self.pagina_siguiente)
        pag_layout.addWidget(QLabel("Página:"))
        pag_layout.addWidget(self.spin_pagina)
        pag_layout.addWidget(self.btn_prev)
        pag_layout.addWidget(self.btn_next)
        pag_layout.addWidget(self.lbl_total)
        main_layout.addLayout(pag_layout)
        # Lista y card
        self.lista = QListWidget()
        self.lista.currentItemChanged.connect(self.mostrar_detalle)
        main_layout.addWidget(self.lista)
        self.card = CardPersonaje({"name":"-","status":"-","species":"-","gender":"-","origin":{"name":"-"},"image":""})
        main_layout.addWidget(self.card, alignment=Qt.AlignCenter)
        self.setLayout(main_layout)
        self.personajes = []
        self.total_paginas = 1
        self.cargar_personajes()

    def cargar_personajes(self):
        self.lista.clear()
        params = {
            "page": self.spin_pagina.value(),
            "name": self.txt_nombre.text(),
            "status": self.cmb_estado.currentText(),
            "species": self.cmb_especie.text()
        }
        params = {k: v for k, v in params.items() if v}
        resp = requests.get(API_URL, params=params)
        if resp.status_code != 200:
            QMessageBox.warning(self, "Error", "No se pudieron obtener los personajes.")
            self.lbl_total.setText("Total páginas: ?")
            self.personajes = []
            self.card.actualizar({"name":"-","status":"-","species":"-","gender":"-","origin":{"name":"-"},"image":""})
            return
        datos = resp.json()
        self.personajes = datos.get("results", [])
        self.total_paginas = datos.get("info", {}).get("pages", 1)
        self.lbl_total.setText(f"Total páginas: {self.total_paginas}")
        for p in self.personajes:
            self.lista.addItem(f"{p['name']}")
        if self.personajes:
            self.lista.setCurrentRow(0)
        else:
            self.card.actualizar({"name":"-","status":"-","species":"-","gender":"-","origin":{"name":"-"},"image":""})

    def mostrar_detalle(self):
        idx = self.lista.currentRow()
        if idx < 0 or idx >= len(self.personajes):
            self.card.actualizar({"name":"-","status":"-","species":"-","gender":"-","origin":{"name":"-"},"image":""})
            return
        p = self.personajes[idx]
        self.card.actualizar(p)

    def pagina_anterior(self):
        if self.spin_pagina.value() > 1:
            self.spin_pagina.setValue(self.spin_pagina.value() - 1)
            self.cargar_personajes()

    def pagina_siguiente(self):
        if self.spin_pagina.value() < self.total_paginas:
            self.spin_pagina.setValue(self.spin_pagina.value() + 1)
            self.cargar_personajes()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPersonajes()
    ventana.show()
    sys.exit(app.exec_())
