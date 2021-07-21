import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class Window(QMainWindow):  # NOTE: Has to inherit from QMainWindow
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Widget")
        self.setGeometry(1500, 200, 600, 600)
        self.UI()

        self.show()

    def UI(self):
        # ********************* Main Menu ****************************
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        code = menubar.addMenu("Code")
        help_ = menubar.addMenu("Help")

        # ********************* Sub Menu Items ***********************
        new = QAction("New Project", self)
        new.setShortcut("Ctrl+O")
        file.addAction(new)  # single add
        open_ = QAction("Open", self)
        exit_ = QAction("Exit", self)
        exit_.setIcon(QIcon("icons/exit.png"))
        exit_.triggered.connect(self.exitFunc)
        file.addActions([open_, exit_])  # multi add

        # ********************* ToolBar ***********************
        tb = self.addToolBar("My Toolbar")
        tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # display text under toolbar icon
        newTb = QAction(QIcon("icons/empty.png"), "New", self)  # quick create with icon
        tb.addAction(newTb)
        openTb = QAction(QIcon("icons/folder.png"), "Open", self)
        tb.addAction(openTb)
        saveTb = QAction(QIcon("icons/save.png"), "Save", self)
        tb.addAction(saveTb)
        exitTb = QAction(QIcon("icons/exit.png"), "Exit", self)
        exitTb.triggered.connect(self.exitFunc)
        tb.addAction(exitTb)
        tb.actionTriggered.connect(self.btnFunc)

        self.combo = QComboBox()
        self.combo.addItems(["Item1", "Item2", "Item3", "Item4", "Item5"])
        tb.addWidget(self.combo)

    def exitFunc(self):
        mbox = QMessageBox.information(self, "Warning", "Are you sure?", QMessageBox.Yes | QMessageBox.No,
                                       QMessageBox.No)  # last .No is for default

        if mbox == QMessageBox.Yes:
            sys.exit()

    def btnFunc(self, btn):  # btn parameter to get which button the user has pressed
        if btn.text() == "New":
            print("Pressed New")
        elif btn.text() == "Open":
            print("Pressed Open")
        else:
            print("Pressed Save")

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
