import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Candara", 16)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Spinbox")
        self.setGeometry(50, 50, 600, 600)
        self.UI()

    def UI(self):
        self.spinbox = QSpinBox(self)
        self.spinbox.move(150, 100)
        self.spinbox.setFont(font)
        # self.spinbox.setMinimum(25)
        # self.spinbox.setMaximum(110)
        self.spinbox.setRange(25, 110)  # combined min max range

        # prefix/suffix
        # self.spinbox.setPrefix("$ ")
        self.spinbox.setSuffix(" cm")

        # stepsize
        self.spinbox.setSingleStep(5)
        self.spinbox.valueChanged.connect(self.getValue)

        button = QPushButton("Send", self)
        button.move(150, 130)
        button.clicked.connect(self.getValue)  # connect to same function getValue
        self.show()

    def getValue(self):
        value = self.spinbox.value()
        print(value)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
