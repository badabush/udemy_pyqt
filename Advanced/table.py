import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Widget")
        self.setGeometry(1500, 200, 600, 500)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        self.table = QTableWidget()
        btn = QPushButton("Get")

        self.table.setRowCount(5)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Name"))  # change header
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Surname"))  # change header
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("Country"))  # change header
        # self.table.horizontalHeader().hide() # hide horizontal header
        self.table.setItem(0, 0, QTableWidgetItem("Item 1"))  # set cell (row,column)
        self.table.setItem(0, 1, QTableWidgetItem("Item 2"))  # set cell (row,column)
        self.table.setItem(1, 2, QTableWidgetItem("Item 3"))  # set cell (row,column)
        self.table.setItem(4, 2, QTableWidgetItem("Item 4"))  # set cell (row,column)

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # make table non-editable
        btn.clicked.connect(self.getValue)  # get value from table after button is clicked

        self.table.doubleClicked.connect(self.doubleClicked)  # get value from cell if double clicked
        vbox.addWidget(self.table)
        vbox.addWidget(btn)
        self.setLayout(vbox)
        self.show()

    def getValue(self):
        for item in self.table.selectedItems():
            print(item.text(), item.row(), item.column())

    def doubleClicked(self):
        item = self.table.currentItem()
        if item:
            print(item.text(), item.row(), item.column())



def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
