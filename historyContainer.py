

from h_Container import Ui_MainWindow as U1
from PyQt5.QtCore import pyqtSignal ,QObject 
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QWidget, QHBoxLayout, \
    QGraphicsDropShadowEffect, QPushButton, QApplication, QComboBox

class historyContainer(QObject):

    def __init__(self,widgetToAdd):
        super().__init__()
        ui = U1()
        MainWindow = QtWidgets.QMainWindow()
        ui.setupUi(MainWindow)

        shadow = QGraphicsDropShadowEffect(blurRadius=6, xOffset=0, yOffset=4)
        shadow1 = QGraphicsDropShadowEffect(blurRadius=6, xOffset=0, yOffset=2)

        self.parent = ui.frame
        self.historyArea = ui.horizontalLayout
        self.backBtn = ui.pushButton_2
        self.widgetToAdd = widgetToAdd
        self.widgetToAdd.addWidget(self.parent)
        self.scr = ui.scrollArea
        self.scr.setGraphicsEffect(shadow)
        self.backBtn.setGraphicsEffect(shadow1)
