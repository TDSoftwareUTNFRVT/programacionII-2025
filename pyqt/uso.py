#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Archivo: uso.py
Propósito: Usar la interfaz generada desde Qt Designer (prueba.py) 
          y agregar funcionalidad personalizada.
"""

import sys
from PyQt5 import QtWidgets
from prueba import Ui_Dialog


class VentanaPersonalizada(QtWidgets.QDialog):
    """
    Clase que hereda de QDialog e implementa la interfaz generada
    desde Qt Designer, agregando funcionalidad personalizada.
    """
    
    def __init__(self):
        super().__init__()
        
        # Configurar la interfaz generada desde Qt Designer
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # Conectar señales y slots personalizados
        self.conectar_eventos()
        
        # Personalizar la ventana
        self.personalizar_ventana()
    
    def conectar_eventos(self):
        """
        Conectar los eventos de los widgets a las funciones correspondientes.
        """
        # Conectar el botón Cancel del QDialogButtonBox para cerrar la ventana
        self.ui.buttonBox.rejected.connect(self.cerrar_ventana)
        
        # También conectar el botón OK si queremos que cierre la ventana
        self.ui.buttonBox.accepted.connect(self.cerrar_ventana)
        
        # Opcional: conectar algún otro botón para cerrar (por ejemplo pushButton)
        self.ui.pushButton.clicked.connect(self.cerrar_ventana)
    
    def personalizar_ventana(self):
        """
        Personalizar la apariencia y configuración de la ventana.
        """
        # Cambiar el texto del botón para que sea más claro
        self.ui.pushButton.setText("Cerrar Aplicación")
        
        # Cambiar los textos de las etiquetas para que sean más descriptivos
        self.ui.label.setText("Nombre:")
        self.ui.label_2.setText("Descripción:")
        
        # Agregar placeholder text a los campos
        self.ui.lineEdit.setPlaceholderText("Ingrese su nombre aquí...")
        self.ui.textEdit.setPlaceholderText("Ingrese una descripción...")
        
        # Configurar el título de la ventana
        self.setWindowTitle("Sistema de Gestión - Demo")
    
    def cerrar_ventana(self):
        """
        Función personalizada para cerrar la ventana.
        Puede incluir validaciones o confirmaciones antes de cerrar.
        """
        # Opcional: Mostrar mensaje de confirmación
        respuesta = QtWidgets.QMessageBox.question(
            self, 
            'Confirmar cierre',
            '¿Está seguro que desea cerrar la aplicación?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )
        
        if respuesta == QtWidgets.QMessageBox.Yes:
            print("Cerrando la aplicación...")
            self.close()  # Cerrar la ventana
            # Opcional: también podemos cerrar toda la aplicación
            # QtWidgets.QApplication.instance().quit()


def main():
    """
    Función principal para ejecutar la aplicación.
    """
    # Crear la aplicación
    app = QtWidgets.QApplication(sys.argv)
    
    # Crear y mostrar la ventana personalizada
    ventana = VentanaPersonalizada()
    ventana.show()
    
    # Ejecutar el bucle de eventos
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()