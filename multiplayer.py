from PyQt5.QtMultimedia import QSound
import os
import PyQt5.QtCore as qtCore
from PyQt5.QtMultimedia import QMediaPlayer , QMediaContent
from PyQt5.QtCore import pyqtSignal ,QObject
from playsound import playsound
import threading


class play:
    def __init__(self,path):
        self.p = path
        # self.play_sound()



    def play_sound(self):
        playsound(self.p)




# play("C:/Users/Alucard's PC/Desktop/c/SOUND/BOOT.mp3")