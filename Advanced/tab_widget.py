import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tab Widget")
        self.setGeometry(1500, 200, 600, 600)
        self.UI()

    def UI(self):
        mainLayout = QVBoxLayout()
        self.tabs = QTabWidget()

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")
        self.tabs.addTab(self.tab3, "Tab 3")

        # self.tabs.setTabEnabled(1,False)  # enable/disable tab (grey out)
        # self.tabs.setTabPosition(2)   # tab layout (hor upper, vert side etc.)

        # ************************ Widgets ************************
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.text = QLabel("Hello Python")
        self.btn1 = QPushButton("First Tab")
        self.btn1.clicked.connect(self.btnFunc)
        self.btn2 = QPushButton("Second Tab")

        vbox.addWidget(self.text)
        vbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        self.tab1.setLayout(vbox)
        self.tab2.setLayout(hbox)


        mainLayout.addWidget(self.tabs)
        self.setLayout(mainLayout)
        self.show()

    def btnFunc(self):
        self.text.setText("Bye Python")

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
