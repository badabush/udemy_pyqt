import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Candara", 12)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Messagebox")
        self.setGeometry(50, 50, 600, 600)
        self.UI()

    def UI(self):
        button = QPushButton("Dialog", self)
        button.setFont(font)
        button.move(200, 150)
        button.clicked.connect(self.messageBox)

        self.show()

    def messageBox(self):
        # # Yes | NO | Cancel, "highlighted button" (Yes was default)
        # mbox = QMessageBox.question(self, "Warning", "Do you really want to exit?",
        #                             QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        #
        # if mbox == QMessageBox.Yes:
        #     sys.exit()
        # elif mbox == QMessageBox.No:
        #     print("You Clicked No")
        mbox = QMessageBox.information(self, "Information", "You Logged Out!")
        sys.exit()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
