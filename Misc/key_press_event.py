import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Key Press Event")
        self.setGeometry(1500, 200, 400, 400)
        self.UI()

    def UI(self):

        self.show()

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
