import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Dialogs")
        self.setGeometry(1500, 200, 600, 600)
        self.UI()

        self.show()

    def UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.editor = QTextEdit()
        fileBtn = QPushButton("Open File")
        fileBtn.clicked.connect(self.openFile)
        fontBtn = QPushButton("Change Font")
        fontBtn.clicked.connect(self.changeFont)
        colorBtn = QPushButton("Change Color")
        colorBtn.clicked.connect(self.changeColor)
        vbox.addWidget(self.editor)
        vbox.addLayout(hbox)
        hbox.addStretch()
        hbox.addWidget(fileBtn)
        hbox.addWidget(fontBtn)
        hbox.addWidget(colorBtn)
        hbox.addStretch()

        self.setLayout(vbox)

    def openFile(self):
        url = QFileDialog.getOpenFileName(self, "Open a file", "../", "All Files(*);;*txt")
        fileUrl = url[0]
        file = open(fileUrl, 'r')
        content = file.read()
        self.editor.setText(content)

    def changeFont(self):
        font, _ = QFontDialog.getFont()
        self.editor.setCurrentFont(font)

    def changeColor(self):
        color= QColorDialog.getColor()
        self.editor.setTextColor(color)

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
