import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horizontal & Vertical Box Layout")
        self.setGeometry(1500, 200, 400, 400)
        self.UI()

    def UI(self):
        mainLayout = QVBoxLayout()
        topLayout = QHBoxLayout()
        bottomLayout = QHBoxLayout()
        mainLayout.addLayout(topLayout)  # add layouts to layouts
        mainLayout.addLayout(bottomLayout)  # add layouts to layouts

        cbox = QCheckBox()
        rbtn = QRadioButton()
        combobox = QComboBox()
        btn1 = QPushButton()
        btn2 = QPushButton()

        topLayout.setContentsMargins(150, 10, 20, 20)  # add margins (left, top, right, bottom)

        topLayout.addWidget(cbox)
        topLayout.addWidget(rbtn)
        topLayout.addWidget(combobox)

        bottomLayout.setContentsMargins(150, 10, 150, 10)  # add margins (left, top, right, bottom)
        bottomLayout.addWidget(btn1)
        bottomLayout.addWidget(btn2)

        self.setLayout(mainLayout)

        self.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
