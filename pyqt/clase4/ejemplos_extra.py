# Ejemplos adicionales de PyQt5: Diálogos avanzados y widgets especiales
# ------------------------------------------------------------------------
#
# Este archivo complementa la clase 4 con ejemplos adicionales de diálogos
# y widgets que no están en el ejercicio principal pero son muy útiles.

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
                             QPushButton, QWidget, QLabel, QLineEdit, QTextEdit,
                             QColorDialog, QFontDialog, QInputDialog, QProgressDialog,
                             QDialog, QDialogButtonBox, QFormLayout, QSpinBox,
                             QComboBox, QCheckBox, QSlider, QGroupBox, QTabWidget)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor, QFont, QPalette

class VentanaEjemplos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 - Diálogos y Widgets Avanzados")
        self.setGeometry(100, 100, 600, 500)
        
        # Widget central con pestañas
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        
        # Crear las diferentes pestañas
        self.crear_tab_dialogos()
        self.crear_tab_input()
        self.crear_tab_progress()
        self.crear_tab_custom()
    
    def crear_tab_dialogos(self):
        """Pestaña con diálogos estándar"""
        tab = QWidget()
        layout = QVBoxLayout()
        
        # Título
        titulo = QLabel("Diálogos Estándar de PyQt5")
        titulo.setStyleSheet("font-size: 16px; font-weight: bold; margin: 10px;")
        layout.addWidget(titulo)
        
        # Botones para diferentes diálogos
        btn_color = QPushButton("Seleccionar Color")
        btn_color.clicked.connect(self.seleccionar_color)
        layout.addWidget(btn_color)
        
        btn_fuente = QPushButton("Seleccionar Fuente")
        btn_fuente.clicked.connect(self.seleccionar_fuente)
        layout.addWidget(btn_fuente)
        
        btn_info = QPushButton("Mostrar Información")
        btn_info.clicked.connect(self.mostrar_info)
        layout.addWidget(btn_info)
        
        btn_advertencia = QPushButton("Mostrar Advertencia")
        btn_advertencia.clicked.connect(self.mostrar_advertencia)
        layout.addWidget(btn_advertencia)
        
        btn_error = QPushButton("Mostrar Error")
        btn_error.clicked.connect(self.mostrar_error)
        layout.addWidget(btn_error)
        
        btn_pregunta = QPushButton("Hacer Pregunta")
        btn_pregunta.clicked.connect(self.hacer_pregunta)
        layout.addWidget(btn_pregunta)
        
        # Área para mostrar resultados
        self.resultado_label = QLabel("Resultados aparecerán aquí...")
        self.resultado_label.setStyleSheet("background-color: #f0f0f0; padding: 10px; margin: 10px;")
        self.resultado_label.setWordWrap(True)
        layout.addWidget(self.resultado_label)
        
        layout.addStretch()
        tab.setLayout(layout)
        self.tabs.addTab(tab, "Diálogos")
    
    def crear_tab_input(self):
        """Pestaña con diálogos de entrada"""
        tab = QWidget()
        layout = QVBoxLayout()
        
        titulo = QLabel("Diálogos de Entrada de Datos")
        titulo.setStyleSheet("font-size: 16px; font-weight: bold; margin: 10px;")
        layout.addWidget(titulo)
        
        btn_texto = QPushButton("Pedir Texto")
        btn_texto.clicked.connect(self.pedir_texto)
        layout.addWidget(btn_texto)
        
        btn_numero = QPushButton("Pedir Número Entero")
        btn_numero.clicked.connect(self.pedir_numero)
        layout.addWidget(btn_numero)
        
        btn_decimal = QPushButton("Pedir Número Decimal")
        btn_decimal.clicked.connect(self.pedir_decimal)
        layout.addWidget(btn_decimal)
        
        btn_lista = QPushButton("Seleccionar de Lista")
        btn_lista.clicked.connect(self.seleccionar_lista)
        layout.addWidget(btn_lista)
        
        # Área para mostrar resultados
        self.resultado_input = QLabel("Los valores ingresados aparecerán aquí...")
        self.resultado_input.setStyleSheet("background-color: #e8f5e8; padding: 10px; margin: 10px;")
        self.resultado_input.setWordWrap(True)
        layout.addWidget(self.resultado_input)
        
        layout.addStretch()
        tab.setLayout(layout)
        self.tabs.addTab(tab, "Entrada")
    
    def crear_tab_progress(self):
        """Pestaña con diálogos de progreso"""
        tab = QWidget()
        layout = QVBoxLayout()
        
        titulo = QLabel("Diálogos de Progreso")
        titulo.setStyleSheet("font-size: 16px; font-weight: bold; margin: 10px;")
        layout.addWidget(titulo)
        
        btn_progress = QPushButton("Mostrar Barra de Progreso")
        btn_progress.clicked.connect(self.mostrar_progreso)
        layout.addWidget(btn_progress)
        
        btn_progress_indef = QPushButton("Progreso Indefinido")
        btn_progress_indef.clicked.connect(self.mostrar_progreso_indefinido)
        layout.addWidget(btn_progress_indef)
        
        # Información
        info = QLabel("""Los diálogos de progreso son útiles para operaciones largas como:
• Copiar archivos
• Descargas
• Procesamiento de datos
• Cualquier tarea que tome tiempo""")
        info.setStyleSheet("background-color: #fff3cd; padding: 10px; margin: 10px;")
        info.setWordWrap(True)
        layout.addWidget(info)
        
        layout.addStretch()
        tab.setLayout(layout)
        self.tabs.addTab(tab, "Progreso")
    
    def crear_tab_custom(self):
        """Pestaña con diálogo personalizado"""
        tab = QWidget()
        layout = QVBoxLayout()
        
        titulo = QLabel("Diálogo Personalizado")
        titulo.setStyleSheet("font-size: 16px; font-weight: bold; margin: 10px;")
        layout.addWidget(titulo)
        
        btn_custom = QPushButton("Abrir Diálogo de Configuración")
        btn_custom.clicked.connect(self.abrir_dialogo_custom)
        layout.addWidget(btn_custom)
        
        # Área para mostrar configuración actual
        self.config_actual = QLabel("Configuración actual: Sin configurar")
        self.config_actual.setStyleSheet("background-color: #f8f9fa; padding: 10px; margin: 10px; border: 1px solid #ddd;")
        self.config_actual.setWordWrap(True)
        layout.addWidget(self.config_actual)
        
        # Explicación
        explicacion = QLabel("""Un diálogo personalizado permite crear formularios complejos
con múltiples controles y validación personalizada.""")
        explicacion.setStyleSheet("color: #6c757d; margin: 10px;")
        explicacion.setWordWrap(True)
        layout.addWidget(explicacion)
        
        layout.addStretch()
        tab.setLayout(layout)
        self.tabs.addTab(tab, "Personalizado")
    
    # ---- Funciones para diálogos estándar ----
    
    def seleccionar_color(self):
        color = QColorDialog.getColor(Qt.white, self, "Seleccionar color")
        if color.isValid():
            self.resultado_label.setText(f"Color seleccionado: {color.name()}")
            self.resultado_label.setStyleSheet(f"background-color: {color.name()}; padding: 10px; margin: 10px;")
    
    def seleccionar_fuente(self):
        fuente_actual = self.font()
        fuente, ok = QFontDialog.getFont(fuente_actual, self, "Seleccionar fuente")
        if ok:
            self.resultado_label.setFont(fuente)
            self.resultado_label.setText(f"Fuente: {fuente.family()}, Tamaño: {fuente.pointSize()}")
    
    def mostrar_info(self):
        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.information(self, "Información", "Este es un mensaje informativo.")
        self.resultado_label.setText("Se mostró un mensaje de información")
    
    def mostrar_advertencia(self):
        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.warning(self, "Advertencia", "Este es un mensaje de advertencia.")
        self.resultado_label.setText("Se mostró una advertencia")
    
    def mostrar_error(self):
        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.critical(self, "Error", "Este es un mensaje de error.")
        self.resultado_label.setText("Se mostró un mensaje de error")
    
    def hacer_pregunta(self):
        from PyQt5.QtWidgets import QMessageBox
        respuesta = QMessageBox.question(self, "Pregunta", "¿Te gusta PyQt5?",
                                       QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        
        if respuesta == QMessageBox.Yes:
            self.resultado_label.setText("Respuesta: ¡Sí! 😊")
        elif respuesta == QMessageBox.No:
            self.resultado_label.setText("Respuesta: No 😢")
        else:
            self.resultado_label.setText("Respuesta: Cancelado")
    
    # ---- Funciones para entrada de datos ----
    
    def pedir_texto(self):
        texto, ok = QInputDialog.getText(self, 'Entrada de texto', 'Ingresa tu nombre:')
        if ok and texto:
            self.resultado_input.setText(f"Texto ingresado: {texto}")
        else:
            self.resultado_input.setText("Entrada cancelada")
    
    def pedir_numero(self):
        numero, ok = QInputDialog.getInt(self, 'Entrada de número', 'Ingresa tu edad:', 25, 0, 150, 1)
        if ok:
            self.resultado_input.setText(f"Número ingresado: {numero}")
        else:
            self.resultado_input.setText("Entrada cancelada")
    
    def pedir_decimal(self):
        decimal, ok = QInputDialog.getDouble(self, 'Entrada decimal', 'Ingresa tu altura (m):', 1.70, 0.50, 3.00, 2)
        if ok:
            self.resultado_input.setText(f"Decimal ingresado: {decimal:.2f}")
        else:
            self.resultado_input.setText("Entrada cancelada")
    
    def seleccionar_lista(self):
        items = ['Python', 'Java', 'C++', 'JavaScript', 'Go', 'Rust']
        item, ok = QInputDialog.getItem(self, 'Seleccionar elemento', 'Elige tu lenguaje favorito:', items, 0, False)
        if ok and item:
            self.resultado_input.setText(f"Seleccionado: {item}")
        else:
            self.resultado_input.setText("Selección cancelada")
    
    # ---- Funciones para progreso ----
    
    def mostrar_progreso(self):
        progress = QProgressDialog("Procesando archivos...", "Cancelar", 0, 100, self)
        progress.setWindowModality(Qt.WindowModal)
        progress.setWindowTitle("Progreso")
        
        # Simular trabajo con un timer
        self.timer = QTimer()
        self.progreso_actual = 0
        
        def actualizar_progreso():
            self.progreso_actual += 2
            progress.setValue(self.progreso_actual)
            if self.progreso_actual >= 100:
                self.timer.stop()
                progress.close()
        
        self.timer.timeout.connect(actualizar_progreso)
        self.timer.start(100)  # Actualizar cada 100ms
        
        progress.exec_()
    
    def mostrar_progreso_indefinido(self):
        progress = QProgressDialog("Conectando al servidor...", "Cancelar", 0, 0, self)
        progress.setWindowModality(Qt.WindowModal)
        progress.setWindowTitle("Conectando")
        
        # Simular conexión
        self.timer2 = QTimer()
        def cerrar_progreso():
            self.timer2.stop()
            progress.close()
        
        self.timer2.timeout.connect(cerrar_progreso)
        self.timer2.start(3000)  # Cerrar después de 3 segundos
        
        progress.exec_()
    
    # ---- Diálogo personalizado ----
    
    def abrir_dialogo_custom(self):
        dialogo = DialogoConfiguracion(self)
        if dialogo.exec_() == QDialog.Accepted:
            config = dialogo.obtener_configuracion()
            texto_config = f"""Configuración guardada:
• Nombre: {config['nombre']}
• Edad: {config['edad']}
• País: {config['pais']}
• Suscrito: {'Sí' if config['suscrito'] else 'No'}
• Nivel: {config['nivel']}%"""
            self.config_actual.setText(texto_config)

class DialogoConfiguracion(QDialog):
    """Diálogo personalizado para configuración"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Configuración de Usuario")
        self.setModal(True)
        self.resize(400, 300)
        
        # Layout principal
        layout = QVBoxLayout()
        
        # Formulario
        form_layout = QFormLayout()
        
        self.nombre_edit = QLineEdit()
        self.nombre_edit.setPlaceholderText("Ingresa tu nombre")
        form_layout.addRow("Nombre:", self.nombre_edit)
        
        self.edad_spin = QSpinBox()
        self.edad_spin.setRange(1, 150)
        self.edad_spin.setValue(25)
        form_layout.addRow("Edad:", self.edad_spin)
        
        self.pais_combo = QComboBox()
        self.pais_combo.addItems(["Argentina", "Chile", "Uruguay", "Brasil", "Paraguay"])
        form_layout.addRow("País:", self.pais_combo)
        
        self.suscrito_check = QCheckBox("Suscribirse al newsletter")
        form_layout.addRow("Opciones:", self.suscrito_check)
        
        self.nivel_slider = QSlider(Qt.Horizontal)
        self.nivel_slider.setRange(0, 100)
        self.nivel_slider.setValue(50)
        self.nivel_label = QLabel("50%")
        self.nivel_slider.valueChanged.connect(lambda v: self.nivel_label.setText(f"{v}%"))
        
        nivel_layout = QHBoxLayout()
        nivel_layout.addWidget(self.nivel_slider)
        nivel_layout.addWidget(self.nivel_label)
        form_layout.addRow("Nivel de experiencia:", nivel_layout)
        
        # Agrupar el formulario
        grupo = QGroupBox("Información Personal")
        grupo.setLayout(form_layout)
        layout.addWidget(grupo)
        
        # Botones
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.accepted.connect(self.validar_y_aceptar)
        botones.rejected.connect(self.reject)
        layout.addWidget(botones)
        
        self.setLayout(layout)
    
    def validar_y_aceptar(self):
        """Validar datos antes de aceptar"""
        if not self.nombre_edit.text().strip():
            from PyQt5.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Error", "El nombre es obligatorio")
            return
        
        self.accept()
    
    def obtener_configuracion(self):
        """Devolver la configuración como diccionario"""
        return {
            'nombre': self.nombre_edit.text(),
            'edad': self.edad_spin.value(),
            'pais': self.pais_combo.currentText(),
            'suscrito': self.suscrito_check.isChecked(),
            'nivel': self.nivel_slider.value()
        }

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    ventana = VentanaEjemplos()
    ventana.show()
    
    sys.exit(app.exec_())

# ========================================
# Conceptos adicionales cubiertos:
# ========================================
#
# 1. QColorDialog - Selector de colores
# 2. QFontDialog - Selector de fuentes
# 3. QInputDialog - Entrada rápida de datos
# 4. QProgressDialog - Barras de progreso
# 5. QDialog personalizado - Formularios complejos
# 6. QTabWidget - Interfaces con pestañas
# 7. QFormLayout - Layout para formularios
# 8. QGroupBox - Agrupación visual de controles
# 9. QSlider - Control deslizante
# 10. Validación de formularios
#
# Estos elementos complementan el editor de texto y muestran
# la versatilidad de PyQt5 para crear interfaces profesionales.
