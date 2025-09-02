# Ayuda PyQt5: Menús, Diálogos y Gestión de Archivos
# ---------------------------------------------------
#
# Esta clase introduce elementos profesionales para crear aplicaciones completas:
# menús, diálogos modales, gestión de archivos y barras de estado.
#
# ========================================
# 1. QMainWindow vs QWidget
# ========================================
#
# QMainWindow es la clase base para aplicaciones con:
# - Barra de menús
# - Barras de herramientas
# - Barra de estado
# - Widget central
# - Docks (paneles laterales)
#
# Diferencias clave:
# - QWidget: Ventana simple, ideal para formularios
# - QMainWindow: Aplicación completa con estructura profesional

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QMenuBar,
                             QAction, QFileDialog, QMessageBox, QStatusBar)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence

# ========================================
# 2. Estructura básica de QMainWindow
# ========================================

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación con Menús")
        self.setGeometry(100, 100, 800, 600)
        
        # Widget central (obligatorio en QMainWindow)
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        self.editor.setPlaceholderText("Área de trabajo principal...")
        
        # Configurar componentes
        self.crear_menus()
        self.crear_barra_estado()
        
        # Variables para gestión de archivos
        self.archivo_actual = None

# ========================================
# 3. Creación de menús y acciones
# ========================================

    def crear_menus(self):
        # Obtener la barra de menús (se crea automáticamente)
        menubar = self.menuBar()
        
        # ---- Menú Archivo ----
        menu_archivo = menubar.addMenu('&Archivo')  # & crea shortcut Alt+A
        
        # Acción Nuevo
        accion_nuevo = QAction('&Nuevo', self)
        accion_nuevo.setShortcut(QKeySequence.New)  # Ctrl+N estándar
        accion_nuevo.setStatusTip('Crear un nuevo documento')
        accion_nuevo.triggered.connect(self.nuevo_archivo)
        menu_archivo.addAction(accion_nuevo)
        
        # Acción Abrir
        accion_abrir = QAction('&Abrir...', self)
        accion_abrir.setShortcut(QKeySequence.Open)  # Ctrl+O
        accion_abrir.setStatusTip('Abrir un archivo existente')
        accion_abrir.triggered.connect(self.abrir_archivo)
        menu_archivo.addAction(accion_abrir)
        
        # Separador visual
        menu_archivo.addSeparator()
        
        # Acción Guardar
        accion_guardar = QAction('&Guardar', self)
        accion_guardar.setShortcut(QKeySequence.Save)  # Ctrl+S
        accion_guardar.setStatusTip('Guardar el documento actual')
        accion_guardar.triggered.connect(self.guardar_archivo)
        menu_archivo.addAction(accion_guardar)
        
        # Acción Guardar Como
        accion_guardar_como = QAction('Guardar &como...', self)
        accion_guardar_como.setShortcut(QKeySequence.SaveAs)  # Ctrl+Shift+S
        accion_guardar_como.triggered.connect(self.guardar_como)
        menu_archivo.addAction(accion_guardar_como)
        
        menu_archivo.addSeparator()
        
        # Acción Salir
        accion_salir = QAction('&Salir', self)
        accion_salir.setShortcut(QKeySequence.Quit)  # Ctrl+Q
        accion_salir.setStatusTip('Salir de la aplicación')
        accion_salir.triggered.connect(self.salir)
        menu_archivo.addAction(accion_salir)
        
        # ---- Menú Editar ----
        menu_editar = menubar.addMenu('&Editar')
        
        # Estas acciones están conectadas a funciones integradas del QTextEdit
        accion_cortar = QAction('Cor&tar', self)
        accion_cortar.setShortcut(QKeySequence.Cut)
        accion_cortar.triggered.connect(self.editor.cut)
        menu_editar.addAction(accion_cortar)
        
        accion_copiar = QAction('&Copiar', self)
        accion_copiar.setShortcut(QKeySequence.Copy)
        accion_copiar.triggered.connect(self.editor.copy)
        menu_editar.addAction(accion_copiar)
        
        accion_pegar = QAction('&Pegar', self)
        accion_pegar.setShortcut(QKeySequence.Paste)
        accion_pegar.triggered.connect(self.editor.paste)
        menu_editar.addAction(accion_pegar)
        
        # ---- Menú Ayuda ----
        menu_ayuda = menubar.addMenu('A&yuda')
        
        accion_acerca_de = QAction('&Acerca de...', self)
        accion_acerca_de.triggered.connect(self.acerca_de)
        menu_ayuda.addAction(accion_acerca_de)

