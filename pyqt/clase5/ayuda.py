# Ayuda PyQt5: Gestión de Datos con Archivos de Texto
# --------------------------------------------------
#
# Esta clase enseña cómo crear aplicaciones que persistan datos usando archivos,
# implementando un CRUD completo (Crear, Leer, Actualizar, Eliminar).
#
# ========================================
# 1. Persistencia de datos en archivos
# ========================================
#
# ¿Por qué usar archivos de texto?
# - Simple de implementar y entender
# - No requiere librerías adicionales
# - Fácil de leer y modificar manualmente
# - Ideal para aprender conceptos de persistencia
#
# Formato recomendado: usar separadores
# - Separador: | (pipe) o ; (punto y coma)
# - Una línea por registro
# - Orden fijo de campos

import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QGridLayout, QLabel, QLineEdit,
                             QPushButton, QTextEdit, QComboBox, QMessageBox,
                             QListWidget, QListWidgetItem, QGroupBox, QSplitter)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# ========================================
# 2. Estructura básica del sistema
# ========================================

class GestorDocentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Docentes - Ejemplo Completo")
        self.setGeometry(100, 100, 1000, 700)
        
        # Archivo de datos
        self.archivo_datos = "docentes.txt"
        
        # Lista para mantener datos en memoria (opcional)
        self.docentes = []
        
        self.configurar_interfaz()
        self.cargar_datos_iniciales()
    
    def configurar_interfaz(self):
        """Configurar la interfaz principal"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Crear splitter para dividir pantalla
        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)
        
        # Panel izquierdo: Formulario
        panel_form = self.crear_formulario()
        splitter.addWidget(panel_form)
        
        # Panel derecho: Lista y detalles
        panel_lista = self.crear_panel_lista()
        splitter.addWidget(panel_lista)
        
        # Configurar proporciones
        splitter.setSizes([400, 600])
    
    def crear_formulario(self):
        """Crear el formulario de entrada de datos"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Grupo del formulario
        grupo_form = QGroupBox("Datos del Docente")
        form_layout = QGridLayout()
        
        # Campos del formulario
        self.legajo_edit = QLineEdit()
        self.legajo_edit.setPlaceholderText("Ej: DOC001")
        form_layout.addWidget(QLabel("Legajo:"), 0, 0)
        form_layout.addWidget(self.legajo_edit, 0, 1)
        
        self.nombre_edit = QLineEdit()
        self.nombre_edit.setPlaceholderText("Nombre del docente")
        form_layout.addWidget(QLabel("Nombre:"), 1, 0)
        form_layout.addWidget(self.nombre_edit, 1, 1)
        
        self.apellido_edit = QLineEdit()
        self.apellido_edit.setPlaceholderText("Apellido del docente")
        form_layout.addWidget(QLabel("Apellido:"), 2, 0)
        form_layout.addWidget(self.apellido_edit, 2, 1)
        
        self.dni_edit = QLineEdit()
        self.dni_edit.setPlaceholderText("12345678")
        form_layout.addWidget(QLabel("DNI:"), 3, 0)
        form_layout.addWidget(self.dni_edit, 3, 1)
        
        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText("docente@universidad.edu")
        form_layout.addWidget(QLabel("Email:"), 4, 0)
        form_layout.addWidget(self.email_edit, 4, 1)
        
        self.telefono_edit = QLineEdit()
        self.telefono_edit.setPlaceholderText("123456789")
        form_layout.addWidget(QLabel("Teléfono:"), 5, 0)
        form_layout.addWidget(self.telefono_edit, 5, 1)
        
        self.materia_edit = QLineEdit()
        self.materia_edit.setPlaceholderText("Materia que dicta")
        form_layout.addWidget(QLabel("Materia:"), 6, 0)
        form_layout.addWidget(self.materia_edit, 6, 1)
        
        self.categoria_combo = QComboBox()
        self.categoria_combo.addItems(["Titular", "Asociado", "Adjunto", "Auxiliar", "Interino"])
        form_layout.addWidget(QLabel("Categoría:"), 7, 0)
        form_layout.addWidget(self.categoria_combo, 7, 1)
        
        grupo_form.setLayout(form_layout)
        layout.addWidget(grupo_form)
        
        # Grupo de botones
        grupo_botones = QGroupBox("Acciones")
        botones_layout = QVBoxLayout()
        
        self.btn_agregar = QPushButton("Agregar Docente")
        self.btn_agregar.clicked.connect(self.agregar_docente)
        botones_layout.addWidget(self.btn_agregar)
        
        self.btn_buscar = QPushButton("Buscar por Legajo")
        self.btn_buscar.clicked.connect(self.buscar_docente)
        botones_layout.addWidget(self.btn_buscar)
        
        self.btn_modificar = QPushButton("Modificar Seleccionado")
        self.btn_modificar.clicked.connect(self.modificar_docente)
        botones_layout.addWidget(self.btn_modificar)
        
        self.btn_eliminar = QPushButton("Eliminar Seleccionado")
        self.btn_eliminar.clicked.connect(self.eliminar_docente)
        botones_layout.addWidget(self.btn_eliminar)
        
        self.btn_limpiar = QPushButton("Limpiar Formulario")
        self.btn_limpiar.clicked.connect(self.limpiar_formulario)
        botones_layout.addWidget(self.btn_limpiar)
        
        grupo_botones.setLayout(botones_layout)
        layout.addWidget(grupo_botones)
        
        widget.setLayout(layout)
        return widget
    
    def crear_panel_lista(self):
        """Crear panel con lista y detalles"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Búsqueda
        busqueda_layout = QHBoxLayout()
        busqueda_layout.addWidget(QLabel("Buscar:"))
        self.busqueda_edit = QLineEdit()
        self.busqueda_edit.setPlaceholderText("Buscar por apellido, nombre o legajo...")
        self.busqueda_edit.textChanged.connect(self.filtrar_lista)
        busqueda_layout.addWidget(self.busqueda_edit)
        layout.addLayout(busqueda_layout)
        
        # Lista de docentes
        self.lista_docentes = QListWidget()
        self.lista_docentes.itemClicked.connect(self.mostrar_detalles)
        layout.addWidget(self.lista_docentes)
        
        # Detalles del docente seleccionado
        grupo_detalles = QGroupBox("Detalles del Docente Seleccionado")
        self.detalles_text = QTextEdit()
        self.detalles_text.setReadOnly(True)
        self.detalles_text.setMaximumHeight(200)
        detalles_layout = QVBoxLayout()
        detalles_layout.addWidget(self.detalles_text)
        grupo_detalles.setLayout(detalles_layout)
        layout.addWidget(grupo_detalles)
        
        widget.setLayout(layout)
        return widget

# ========================================
# 3. Manejo de archivos
# ========================================

    def cargar_datos_iniciales(self):
        """Cargar datos desde el archivo al iniciar"""
        if not os.path.exists(self.archivo_datos):
            # Crear archivo con datos de ejemplo
            self.crear_datos_ejemplo()
            return
        
        try:
            with open(self.archivo_datos, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:  # Ignorar líneas vacías
                        datos = linea.split('|')
                        if len(datos) == 8:  # Verificar formato correcto
                            self.agregar_a_lista(datos)
                        else:
                            print(f"Línea con formato incorrecto: {linea}")
            
            print(f"Se cargaron {self.lista_docentes.count()} docentes")
        
        except Exception as e:
            QMessageBox.critical(self, 'Error al cargar', 
                               f'No se pudieron cargar los datos:\n{str(e)}')
    
    def guardar_todos_los_datos(self):
        """Guardar toda la lista al archivo"""
        try:
            with open(self.archivo_datos, 'w', encoding='utf-8') as archivo:
                for i in range(self.lista_docentes.count()):
                    item = self.lista_docentes.item(i)
                    datos = item.data(Qt.UserRole)
                    linea = '|'.join(datos) + '\n'
                    archivo.write(linea)
            
            print("Datos guardados correctamente")
        
        except Exception as e:
            QMessageBox.critical(self, 'Error al guardar',
                               f'No se pudieron guardar los datos:\n{str(e)}')
    
    def crear_datos_ejemplo(self):
        """Crear archivo con datos de ejemplo"""
        datos_ejemplo = [
            "DOC001|Juan|Pérez|12345678|juan.perez@universidad.edu|123456789|Matemática|Titular",
            "DOC002|María|González|87654321|maria.gonzalez@universidad.edu|987654321|Física|Adjunto",
            "DOC003|Carlos|Rodríguez|11223344|carlos.rodriguez@universidad.edu|456789123|Química|Asociado",
            "DOC004|Ana|López|55667788|ana.lopez@universidad.edu|789123456|Historia|Auxiliar",
            "DOC005|Pedro|Martínez|99887766|pedro.martinez@universidad.edu|321654987|Inglés|Interino"
        ]
        
        try:
            with open(self.archivo_datos, 'w', encoding='utf-8') as archivo:
                for linea in datos_ejemplo:
                    archivo.write(linea + '\n')
            
            # Cargar los datos de ejemplo en la lista
            for linea in datos_ejemplo:
                datos = linea.split('|')
                self.agregar_a_lista(datos)
            
            QMessageBox.information(self, 'Datos de ejemplo', 
                                  'Se crearon datos de ejemplo para empezar')
        
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'No se pudo crear el archivo:\n{str(e)}')

# ========================================
# 4. Operaciones CRUD (Create, Read, Update, Delete)
# ========================================

    def agregar_docente(self):
        """Agregar nuevo docente"""
        # Validar campos obligatorios
        if not self.legajo_edit.text().strip():
            QMessageBox.warning(self, 'Error', 'El legajo es obligatorio')
            self.legajo_edit.setFocus()
            return
        
        if not self.nombre_edit.text().strip():
            QMessageBox.warning(self, 'Error', 'El nombre es obligatorio')
            self.nombre_edit.setFocus()
            return
        
        if not self.apellido_edit.text().strip():
            QMessageBox.warning(self, 'Error', 'El apellido es obligatorio')
            self.apellido_edit.setFocus()
            return
        
        # Verificar que el legajo no exista
        legajo = self.legajo_edit.text().strip().upper()
        if self.buscar_por_legajo(legajo):
            QMessageBox.warning(self, 'Error', 
                              f'Ya existe un docente con el legajo {legajo}')
            return
        
        # Validar email (básico)
        email = self.email_edit.text().strip()
        if email and '@' not in email:
            QMessageBox.warning(self, 'Error', 'El formato del email es incorrecto')
            return
        
        # Recopilar datos
        datos = [
            legajo,
            self.nombre_edit.text().strip(),
            self.apellido_edit.text().strip(),
            self.dni_edit.text().strip(),
            email,
            self.telefono_edit.text().strip(),
            self.materia_edit.text().strip(),
            self.categoria_combo.currentText()
        ]
        
        # Agregar a la lista y guardar
        self.agregar_a_lista(datos)
        self.guardar_todos_los_datos()
        self.limpiar_formulario()
        
        QMessageBox.information(self, 'Éxito', 
                              f'Docente {datos[1]} {datos[2]} agregado correctamente')
    
    def buscar_por_legajo(self, legajo):
        """Buscar si existe un legajo en la lista"""
        for i in range(self.lista_docentes.count()):
            item = self.lista_docentes.item(i)
            datos = item.data(Qt.UserRole)
            if datos[0].upper() == legajo.upper():
                return item
        return None
    
    def buscar_docente(self):
        """Buscar y seleccionar docente por legajo"""
        legajo = self.legajo_edit.text().strip()
        if not legajo:
            QMessageBox.warning(self, 'Error', 'Ingrese un legajo para buscar')
            return
        
        item = self.buscar_por_legajo(legajo)
        if item:
            self.lista_docentes.setCurrentItem(item)
            self.mostrar_detalles(item)
            self.lista_docentes.scrollToItem(item)
        else:
            QMessageBox.information(self, 'No encontrado', 
                                  f'No se encontró docente con legajo: {legajo}')
    
    def modificar_docente(self):
        """Modificar el docente seleccionado"""
        item_actual = self.lista_docentes.currentItem()
        if not item_actual:
            QMessageBox.warning(self, 'Error', 
                              'Seleccione un docente de la lista para modificar')
            return
        
        # Cargar datos en el formulario
        datos = item_actual.data(Qt.UserRole)
        self.legajo_edit.setText(datos[0])
        self.nombre_edit.setText(datos[1])
        self.apellido_edit.setText(datos[2])
        self.dni_edit.setText(datos[3])
        self.email_edit.setText(datos[4])
        self.telefono_edit.setText(datos[5])
        self.materia_edit.setText(datos[6])
        
        # Seleccionar categoría en el combo
        index = self.categoria_combo.findText(datos[7])
        if index >= 0:
            self.categoria_combo.setCurrentIndex(index)
        
        # Cambiar el botón para actualizar
        self.btn_agregar.setText("Actualizar Docente")
        self.btn_agregar.clicked.disconnect()
        self.btn_agregar.clicked.connect(lambda: self.actualizar_docente(item_actual))
        
        QMessageBox.information(self, 'Modo edición', 
                              'Modifique los datos y presione "Actualizar Docente"')
    
    def actualizar_docente(self, item):
        """Actualizar los datos del docente"""
        # Validar igual que en agregar
        if not self.nombre_edit.text().strip() or not self.apellido_edit.text().strip():
            QMessageBox.warning(self, 'Error', 'Nombre y apellido son obligatorios')
            return
        
        # Obtener datos actualizados
        nuevos_datos = [
            self.legajo_edit.text().strip().upper(),
            self.nombre_edit.text().strip(),
            self.apellido_edit.text().strip(),
            self.dni_edit.text().strip(),
            self.email_edit.text().strip(),
            self.telefono_edit.text().strip(),
            self.materia_edit.text().strip(),
            self.categoria_combo.currentText()
        ]
        
        # Actualizar el item
        item.setData(Qt.UserRole, nuevos_datos)
        item.setText(f"{nuevos_datos[2]}, {nuevos_datos[1]} ({nuevos_datos[0]})")
        
        # Guardar cambios
        self.guardar_todos_los_datos()
        
        # Restaurar botón agregar
        self.btn_agregar.setText("Agregar Docente")
        self.btn_agregar.clicked.disconnect()
        self.btn_agregar.clicked.connect(self.agregar_docente)
        
        self.limpiar_formulario()
        QMessageBox.information(self, 'Éxito', 'Docente actualizado correctamente')
    
    def eliminar_docente(self):
        """Eliminar el docente seleccionado"""
        item_actual = self.lista_docentes.currentItem()
        if not item_actual:
            QMessageBox.warning(self, 'Error', 
                              'Seleccione un docente de la lista para eliminar')
            return
        
        # Confirmar eliminación
        datos = item_actual.data(Qt.UserRole)
        respuesta = QMessageBox.question(
            self, 'Confirmar eliminación',
            f'¿Está seguro de eliminar a {datos[1]} {datos[2]} (Legajo: {datos[0]})?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if respuesta == QMessageBox.Yes:
            # Eliminar de la lista
            row = self.lista_docentes.row(item_actual)
            self.lista_docentes.takeItem(row)
            
            # Guardar cambios
            self.guardar_todos_los_datos()
            
            # Limpiar detalles y formulario
            self.detalles_text.clear()
            self.limpiar_formulario()
            
            QMessageBox.information(self, 'Éxito', 'Docente eliminado correctamente')

# ========================================
# 5. Funciones auxiliares de interfaz
# ========================================

    def agregar_a_lista(self, datos):
        """Agregar un docente a la lista visual"""
        # Crear texto para mostrar: "Apellido, Nombre (Legajo)"
        texto_item = f"{datos[2]}, {datos[1]} ({datos[0]})"
        
        # Crear item y guardar datos completos
        item = QListWidgetItem(texto_item)
        item.setData(Qt.UserRole, datos)  # Guardar datos completos en el item
        
        # Agregar a la lista
        self.lista_docentes.addItem(item)
    
    def filtrar_lista(self):
        """Filtrar la lista según el texto de búsqueda"""
        texto_busqueda = self.busqueda_edit.text().lower()
        
        for i in range(self.lista_docentes.count()):
            item = self.lista_docentes.item(i)
            datos = item.data(Qt.UserRole)
            
            # Buscar en legajo, nombre y apellido
            coincide = (texto_busqueda in datos[0].lower() or  # legajo
                       texto_busqueda in datos[1].lower() or   # nombre
                       texto_busqueda in datos[2].lower())     # apellido
            
            # Mostrar u ocultar según coincidencia
            item.setHidden(not coincide)
    
    def mostrar_detalles(self, item):
        """Mostrar detalles del docente seleccionado"""
        datos = item.data(Qt.UserRole)
        
        detalles = f"""INFORMACIÓN DEL DOCENTE
{'='*40}

