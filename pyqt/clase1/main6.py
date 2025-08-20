from PyQt5.QtWidgets import QApplication, QWidget, QBoxLayout, QLabel
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(layout)

        label1 = QLabel("Label 1")
        layout.addWidget(label1, 0)

        label2 = QLabel("Label 2")
        layout.addWidget(label2, 0)

        layout2 = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addLayout(layout2)

        label3 = QLabel("Label 3")
        layout2.addWidget(label3, 0)

        label4 = QLabel("Label 4")
        layout2.addWidget(label4, 0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = Window()
    screen.show()
    sys.exit(app.exec_())