import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

"""
A QWidget is the base class for all drawable classes in Qt. Any QWidget-based class can be shown as a window by showing 
it when it has no parent.

A QDialog is based on QWidget, but designed to be shown as a window. It will always appear in a window, and has 
functions to make it work well with common buttons on dialogs (accept, reject, etc.).

QMainWindow is designed around common needs for a main window to have. It has predefined places for a menu bar, 
a status bar, a toolbar, and other widgets. It does not have any built-in allowances for buttons like QDialog does.
"""


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Management App")
        self.setWindowIcon(QIcon("icons/icon.ico"))
        self.setGeometry(1200, 200, 1350, 750)
        self.setFixedSize(self.size())  # disable maximize window

        self.ui()
        self.show()

    def ui(self):
        self.toolbar()
        self.tab_widget()
        self.widgets()
        self.layouts()

    def toolbar(self):
        self.tb = self.addToolBar("Toolbar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # enable text under icon in toolbar
        # ***************************************
        # ************* Toolbar Buttons

        # ************* Add Product
        self.add_product = QAction(QIcon("icons/add.png"), "Add Product", self)
        self.tb.addAction(self.add_product)
        self.tb.addSeparator()

        # ************* Add Member
        self.add_member = QAction(QIcon("icons/users.png"), "Add Member", self)
        self.tb.addAction(self.add_member)
        self.tb.addSeparator()
        # ************* Add Sell Product
        self.sell_product = QAction(QIcon("icons/sell.png"), "Sell Product", self)
        self.tb.addAction(self.sell_product)
        self.tb.addSeparator()

    def tab_widget(self):
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)  # add tabs to main window
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab1, "Products")
        self.tabs.addTab(self.tab2, "Members")
        self.tabs.addTab(self.tab3, "Stats")

    def widgets(self):
        # ***********************************
        # ************* Tab 1 Widgets
        # ***********************************

        # ************* Main Left Layout Widget
        self.products_table = QTableWidget()
        self.products_table.setColumnCount(6)
        self.products_table.setColumnHidden(0, True)  # hide a column
        self.products_table.setHorizontalHeaderItem(0, QTableWidgetItem("Product Id"))
        self.products_table.setHorizontalHeaderItem(1, QTableWidgetItem("Product Name"))
        self.products_table.setHorizontalHeaderItem(2, QTableWidgetItem("Manufacturer"))
        self.products_table.setHorizontalHeaderItem(3, QTableWidgetItem("Price"))
        self.products_table.setHorizontalHeaderItem(4, QTableWidgetItem("Quota"))
        self.products_table.setHorizontalHeaderItem(5, QTableWidgetItem("Availability"))

        # ************* Right Top Layout Widgets
        self.search_text = QLabel("Search")
        self.search_entry = QLineEdit()
        self.search_entry.setPlaceholderText("Search for Products")
        self.search_btn = QPushButton("Search")

        # ************* Right Middle Layout Widgets
        self.all_products = QRadioButton("All Products")
        self.available_products = QRadioButton("Available Products")
        self.not_available_products = QRadioButton("Not Available Products")
        self.list_btn = QPushButton("List")

        # ***********************************
        # ************* Tab 2 Widgets
        # ***********************************
        self.members_table_widget = QTableWidget()
        self.members_table_widget.setColumnCount(4)
        self.members_table_widget.setHorizontalHeaderItem(0, QTableWidgetItem("Member Id"))
        self.members_table_widget.setHorizontalHeaderItem(1, QTableWidgetItem("Member Name"))
        self.members_table_widget.setHorizontalHeaderItem(2, QTableWidgetItem("Member Surname"))
        self.members_table_widget.setHorizontalHeaderItem(3, QTableWidgetItem("Phone"))
        self.member_search_text = QLabel("Search Members")
        self.member_search_entry = QLineEdit()
        self.member_search_btn = QPushButton("Search")

    def layouts(self):
        # ***********************************
        # ************* Tab 1 Layout
        # ***********************************
        self.main_layout = QHBoxLayout()
        self.main_left_layout = QVBoxLayout()
        self.main_right_layout = QVBoxLayout()
        self.right_top_layout = QHBoxLayout()
        self.right_middle_layout = QHBoxLayout()
        self.top_groupbox = QGroupBox("Search Box")
        self.middle_groupbox = QGroupBox("List Box")

        # ************* Add Widgets
        # ************* Main Left Layout Widget
        self.main_left_layout.addWidget(self.products_table)
        # ************* Right Top Layout Widget
        self.right_top_layout.addWidget(self.search_text)
        self.right_top_layout.addWidget(self.search_entry)
        self.right_top_layout.addWidget(self.search_btn)
        self.top_groupbox.setLayout(self.right_top_layout)

        # ************* Right Middle Layout Widgets
        self.right_middle_layout.addWidget(self.all_products)
        self.right_middle_layout.addWidget(self.available_products)
        self.right_middle_layout.addWidget(self.not_available_products)
        self.right_middle_layout.addWidget(self.list_btn)

        self.middle_groupbox.setLayout(self.right_middle_layout)

        self.main_right_layout.addWidget(self.top_groupbox)
        self.main_right_layout.addWidget(self.middle_groupbox)

        self.main_layout.addLayout(self.main_left_layout, 70)
        self.main_layout.addLayout(self.main_right_layout, 30)
        self.tab1.setLayout(self.main_layout)

        # ***********************************
        # ************* Tab 2 Layout
        # ***********************************
        self.member_main_layout = QHBoxLayout()
        self.member_left_layout = QHBoxLayout()
        self.member_right_layout = QHBoxLayout()
        self.member_right_groupbox = QGroupBox("Search for Members")
        self.member_right_groupbox.setContentsMargins(10, 10, 10, 600)
        self.member_right_layout.addWidget(self.member_search_text)
        self.member_right_layout.addWidget(self.member_search_entry)
        self.member_right_layout.addWidget(self.member_search_btn)
        self.member_right_groupbox.setLayout(self.member_right_layout)

        self.member_left_layout.addWidget(self.members_table_widget)
        self.member_main_layout.addLayout(self.member_left_layout, 70)
        self.member_main_layout.addWidget(self.member_right_groupbox, 30)
        self.tab2.setLayout(self.member_main_layout)

    def keyPressEvent(self, event):
        # catches user key presses, close window on "ESCAPE"
        if event.key() == Qt.Key_Escape:
            self.close()


def main():
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
