from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)

        label1 = QLabel("The Story of Dale")
        layout.addWidget(label1, 0, 0)

        label2 = QLabel("Few people could understand Dale's motivation. It wasn't something that was easily explained.")
        label2.setWordWrap(True)
        layout.addWidget(label2, 0, 1)

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())