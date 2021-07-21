import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Layout")
        self.setGeometry(1500, 200, 400, 400)
        self.UI()

    def UI(self):
        formLayout = QFormLayout()
        formLayout.setRowWrapPolicy(QFormLayout.WrapAllRows)  # make linebreak for each element in row (Wrap)
        name_txt = QLabel("Name: ")
        name_input = QLineEdit()
        name_input.setPlaceholderText("Input Name.")
        pass_txt = QLabel("Password: ")
        pass_input = QLineEdit()
        pass_input.setPlaceholderText("Input Password.")
        pass_input.setEchoMode(QLineEdit.Password)  # hide password value

        # add multiple lineedit fields to form

        date_txt = QLabel("Date of Birth:")
        hbox_date = QHBoxLayout()
        hbox_date.addWidget(QLineEdit())
        hbox_date.addWidget(QLineEdit())
        hbox_date.addWidget(QLineEdit())


        # create layout for buttons, add them to formlayout row
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 20, 0, 0)
        hbox.addStretch()
        hbox.addWidget(QPushButton("Enter"))
        hbox.addWidget(QPushButton("Exit"))

        formLayout.addRow(name_txt, name_input)
        formLayout.addRow(pass_txt, pass_input)
        formLayout.addRow(date_txt, hbox_date)
        formLayout.addRow(QLabel("Country: "), QComboBox())  # fast version without defining it before
        # formLayout.addRow(QPushButton("Enter"), QPushButton("Exit")) # would add 2 buttons in row layout

        formLayout.addRow(hbox)

        self.setLayout(formLayout)
        self.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
