import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slider Widget")
        self.setGeometry(1500, 200, 600, 500)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        self.slider = QSlider(Qt.Horizontal)  # slider is vertical per default, change with args
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setTickPosition(QSlider.TicksAbove)  # add ticks (above)
        self.slider.setTickInterval(10)  # add tick interval
        self.slider.valueChanged.connect(self.getValue)
        self.text1 = QLabel("0")
        self.text1.setAlignment(Qt.AlignCenter)  # align to center
        self.text2 = QLabel("Hello Python")

        vbox.addStretch()
        vbox.addWidget(self.text1)
        vbox.addWidget(self.text2)
        vbox.addWidget(self.slider)
        self.setLayout(vbox)
        self.show()

    def getValue(self):
        val = self.slider.value()
        self.text1.setText(str(val))
        fontSize = self.slider.value()
        font = QFont("Times", fontSize)
        self.text2.setFont(font)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
