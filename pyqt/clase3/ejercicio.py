# Práctico PyQt5: Uso de múltiples ventanas (Herramientas y Contexto)
# -------------------------------------------------------------------
#
# Objetivo: Aprender a crear y manejar dos ventanas simultáneas en PyQt5.
# Una ventana será de herramientas (con botones como Guardar, Abrir, Buscar, etc.)
# y la otra mostrará el contexto: un formulario de afiliados al Club Atlético Chacarita Juniors.
#
# Cada ejercicio suma widgets y lógica, guiando al alumno en el uso de PyQt5, QGridLayout y manejo de ventanas.
#
# -----------------------------------------------------------------------------
# Ejercicio 1: Crear la ventana de contexto (formulario de afiliados)
# -----------------------------------------------------------------------------
# Teoría:
# - QWidget es la base para crear ventanas.
# - QGridLayout organiza los widgets en filas y columnas.
# - QLabel y QLineEdit permiten mostrar e ingresar datos.
#
# Consigna:
# - Crear una ventana principal (QWidget) de 500x350, título "Afiliados - Chacarita Juniors".
# - Agregar QLabel grande y centrado: "Formulario de Afiliación".
# - Agregar QLabel y QLineEdit para Nombre, Apellido, DNI y Fecha de nacimiento.
#
# -----------------------------------------------------------------------------
# Ejercicio 2: Crear la ventana de herramientas
# -----------------------------------------------------------------------------
# Teoría:
# - Otra instancia de QWidget puede funcionar como ventana secundaria.
# - QPushButton permite crear botones de acción.
# - QVBoxLayout organiza widgets en columna.
#
# Consigna:
# - Crear una ventana secundaria de 200x300, título "Herramientas".
# - Agregar botones: "Guardar", "Abrir", "Buscar", "Salir".
#
# -----------------------------------------------------------------------------
# Ejercicio 3: Mostrar ambas ventanas a la vez
# -----------------------------------------------------------------------------
# Teoría:
# - Puedes crear y mostrar varias ventanas instanciando varias clases QWidget.
# - show() en cada ventana las hace visibles simultáneamente.
#
# Consigna:
# - Modifica el script para que ambas ventanas se muestren al ejecutar el programa.
#
# -----------------------------------------------------------------------------
# Ejercicio 4: Conectar botones de herramientas con el formulario
# -----------------------------------------------------------------------------
# Teoría:
# - Los botones pueden ejecutar funciones que interactúan con la otra ventana.
# - Puedes pasar referencias entre ventanas para manipular datos.
#
# Consigna:
# - Haz que el botón "Guardar" muestre un mensaje con los datos ingresados en el formulario.
# - El botón "Salir" debe cerrar ambas ventanas.
#
# -----------------------------------------------------------------------------
# Ejercicio 5: Personalización visual y validaciones
# -----------------------------------------------------------------------------
# Consigna:
# - Cambia colores, fuentes y tamaño de los widgets para una interfaz moderna.
# - Valida que los campos obligatorios estén completos antes de guardar.
#
# -----------------------------------------------------------------------------
# Sugerencia:
# - Usa QDateEdit para la fecha de nacimiento.
# - Usa QMessageBox para mostrar mensajes.
#
# -----------------------------------------------------------------------------
# Esqueleto inicial:

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton, QVBoxLayout

class VentanaFormulario(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Afiliados - Chacarita Juniors")
        self.setGeometry(100, 100, 500, 350)
        layout = QGridLayout()
        self.setLayout(layout)
        # COMPLETAR: agregar widgets para el formulario

class VentanaHerramientas(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Herramientas")
        self.setGeometry(650, 100, 200, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)
        # COMPLETAR: agregar botones de herramientas

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana_form = VentanaFormulario()
    ventana_herr = VentanaHerramientas()
    # COMPLETAR: mostrar ambas ventanas
    sys.exit(app.exec_())
