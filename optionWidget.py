from optionWidgetQt import Ui_MainWindow as U
from PyQt5.QtCore import pyqtSignal ,QObject 
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QWidget, QHBoxLayout, \
    QGraphicsDropShadowEffect, QPushButton, QApplication, QComboBox




class option(QObject):

    def __init__(self,widget_To_Add, description, url):
        super().__init__()
        ui1 = U()
        MainWindow = QtWidgets.QMainWindow()
        ui1.setupUi(MainWindow)
        self.parent = ui1.frameToAdd
        self.widgetToAdd = widget_To_Add
        widget_To_Add.addWidget(self.parent)
        self.title = ui1.label
        self.getButton = ui1.pushButton
        self.title.setText(description)
        self.url = url
        self.description = description
        self.padd = ui1.frame

        # Shadows:
        shadow = QGraphicsDropShadowEffect(blurRadius=6, xOffset=0, yOffset=4)

        # Shadow implementation:
        self.padd.setGraphicsEffect(shadow)