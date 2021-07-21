import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from random import randint

textFont = QFont("Candara", 16)
buttonFont = QFont("Candara", 12)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock-Paper-Scissors Game")
        self.setGeometry(1500, 500, 550, 500)

        self.UI()

    def UI(self):

        # -------------------- Scores -------------------- #
        self.scoreComputerText = QLabel("Computer Score: 0  ", self)
        self.scoreComputerText.move(50, 20)
        self.scoreComputerText.setFont(textFont)
        self.scorePlayerText = QLabel("Player Score: 0  ", self)
        self.scorePlayerText.move(330, 20)
        self.scorePlayerText.setFont(textFont)
        self.scoreComputer = 0
        self.scorePlayer = 0

        # -------------------- Images -------------------- #
        self.imageComputer = QLabel(self)
        self.imageComputer.setPixmap(QPixmap("images/rock.png"))
        self.imageComputer.move(70, 100)
        self.imagePlayer = QLabel(self)
        self.imagePlayer.setPixmap(QPixmap("images/paper.png"))
        self.imagePlayer.move(330, 100)

        self.imageVs = QLabel(self)
        self.imageVs.setPixmap(QPixmap("images/game.png"))
        self.imageVs.move(250, 160)

        # -------------------- Buttons -------------------- #
        btnStart = QPushButton("Start", self)
        btnStart.move(180, 300)
        btnStart.setFont(buttonFont)
        btnStart.clicked.connect(self.startGame)
        btnStop = QPushButton("Stop", self)
        btnStop.move(280, 300)
        btnStop.setFont(buttonFont)
        btnStop.clicked.connect(self.stopGame)

        # -------------------- Timer -------------------- #
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.playGame)

        self.show()

    def startGame(self):
        self.timer.start()

    def stopGame(self):
        if not self.timer.isActive():
            return
        self.timer.stop()
        if self.rndComputer == 1 and self.rndPlayer == 1:
            msgbox = QMessageBox.information(self, "Information", "Draw Game")

        if self.rndComputer == 1 and self.rndPlayer == 2:
            msgbox = QMessageBox.information(self, "Information", "Player Wins")
            self.scorePlayer += 1
            self.scorePlayerText.setText("Player Score: {score}".format(score=self.scorePlayer))

        if self.rndComputer == 1 and self.rndPlayer == 3:
            msgbox = QMessageBox.information(self, "Information", "Computer Wins")
            self.scoreComputer += 1
            self.scoreComputerText.setText("Computer Score: {score}".format(score=self.scoreComputer))

        if self.rndComputer == 2 and self.rndPlayer == 1:
            msgbox = QMessageBox.information(self, "Information", "Computer Wins")
            self.scoreComputer += 1
            self.scoreComputerText.setText("Computer Score: {score}".format(score=self.scoreComputer))

        if self.rndComputer == 2 and self.rndPlayer == 2:
            msgbox = QMessageBox.information(self, "Information", "Draw Game")
            self.scorePlayerText.setText("Player Score: {score}".format(score=self.scorePlayer))

        if self.rndComputer == 2 and self.rndPlayer == 3:
            msgbox = QMessageBox.information(self, "Information", "Player Wins")
            self.scorePlayer += 1
            self.scorePlayerText.setText("Player Score: {score}".format(score=self.scorePlayer))

        if self.rndComputer == 3 and self.rndPlayer == 1:
            msgbox = QMessageBox.information(self, "Information", "Player Wins")
            self.scorePlayer += 1
            self.scorePlayerText.setText("Player Score: {score}".format(score=self.scorePlayer))

        if self.rndComputer == 3 and self.rndPlayer == 2:
            msgbox = QMessageBox.information(self, "Information", "Computer Wins")
            self.scoreComputer += 1
            self.scoreComputerText.setText("Computer Score: {score}".format(score=self.scoreComputer))

        if self.rndComputer == 3 and self.rndPlayer == 3:
            msgbox = QMessageBox.information(self, "Information", "Draw Game")

        if self.scoreComputer == 3:
            msgbox = QMessageBox.information(self, "Information", "Game Over. Computer Wins.")
            sys.exit()
        if self.scorePlayer == 3:
            msgbox = QMessageBox.information(self, "Information", "Game Over. Player Wins.")
            sys.exit()


    def playGame(self):
        self.rndComputer = randint(1, 3)
        if self.rndComputer == 1:
            self.imageComputer.setPixmap(QPixmap("images/rock.png"))
        elif self.rndComputer == 2:
            self.imageComputer.setPixmap(QPixmap("images/paper.png"))
        else:
            self.imageComputer.setPixmap(QPixmap("images/scissors.png"))

        self.rndPlayer = randint(1, 3)
        if self.rndPlayer == 1:
            self.imagePlayer.setPixmap(QPixmap("images/rock.png"))
        elif self.rndPlayer == 2:
            self.imagePlayer.setPixmap(QPixmap("images/paper.png"))
        else:
            self.imagePlayer.setPixmap(QPixmap("images/scissors.png"))


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
