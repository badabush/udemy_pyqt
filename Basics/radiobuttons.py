import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Radio Buttons")
        self.setGeometry(50, 50, 600, 600)
        self.UI()

    def UI(self):
        self.name = QLineEdit(self)
        self.name.move(150, 50)
        self.name.setPlaceholderText("Enter your name")

        self.surname = QLineEdit(self)
        self.surname.move(150, 80)
        self.surname.setPlaceholderText("Enter your surname")

        self.male = QRadioButton("Male", self)
        self.male.move(150, 110)
        self.male.setChecked(True)
        self.female = QRadioButton("Female", self)
        self.female.move(200, 110)
        button = QPushButton("Submit", self)
        button.move(200, 140)
        button.clicked.connect(self.getValues)

        self.show()

    def getValues(self):
        name = self.name.text()
        surname = self.surname.text()
        if self.male.isChecked():
            gender = "male"
        else:
            gender = "female"

        print("Name: {name}\nSurname: {sname}\nGender: {gender}".format(name=name, sname=surname, gender=gender))


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
