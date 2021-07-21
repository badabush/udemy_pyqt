import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Checkboxes")
        self.setGeometry(50, 50, 600, 600)
        self.UI()

    def UI(self):
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Enter your name")
        self.surname = QLineEdit(self)
        self.surname.setPlaceholderText("Enter your surname")
        self.name.move(150, 50)
        self.surname.move(150, 80)

        self.checkbox = QCheckBox("Remember me", self)
        self.checkbox.move(150, 110)

        button = QPushButton("Submit", self)
        button.move(200, 140)
        button.clicked.connect(self.submit)

        self.show()

    def submit(self):
        if self.checkbox.isChecked():
            print('Name: {name} \nSurname: {sname} \nChecked: {checked}'.format(name=self.name.text(),
                                                                                sname=self.surname.text(),
                                                                                checked=self.checkbox.isChecked()))
        else:
            print('Name: {name} \nSurname: {sname} \nChecked: {checked}'.format(name=self.name.text(),
                                                                                sname=self.surname.text(),
                                                                                checked=self.checkbox.isChecked()))


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
