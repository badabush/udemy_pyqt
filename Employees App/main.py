import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont

import sqlite3
from PIL import Image  # pillow is used for storing images

# ****************** Database ******************
con = sqlite3.connect("employees.db")
cur = con.cursor()
person_id = None
default_image = "person.png"


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Employees App")
        self.setGeometry(1500, 200, 750, 600)

        self.ui()

        self.show()

    def ui(self):
        self.main_design()
        self.layouts()
        self.get_employees()
        self.display_first_record()

    def main_design(self):
        self.setStyleSheet("font-size: 14pt;font-family: Arial Bold;")
        self.employeeList = QListWidget()
        self.employeeList.itemClicked.connect(self.single_click)
        self.btnNew = QPushButton("New")
        self.btnNew.clicked.connect(self.add_employee)
        self.btnUpdate = QPushButton("Update")
        self.btnUpdate.clicked.connect(self.update_employee)
        self.btnDelete = QPushButton("Delete")
        self.btnDelete.clicked.connect(self.delete_employee)

    def layouts(self):
        # ****************** LAYOUTS ******************
        self.main_layout = QHBoxLayout()
        self.left_layout = QFormLayout()
        self.right_main_layout = QVBoxLayout()
        self.right_top_layout = QHBoxLayout()
        self.right_bottom_layout = QHBoxLayout()

        # ****************** CHILD LAYOUTS -> MAIN LAYOUT ******************
        # add right top/bottom layout to right main layout
        self.right_main_layout.addLayout(self.right_top_layout)
        self.right_main_layout.addLayout(self.right_bottom_layout)
        self.main_layout.addLayout(self.left_layout, 40)  # last number for percentage of space
        self.main_layout.addLayout(self.right_main_layout, 60)  # last number for percentage of space

        # ****************** WIDGETS -> LAYOUTS ******************
        self.right_top_layout.addWidget(self.employeeList)
        self.right_bottom_layout.addWidget(self.btnNew)
        self.right_bottom_layout.addWidget(self.btnUpdate)
        self.right_bottom_layout.addWidget(self.btnDelete)

        # ****************** SET MAIN WINDOW LAYOUT ******************
        self.setLayout(self.main_layout)

    def add_employee(self):
        self.new_employee = AddEmployee()
        self.close()

    def get_employees(self):
        query = "SELECT id, name, surname FROM employees"
        employees = cur.execute(query).fetchall()
        for employee in employees:
            self.employeeList.addItem(str(employee[0]) + "-" + employee[1] + " " + employee[2])

    def display_first_record(self):
        query = "SELECT * FROM employees ORDER BY ROWID ASC LIMIT 1"
        employee = cur.execute(query).fetchone()
        if employee:
            img = QLabel()
            img.setPixmap(QPixmap("images/" + employee[5]))
            name = QLabel(employee[1])
            surname = QLabel(employee[2])
            phone = QLabel(employee[3])
            email = QLabel(employee[4])
            address = QLabel(employee[6])
            self.left_layout.setVerticalSpacing(20)  # vertical spacing between form rows
            self.left_layout.addRow("", img)
            self.left_layout.addRow("Name: ", name)
            self.left_layout.addRow("Surname: ", surname)
            self.left_layout.addRow("Phone: ", phone)
            self.left_layout.addRow("Email: ", email)
            self.left_layout.addRow("Address: ", address)

    def single_click(self):
        for i in reversed(range(self.left_layout.count())):
            widget = self.left_layout.takeAt(i).widget()  # get all widgets in left layout
            if widget is not None:
                widget.deleteLater()  # delete widget in row

        employee = self.employeeList.currentItem().text()
        id = employee.split("-")[0]
        query = "SELECT * FROM employees WHERE id=?"
        employee = cur.execute(query, (id,)).fetchone()  # single item tuple=(1,)

        img = QLabel()
        img.setPixmap(QPixmap("images/" + employee[5]))
        name = QLabel(employee[1])
        surname = QLabel(employee[2])
        phone = QLabel(employee[3])
        email = QLabel(employee[4])
        address = QLabel(employee[6])
        self.left_layout.setVerticalSpacing(20)  # vertical spacing between form rows
        self.left_layout.addRow("", img)
        self.left_layout.addRow("Name: ", name)
        self.left_layout.addRow("Surname: ", surname)
        self.left_layout.addRow("Phone: ", phone)
        self.left_layout.addRow("Email: ", email)
        self.left_layout.addRow("Address: ", address)

    def delete_employee(self):
        if self.employeeList.selectedItems():
            employee = self.employeeList.currentItem().text()
            id = employee.split("-")[0]
            mbox = QMessageBox.question(self, "Warning", "Are you sure?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if mbox == QMessageBox.Yes:
                try:
                    query = "DELETE FROM employees WHERE id=?"
                    cur.execute(query, (id,))
                    con.commit()
                    QMessageBox.information(self, "Information.", "Person has been deleted.")
                    # Restart application to update.
                    self.close()
                    self.main = Main()
                except:
                    QMessageBox.information(self, "Warning!", "Person has not been deleted.")

    def update_employee(self):
        global person_id
        if self.employeeList.selectedItems():
            employee = self.employeeList.currentItem().text()
            person_id = employee.split("-")[0]
            self.update_window = UpdateEmployee()
            self.close()

    def keyPressEvent(self, event):
        # catches user key presses, close window on "ESCAPE"
        if event.key() == Qt.Key_Escape:
            self.close()


class AddEmployee(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Employees")
        self.setGeometry(1500, 200, 350, 600)
        self.default_image = "person.png"
        self.ui()
        self.show()

    def ui(self):
        self.main_design()
        self.layouts()

    def closeEvent(self, event):
        """
        Reopens Main Window when AddEmployee window is closed.
        :param event:
        :return:
        """
        self.main = Main()

    def main_design(self):
        self.setStyleSheet(
            "background-color: white; font-size: 14pt; font-family: Times")  # stylesheet for whole window
        # ****************** TOP ******************
        self.title = QLabel("Add Person")
        self.title.setStyleSheet("font-size: 24pt;font-family: Arial Bold")  # quickly edit size/family/colors/etc.
        self.img_add = QLabel()
        self.img_add.setPixmap(QPixmap("icons/person.png"))

        # ****************** BOT ******************
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter Name")

        self.surname_label = QLabel("Surname:")
        self.surname_input = QLineEdit()
        self.surname_input.setPlaceholderText("Enter Surname")

        self.phone_label = QLabel("Phone:")
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Enter Phone number")

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter Email")

        self.image_label = QLabel("Image:")
        self.image_button = QPushButton("Browse")
        self.image_button.setStyleSheet("background-color: orange; font-size: 10pt")
        self.image_button.clicked.connect(self.upload_image)

        self.address_label = QLabel("Address:")
        self.address_input = QTextEdit()
        self.add_button = QPushButton("Add")
        self.add_button.setStyleSheet("background-color: orange; font-size: 10pt")
        self.add_button.clicked.connect(self.add_employee)

    def layouts(self):
        # ****************** LAYOUTS ******************
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bot_layout = QFormLayout()

        # ****************** MAIN LAYOUT ******************
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.bot_layout)

        # ****************** WIDGETS -> LAYOUT ******************
        # ****************** TOP LAYOUT ******************
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.title)
        self.top_layout.addWidget(self.img_add)
        self.top_layout.addStretch()
        self.top_layout.setContentsMargins(110, 20, 10, 30)  # LTRB

        # ****************** BOTTOM LAYOUT ******************
        self.bot_layout.addRow(self.name_label, self.name_input)
        self.bot_layout.addRow(self.surname_label, self.surname_input)
        self.bot_layout.addRow(self.phone_label, self.phone_input)
        self.bot_layout.addRow(self.email_label, self.email_input)
        self.bot_layout.addRow(self.image_label, self.image_button)
        self.bot_layout.addRow(self.address_label, self.address_input)
        self.bot_layout.addRow("", self.add_button)

        # ****************** SET WINDOW LAYOUT ******************
        self.setLayout(self.main_layout)

    def upload_image(self):
        global default_image
        size = (128, 128)  # define dimensions for image (128,128)
        self.file_name, ok = QFileDialog.getOpenFileName(self, "Upload Image", "", "Image Files (*.jpg *.png)")

        if ok:
            default_image = os.path.basename(self.file_name)
            # PIL package
            img = Image.open(self.file_name)
            img.resize(size)
            img.save("images/{name}".format(name=default_image))

    def add_employee(self):
        global default_image
        name = self.name_input.text()
        surname = self.surname_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        img = default_image
        address = self.address_input.toPlainText()

        if (name and surname and phone != ""):
            try:
                query = "INSERT INTO employees (name, surname, phone, email, image, address) VALUES(?,?,?,?,?,?)"
                cur.execute(query, (name, surname, phone, email, img, address))
                con.commit()
                QMessageBox.information(self, "Success", "Person has been added.")
                self.close()

            except:
                QMessageBox.information(self, "Warning", "Person could not be added.")

        else:
            QMessageBox.information(self, "Warning", "Fields cannot be empty.")

    def keyPressEvent(self, event):
        # catches user key presses, close window on "ESCAPE"
        if event.key() == Qt.Key_Escape:
            self.close()


