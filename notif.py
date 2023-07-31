from notification import Ui_MainWindow as U
from PyQt5.QtCore import pyqtSignal ,QObject 
import time
import threading
from PyQt5.QtCore import pyqtSignal ,QObject 
from PyQt5.QtCore import QObject
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QHBoxLayout, \
    QGraphicsDropShadowEffect, QPushButton, QApplication, QComboBox

from multiplayer import play

class notif(QObject):
    timesUpSignal = pyqtSignal()
    addSignal = pyqtSignal()
    # hideSignal = pyqtSignal()
    def __init__(self,layOutToAdd,t:int, tite="default title", line_1 = "default line", line_2="default line") -> None:
        super().__init__()

        
        

        ui = U()
        MainWindow = QtWidgets.QMainWindow()
        ui.setupUi(MainWindow)
        self.layOutToAdd = layOutToAdd
        self.parent = ui.frame
        
        self.layOutToAdd.addWidget(self.parent)
        self.title = ui.label_19
        self.line1 = ui.label_20
        self.line2 = ui.label_21
        self.okBtn = ui.pushButton
        self.title.setText(tite)
        self.line1.setText(line_1)
        self.line2.setText(line_2)
        shadow = QGraphicsDropShadowEffect(blurRadius=6, xOffset=0, yOffset=2)
        self.t = t
        self.okBtn.clicked.connect(self.parent.hide)
        self.okBtn.clicked.connect(self.layOutToAdd.parentWidget().lower)
        # print("add_1 Emitted! ")
        # self.layOutToAdd.addWidget(self.parent)
        # self.okBtn.clicked.connect(self.hideSignal.emit)
        self.parent.setGraphicsEffect(shadow)
        t= threading.Thread(target=self.timeUp)
        t.start()


    # def trigerAdd(self):
        # self.addSignal.emit()

    def terminate(self):
        self.parent.hide()

    def timeUp(self):
        try:
            # self.c.play_sound()
            time.sleep(self.t)
            self.parent.hide()
            self.layOutToAdd.parentWidget().lower()
        except: pass

