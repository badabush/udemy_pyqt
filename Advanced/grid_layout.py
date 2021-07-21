import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layout")
        self.setGeometry(1500, 200, 600, 600)
        self.UI()

        self.show()

    def UI(self):
        self.gridLayout = QGridLayout()
        # btn1 = QPushButton("Button1")
        # btn2 = QPushButton("Button2")
        # btn3 = QPushButton("Button3")
        # btn4 = QPushButton("Button4")
        # self.gridLayout.addWidget(btn1, 0, 0)
        # self.gridLayout.addWidget(btn2, 0, 1)
        # self.gridLayout.addWidget(btn3, 1, 0)
        # self.gridLayout.addWidget(btn4, 1, 1)
        btn_counter = 1
        for row in range(0, 3):
            for col in range(0, 3):
                btn = QPushButton("{n}".format(n=btn_counter))
                self.gridLayout.addWidget(btn, row, col)
                btn.clicked.connect(self.clickMe)  # connect button to function in each iteration
                btn_counter += 1
        self.setLayout(self.gridLayout)

    def clickMe(self):
        button_id = self.sender().text()  # sender to identify which button was clicked
        if button_id == "1":
            print(1)
        elif button_id == "2":
            print(2)
        elif button_id == "3":
            print(3)
        elif button_id == "4":
            print(4)
        elif button_id == "5":
            print(5)
        elif button_id == "6":
            print(6)
        elif button_id == "7":
            print(7)
        elif button_id == "8":
            print(8)
        elif button_id == "9":
            print(9)

    def keyPressEvent(self, event):
        # catches user key presses, close window on "ESCAPE"
        if event.key() == Qt.Key_Escape:
            self.close()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