# ========================================
# 4. Gestión de archivos con QFileDialog
# ========================================

    def nuevo_archivo(self):
        """Crear un nuevo documento"""
        # Opcional: preguntar si guardar cambios antes de limpiar
        if self.editor.document().isModified():
            respuesta = QMessageBox.question(self, 'Nuevo archivo',
                                           '¿Desea guardar los cambios?',
                                           QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if respuesta == QMessageBox.Yes:
                self.guardar_archivo()
            elif respuesta == QMessageBox.Cancel:
                return
        
        self.editor.clear()
        self.archivo_actual = None
        self.setWindowTitle("Editor - Nuevo documento")
        self.statusBar().showMessage("Nuevo documento creado", 2000)
    
    def abrir_archivo(self):
        """Abrir un archivo existente"""
        # QFileDialog.getOpenFileName devuelve (ruta_archivo, filtro_usado)
        archivo, _ = QFileDialog.getOpenFileName(
            self,                           # Ventana padre
            'Abrir archivo',               # Título del diálogo
            '',                           # Directorio inicial (vacío = último usado)
            'Archivos de texto (*.txt);;Todos los archivos (*.*)'  # Filtros
        )
        
        if archivo:  # Si el usuario seleccionó un archivo
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    self.editor.setPlainText(contenido)
                
                self.archivo_actual = archivo
                self.setWindowTitle(f"Editor - {archivo}")
                self.statusBar().showMessage(f"Archivo abierto: {archivo}", 3000)
                
            except Exception as e:
                QMessageBox.critical(self, 'Error',
                                   f'No se pudo abrir el archivo:\n{str(e)}')
    
    def guardar_archivo(self):
        """Guardar el archivo actual"""
        if self.archivo_actual:
            # Ya tiene archivo asociado, guardar directamente
            self._escribir_archivo(self.archivo_actual)
        else:
            # Primer guardado, pedir nombre de archivo
            self.guardar_como()
    
    def guardar_como(self):
        """Guardar con nuevo nombre"""
        archivo, _ = QFileDialog.getSaveFileName(
            self,
            'Guardar archivo como',
            '',
            'Archivos de texto (*.txt);;Todos los archivos (*.*)'
        )
        
        if archivo:
            self._escribir_archivo(archivo)
    
    def _escribir_archivo(self, archivo):
        """Función auxiliar para escribir archivo"""
        try:
            with open(archivo, 'w', encoding='utf-8') as f:
                f.write(self.editor.toPlainText())
            
            self.archivo_actual = archivo
            self.setWindowTitle(f"Editor - {archivo}")
            self.statusBar().showMessage(f"Archivo guardado: {archivo}", 3000)
            self.editor.document().setModified(False)
            
        except Exception as e:
            QMessageBox.critical(self, 'Error al guardar',
                               f'No se pudo guardar el archivo:\n{str(e)}')

# ========================================
# 5. Diálogos informativos con QMessageBox
# ========================================

    def acerca_de(self):
        """Mostrar información sobre la aplicación"""
        QMessageBox.about(self, 'Acerca de Editor',
                         '''<h3>Editor de Texto</h3>
                         <p>Versión 1.0</p>
                         <p>Un editor simple creado con PyQt5</p>
                         <p>© 2025 - Ejemplo educativo</p>''')
    
    def salir(self):
        """Salir de la aplicación con confirmación"""
        if self.editor.document().isModified():
            respuesta = QMessageBox.question(self, 'Salir',
                                           'Hay cambios sin guardar. ¿Desea salir?',
                                           QMessageBox.Yes | QMessageBox.No)
            if respuesta == QMessageBox.No:
                return
        
        self.close()

# ========================================
# 6. Barra de estado
# ========================================

    def crear_barra_estado(self):
        """Configurar la barra de estado"""
        # QMainWindow crea automáticamente una barra de estado
        self.statusBar().showMessage('Listo')
        
        # Opcional: Conectar eventos del editor para mostrar información
        self.editor.cursorPositionChanged.connect(self.actualizar_cursor)
    
    def actualizar_cursor(self):
        """Mostrar posición del cursor en la barra de estado"""
        cursor = self.editor.textCursor()
        linea = cursor.blockNumber() + 1
        columna = cursor.columnNumber() + 1
        self.statusBar().showMessage(f'Línea: {linea}, Columna: {columna}')

# ========================================
# 7. Ejecutar la aplicación
# ========================================

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())

# ========================================
# Resumen de conceptos clave:
# ========================================
#
# 1. QMainWindow: Ventana principal con menús, barras de herramientas y estado
# 2. QAction: Representa acciones reutilizables en menús y barras
# 3. QFileDialog: Diálogos estándar para abrir/guardar archivos
# 4. QMessageBox: Diálogos informativos, de advertencia y confirmación
# 5. QStatusBar: Barra de estado para mostrar información
# 6. Shortcuts: Atajos de teclado estándar usando QKeySequence
# 7. Gestión de archivos: Lectura/escritura con manejo de errores
#
# Este patrón forma la base de la mayoría de aplicaciones de escritorio modernas.
