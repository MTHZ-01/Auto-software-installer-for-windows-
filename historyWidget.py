from h_widget import Ui_MainWindow as U1
from PyQt5.QtCore import pyqtSignal ,QObject 
from PyQt5 import QtCore, QtGui, QtWidgets
from runner import runner
import threading
from PyQt5.QtWidgets import QWidget, QHBoxLayout, \
    QGraphicsDropShadowEffect, QPushButton, QApplication, QComboBox

class historyWidget(QObject):
    runSignal = pyqtSignal(list)
    delSignal = pyqtSignal(tuple)
    def __init__(self,widgetToAdd,query ,siteName, pathToExe, pathToRar):
        super().__init__()  

        ui = U1()
        MainWindow = QtWidgets.QMainWindow()
        ui.setupUi(MainWindow)
        shadow = QGraphicsDropShadowEffect(blurRadius=8, xOffset=0, yOffset=8)
        self.parent = ui.frame    
        self.parent.setGraphicsEffect(shadow)
        self.titleLable = ui.label_19
        self.siteLable= ui.label_20
        self.deleteBtn = ui.pushButton_8
        self.installBtn = ui.pushButton_7
        self.widgetToAdd = widgetToAdd
        self.widgetToAdd.addWidget(self.parent)
        self.titleLable.setText(query)
        self.siteLable.setText(siteName)
        self.pathExe = pathToExe
        self.pathRar = pathToRar
        self.query = query
        self.installBtn.clicked.connect(lambda :self.runSignal.emit([self.pathExe]))
        self.deleteBtn.clicked.connect(self.delEvent)


    def delEvent(self):
        self.parent.hide()
        self.delSignal.emit((self.query, self.pathExe, self.pathRar))