from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QGridLayout()
        self.setLayout(layout)

        button = QPushButton("Click Me")
        button.clicked.connect(self.on_button_clicked)
        layout.addWidget(button, 0, 0)

    def on_button_clicked(self):
        print("The button was pressed!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = Window()
    screen.show()
    sys.exit(app.exec_())