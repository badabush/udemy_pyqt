import os.path
import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtGui import QIcon
import random
from pygame import mixer
from mutagen.mp3 import MP3

import style

mixer.init()
song_list = []
muted = False
count = 0
song_length = 0
index = 0


class Player(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music Player")
        self.setGeometry(1500, 200, 480, 700)

        self.ui()
        self.show()

    def ui(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        # ****************************** Progress Bars **************************
        self.progress_bar = QProgressBar()
        self.progress_bar.setTextVisible(False)  # hide percentage progress bar information
        self.progress_bar.setStyleSheet(style.progressbar_style())

        # ****************************** Labels **************************
        self.song_timer_label = QLabel("0:00")
        self.song_length_label = QLabel("/ 0:00")

        # ****************************** Buttons **************************
        self.add_button = QToolButton()
        self.add_button.setIcon(QIcon("icons/add.png"))
        self.add_button.setIconSize(QSize(48, 48))  # need to import QSize
        self.add_button.setToolTip("add a Song")  # tooltip
        self.add_button.clicked.connect(self.add_sound)

        self.shuffle_button = QToolButton()
        self.shuffle_button.setIcon(QIcon("icons/shuffle.png"))
        self.shuffle_button.setIconSize(QSize(48, 48))
        self.shuffle_button.setToolTip("Shuffle Songs")  # tooltip
        self.shuffle_button.clicked.connect(self.shuffle_playlist)

        self.previous_button = QToolButton()
        self.previous_button.setIcon(QIcon("icons/previous.png"))
        self.previous_button.setIconSize(QSize(48, 48))
        self.previous_button.setToolTip("Play previous")  # tooltip
        self.previous_button.clicked.connect(self.play_previous)

        self.play_button = QToolButton()
        self.play_button.setIcon(QIcon("icons/play.png"))
        self.play_button.setIconSize(QSize(64, 64))
        self.play_button.setToolTip("Play")  # tooltip
        self.play_button.clicked.connect(self.play)

        self.next_button = QToolButton()
        self.next_button.setIcon(QIcon("icons/next.png"))
        self.next_button.setIconSize(QSize(48, 48))
        self.next_button.setToolTip("Play next")  # tooltip
        self.next_button.clicked.connect(self.play_next)


        self.mute_button = QToolButton()
        self.mute_button.setIcon(QIcon("icons/mute.png"))
        self.mute_button.setIconSize(QSize(24, 24))
        self.mute_button.setToolTip("Mute sound")  # tooltip
        self.mute_button.clicked.connect(self.mute)

        # ****************************** Volume Slider **************************
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setToolTip("Adjust Volume")
        self.volume_slider.setValue(70)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        mixer.music.set_volume(0.7)
        self.volume_slider.valueChanged.connect(self.set_volume)

        # ****************************** List Widget **************************
        self.play_list = QListWidget()
        self.play_list.doubleClicked.connect(self.play)
        self.play_list.setStyleSheet(style.playlist_style())

        # ****************************** Timer **************************
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_progress)

    def layouts(self):
        # ****************************** Creating Layouts ****************************
        self.main_layout = QVBoxLayout()
        self.top_main_layout = QVBoxLayout()
        self.top_group_box = QGroupBox("Music Player", self)
        self.top_group_box.setStyleSheet(style.groupbox_style())
        self.top_layout = QHBoxLayout()
        self.middle_layout = QHBoxLayout()
        self.bottom_layout = QVBoxLayout()

        # ****************************** Adding Widgets ******************************
        # ****************************** Top Layout Widgets **************************
        self.top_layout.addWidget(self.progress_bar)
        self.top_layout.addWidget(self.song_timer_label)
        self.top_layout.addWidget(self.song_length_label)

        # ****************************** Mid Layout Widgets **************************
        self.middle_layout.addStretch()
        self.middle_layout.addWidget(self.add_button)
        self.middle_layout.addWidget(self.shuffle_button)
        self.middle_layout.addWidget(self.previous_button)
        self.middle_layout.addWidget(self.play_button)
        self.middle_layout.addWidget(self.next_button)
        self.middle_layout.addWidget(self.volume_slider)
        self.middle_layout.addWidget(self.mute_button)
        self.middle_layout.addStretch()

        self.top_main_layout.addLayout(self.top_layout)
        self.top_main_layout.addLayout(self.middle_layout)
        self.top_group_box.setLayout(self.top_main_layout)
        self.main_layout.addWidget(self.top_group_box, 25)  # Aspect ratio
        self.main_layout.addLayout(self.bottom_layout, 75)

        # ****************************** Bot Layout Widgets **************************
        self.bottom_layout.addWidget(self.play_list)

        self.setLayout(self.main_layout)

    def add_sound(self):
        directory = QFileDialog.getOpenFileName(self, "Add Sound", "songs/", "Sound Files (*.mp3 *.ogg *.wav)")
        filename = os.path.basename(directory[0])
        self.play_list.addItem(filename)
        # global song_list
        song_list.append(directory[0])

    def shuffle_playlist(self):
        random.shuffle(song_list)
        self.play_list.clear()
        [self.play_list.addItem(os.path.basename(song)) for song in song_list]

    def play(self):
        global song_length
        global count
        global index
        count = 0
        index = self.play_list.currentRow()

        try:
            mixer.music.load(song_list[index])
            mixer.music.play()

            # start timer
            self.timer.start()

            sound = MP3(song_list[index])
            song_length = round(sound.info.length)
            self.progress_bar.setValue(0)
            self.progress_bar.setMaximum(song_length)
            # min, sec = divmod(song_length, 60)  # get minutes and seconds
            #
            # self.song_length_label.setText("/ {min}:{sec}".format(min=str(min), sec=str(sec)))
            self.song_length_label.setText(time.strftime("/ %M:%S", time.gmtime(song_length)))
        except:
            pass

    def set_volume(self):
        self.volume = self.volume_slider.value()
        mixer.music.set_volume(self.volume / 100)

    def mute(self):
        global muted

        if not muted:
            mixer.music.set_volume(0.0)
            muted = True
            self.mute_button.setIcon(QIcon("icons/unmuted.png"))
            self.mute_button.setToolTip("Unmute")
            self.volume_slider.setValue(0)
        else:
            mixer.music.set_volume(0.7)
            muted = False
            self.mute_button.setIcon(QIcon("icons/mute.png"))
            self.mute_button.setToolTip("Mute")
            self.volume_slider.setValue(70)

    def update_progress(self):
        global count
        global song_length

        count += 1
        self.progress_bar.setValue(count)
        self.song_timer_label.setText(time.strftime("%M:%S", time.gmtime(count)))
        if count == song_length:
            self.timer.stop()

    def play_previous(self):
        global song_length
        global count
        global index
        count = 0
        items = self.play_list.count()
        if index == 0:
            index = items
        index -= 1
        try:
            mixer.music.load(song_list[index])
            mixer.music.play()

            # start timer
            self.timer.start()

            sound = MP3(song_list[index])
            song_length = round(sound.info.length)
            self.progress_bar.setValue(0)
            self.progress_bar.setMaximum(song_length)
            # min, sec = divmod(song_length, 60)  # get minutes and seconds
            #
            # self.song_length_label.setText("/ {min}:{sec}".format(min=str(min), sec=str(sec)))
            self.song_length_label.setText(time.strftime("/ %M:%S", time.gmtime(song_length)))
        except:
            pass

    def play_next(self):
        global song_length
        global count
        global index
        count = 0
        items = self.play_list.count()
        index += 1
        if index == items:
            index = 0
        try:
            mixer.music.load(song_list[index])
            mixer.music.play()

            # start timer
            self.timer.start()

            sound = MP3(song_list[index])
            song_length = round(sound.info.length)
            self.progress_bar.setValue(0)
            self.progress_bar.setMaximum(song_length)
            # min, sec = divmod(song_length, 60)  # get minutes and seconds
            #
            # self.song_length_label.setText("/ {min}:{sec}".format(min=str(min), sec=str(sec)))
            self.song_length_label.setText(time.strftime("/ %M:%S", time.gmtime(song_length)))
        except:
            pass

    def keyPressEvent(self, event):
        # catches user key presses, close window on "ESCAPE"
        if event.key() == Qt.Key_Escape:
            self.close()


def main():
    app = QApplication(sys.argv)
    window = Player()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