Legajo:     {datos[0]}
Nombre:     {datos[1]}
Apellido:   {datos[2]}
DNI:        {datos[3]}
Email:      {datos[4]}
Teléfono:   {datos[5]}
Materia:    {datos[6]}
Categoría:  {datos[7]}

{'='*40}
Seleccione "Modificar" o "Eliminar" para editar este registro."""
        
        self.detalles_text.setPlainText(detalles)
    
    def limpiar_formulario(self):
        """Limpiar todos los campos del formulario"""
        self.legajo_edit.clear()
        self.nombre_edit.clear()
        self.apellido_edit.clear()
        self.dni_edit.clear()
        self.email_edit.clear()
        self.telefono_edit.clear()
        self.materia_edit.clear()
        self.categoria_combo.setCurrentIndex(0)
        
        # Asegurar que el botón esté en modo "Agregar"
        self.btn_agregar.setText("Agregar Docente")
        self.btn_agregar.clicked.disconnect()
        self.btn_agregar.clicked.connect(self.agregar_docente)

# ========================================
# 6. Ejecutar la aplicación
# ========================================

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Configurar estilo
    app.setStyle('Fusion')
    
    # Crear y mostrar ventana
    gestor = GestorDocentes()
    gestor.show()
    
    sys.exit(app.exec_())

# ========================================
# Conceptos clave aprendidos:
# ========================================
#
# 1. Persistencia con archivos de texto
# 2. Formato estructurado con separadores
# 3. CRUD completo (Create, Read, Update, Delete)
# 4. Validación de datos de entrada
# 5. Manejo de errores en operaciones de archivo
# 6. Interfaz dividida con QSplitter
# 7. Lista con datos asociados (UserRole)
# 8. Búsqueda y filtrado en tiempo real
# 9. Confirmación para operaciones destructivas
# 10. Estados de interfaz (modo agregar vs modificar)
#
# Este patrón es la base para cualquier sistema de gestión de datos
# y puede adaptarse fácilmente a otros tipos de información.
