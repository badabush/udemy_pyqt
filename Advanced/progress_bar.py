import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Progress Bar Widget")
        self.setGeometry(1500, 200, 600, 600)

        self.count = 0

        self.UI()

        self.show()

    def UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.progressBar = QProgressBar()
        btnStart = QPushButton("Start")
        btnStart.clicked.connect(self.timerStart)
        btnStop = QPushButton("Stop")
        btnStop.clicked.connect(self.timerStop)
        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.runProgressBar)
        vbox.addWidget(self.progressBar)
        vbox.addLayout(hbox)
        hbox.addWidget(btnStart)
        hbox.addWidget(btnStop)

        self.setLayout(vbox)

    def runProgressBar(self):
        self.count += 1
        print(self.count)
        self.progressBar.setValue(self.count)
        if self.count > 100:
            self.timerStop()

    def timerStart(self):
        self.timer.start()

    def timerStop(self):
        self.timer.stop()

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