class UpdateEmployee(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Employee")
        self.setGeometry(1500, 200, 350, 600)
        self.ui()
        self.show()

    def ui(self):
        self.get_person()
        self.main_design()
        self.layouts()

    def closeEvent(self, event):
        """
        Reopens Main Window when AddEmployee window is closed.
        :param event:
        :return:
        """
        self.main = Main()

    def get_person(self):
        global person_id
        query = "SELECT * FROM employees WHERE id=?"
        employee = cur.execute(query, (person_id,)).fetchone()
        self.name = employee[1]
        self.surname = employee[2]
        self.phone = employee[3]
        self.email = employee[4]
        self.img = employee[5]
        self.address = employee[6]

    def main_design(self):
        self.setStyleSheet(
            "background-color: white; font-size: 14pt; font-family: Times")  # stylesheet for whole window
        # ****************** TOP ******************
        self.title = QLabel("Update Person")
        self.title.setStyleSheet("font-size: 24pt;font-family: Arial Bold")  # quickly edit size/family/colors/etc.
        self.img_add = QLabel()
        self.img_add.setPixmap(QPixmap("icons/{img}".format(img=self.img)))

        # ****************** BOT ******************
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter Name")
        self.name_input.setText(self.name)

        self.surname_label = QLabel("Surname:")
        self.surname_input = QLineEdit()
        self.surname_input.setPlaceholderText("Enter Surname")
        self.surname_input.setText(self.surname)

        self.phone_label = QLabel("Phone:")
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Enter Phone number")
        self.phone_input.setText(self.phone)

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter Email")
        self.email_input.setText(self.email)

        self.image_label = QLabel("Image:")
        self.image_button = QPushButton("Browse")
        self.image_button.setStyleSheet("background-color: orange; font-size: 10pt")
        self.image_button.clicked.connect(self.upload_image)

        self.address_label = QLabel("Address:")
        self.address_input = QTextEdit()
        self.address_input.setText(self.address)
        self.update_button = QPushButton("Update")
        self.update_button.setStyleSheet("background-color: orange; font-size: 10pt")
        self.update_button.clicked.connect(self.update_employee)

    def layouts(self):
        # ****************** LAYOUTS ******************
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bot_layout = QFormLayout()

        # ****************** MAIN LAYOUT ******************
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.bot_layout)

        # ****************** WIDGETS -> LAYOUT ******************
        # ****************** TOP LAYOUT ******************
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.title)
        self.top_layout.addWidget(self.img_add)
        self.top_layout.addStretch()
        self.top_layout.setContentsMargins(110, 20, 10, 30)  # LTRB

        # ****************** BOTTOM LAYOUT ******************
        self.bot_layout.addRow(self.name_label, self.name_input)
        self.bot_layout.addRow(self.surname_label, self.surname_input)
        self.bot_layout.addRow(self.phone_label, self.phone_input)
        self.bot_layout.addRow(self.email_label, self.email_input)
        self.bot_layout.addRow(self.image_label, self.image_button)
        self.bot_layout.addRow(self.address_label, self.address_input)
        self.bot_layout.addRow("", self.update_button)

        # ****************** SET WINDOW LAYOUT ******************
        self.setLayout(self.main_layout)

    def upload_image(self):
        global default_image
        size = (128, 128)  # define dimensions for image (128,128)
        self.file_name, ok = QFileDialog.getOpenFileName(self, "Upload Image", "", "Image Files (*.jpg *.png)")

        if ok:
            default_image = os.path.basename(self.file_name)
            # PIL package
            img = Image.open(self.file_name)
            img.resize(size)
            img.save("images/{name}".format(name=default_image))

    def update_employee(self):
        global default_image
        global person_id
        name = self.name_input.text()
        surname = self.surname_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        img = default_image
        address = self.address_input.toPlainText()

        if (name and surname and phone != ""):
            try:
                query = "UPDATE employees set name=?, surname=?, phone=?, email=?, image=?, address=? WHERE id=?"
                cur.execute(query, (name, surname, phone, email, img, address, person_id))
                con.commit()
                QMessageBox.information(self, "Success", "Person has been updated.")
                self.close()

            except:
                QMessageBox.information(self, "Warning", "Person could not be updated.")

        else:
            QMessageBox.information(self, "Warning", "Fields cannot be empty.")


def main():
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
