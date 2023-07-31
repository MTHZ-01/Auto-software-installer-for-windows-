from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from os import startfile
from PyQt5 import QtCore, QtGui, QtWidgets
from install import Ui_MainWindow as U1
from downloadStart import Ui_MainWindow as U2
from os.path import exists
from PyQt5.QtCore import pyqtSignal ,QObject 
import threading
import PyQt5
from urllib.request import urlretrieve
from os.path import basename
from unrar import rarfile
from os import mkdir , walk
from shutil import rmtree , move
from subprocess import run
from zipfile import ZipFile
from requests import get
import time
from multiplayer import play
from optionWidget import option 
from connectionCheck import checkNet
from os import startfile
from actualDownloader import downloader
from extractor import extractor
from runner import runner
from PyQt5.QtWidgets import QWidget, QHBoxLayout, \
    QGraphicsDropShadowEffect, QPushButton, QApplication, QComboBox

import re









class installerGUI(QObject):
    chooseSignal_Installer = pyqtSignal(str, str)
    def __init__(self,widgetToAdd,jsonDict,query,siteName="yasdl"):
        super().__init__()
        ui2 = U1()
        MainWindow = QtWidgets.QMainWindow()
        ui2.setupUi(MainWindow)

        self.jsonDict = jsonDict
        self.parent = ui2.frame
        self.hostAddress = ui2.label_11
        self.name = ui2.label_5
        self.name.setText(query)
        self.siteName = siteName
        self.VersionArea = ui2.verticalLayout
        self.query = query
        widgetToAdd.addWidget(self.parent)
        # widgetToAdd.parentWidget().raise_()
        self.cancleBtn = ui2.pushButton_2
        self.hostAddress.setText(siteName)





    
    
        

class downloaderGUI(PyQt5.QtCore.QObject):

    internetStatusSignal = pyqtSignal(bool)
    downloadSuccessTruenerSignal = pyqtSignal()
    saveSignal = pyqtSignal(dict)
    downloadCancleSignal = pyqtSignal()
    downloadPauseSignal = pyqtSignal()
    downloadResumeSignal = pyqtSignal()
    def playSound(self,path):
        play(path)

    def __init__(self,widgetToAdd,siteName, url,query):
        super().__init__()
        self.connected = True
        self.downloadSuccsess = False
        self.rarFileDirectories = None
        self.exeDir = None
        self.query =query
        self.cancle = False
        

        ui = U2()
        MainWindow = QtWidgets.QMainWindow()
        ui.setupUi(MainWindow)
        self.siteName = siteName
        widgetToAdd.addWidget(ui.frame)


        self.padd = ui.stackedWidget_5
        self.parent = ui.frame
        self.mainTitle = ui.label_3
        self.upRightTitle = ui.label_18
        self.downLeftTitle = ui.label_19
        self.status = ui.label_6
        self.name = ui.label_5
        self.webAddressTitle = ui.label_11
        self.progressBar = ui.progressBar
        self.cancleBtn = ui.pushButton
        self.openBtn = ui.pushButton_4
        self.doneBtn = ui.pushButton_3
        self.rightBtnBox = ui.stackedWidget_3
        self.leftBtnBox = ui.stackedWidget_2    
        self.openBtnPage = ui.page_6
        self.doneBtnPage = ui.page_4
        self.pauseBtn = ui.pushButton_2
        self.appNameTitle = ui.label_5
        self.url = url
        
            
        # Lable handling:
        self.appNameTitle.setText(query)
        self.webAddressTitle.setText(siteName)
        
        # To Be threaded:
        self.internet = checkNet(self.url)
        self.downloader = downloader(self.url)
        self.extractor = extractor(self.siteName)
        self.runner = runner()

        # Signals:


        # Thread Signals:
        self.internet.serverDownSignal.connect(lambda : self.internetStatusSignal.emit(False))
        self.internet.serverUpSignal.connect(lambda : self.internetStatusSignal.emit(True))
        self.internetStatusSignal.connect(self.connectionStatusSetter)
        self.downloader.percenageSignal.connect(self.progressBar.setValue)
        self.downloader.extractReadySignal.connect(self.extractReadyEvent)

        self.openBtn.clicked.connect(self.run)
        self.extractor.extractionComplete_directorySignal.connect(self.exeSet)
        self.downloadSuccessTruenerSignal.connect(self.downloadSuccessTruener)
        self.doneBtn.clicked.connect(self.saveEvent)
            # one thread is in extractReadyEvent function

        # Threads:
        w = threading.Thread(target=self.watchDog)
        d = threading.Thread(target=self.downloadFile)
        uLT = threading.Thread(target=self.upLeft_SwitchDog)
        dRT = threading.Thread(target=self.downRight_SwitchDog)


        # Thread starts:
        w.start()
        d.start()
        uLT.start()
        dRT.start()
        # Shadows:
        shadow = QGraphicsDropShadowEffect(blurRadius=6, xOffset=0, yOffset=1)
        
        # Shadow applyment:
        self.padd.setGraphicsEffect(shadow)

        # Btn handling:
        self.cancleBtn.clicked.connect(self.cancleEvent)

    # Functions: 
    
    def upLeft_SwitchDog(self):
        while not self.downloadSuccsess:
            self.upRightTitle.setText("Your request is being handled")
            time.sleep(4)
            self.upRightTitle.setText("The file will be downloaded")
            time.sleep(4)
            self.upRightTitle.setText("You'll be in the exe file")
            time.sleep(4)
        else:
            self.upRightTitle.setText("Your File is ready !")

    def downRight_SwitchDog(self):
        while not self.downloadSuccsess:
            time.sleep(1)
            self.downLeftTitle.setText("You'll be there in no time !")
            time.sleep(4)
            self.downLeftTitle.setText("Feel free to roam around . . .")
            time.sleep(4)
            self.downLeftTitle.setText("Don't worry about the details . . .")
            time.sleep(4)
        else:
            self.downLeftTitle.setText("Hit 'Open' to install.")


    
    def watchDog(self):
        
        # Checking internet:
        print(" >>WatchDog<< : Checking connection . . .")
        self.internet.startCycle()

        
    def connectionStatusSetter(self,status:bool):
        # Thread Triger Only!
        self.connected = status
        # print(status)

        if status == False:
            self.serverDownEvent()

        elif status == True:
            self.serverUpEvent()


    def downloadSuccessTruener(self):
        self.downloadSuccsess = True


    def downloadFile(self):
        while self.status and not self.downloadSuccsess:
            self.pauseBtn.disconnect()
            self.pauseBtn.clicked.connect(self.pauseEvent)
            self.downloader.download_file()
            break
            
    def exeSet(self,exeDir):
        self.exeDir = exeDir
    
    def run(self):
        self.runner.installSignal.emit(self.exeDir)        

    # Event functions:


    def serverDownEvent(self):
        if not self.downloadSuccsess :
            self.mainTitle.setText("Interrupted")
            self.status.setText("Waiting for connection . . . ")
    
    
    def serverUpEvent(self):
        previous_state = self.status.text()
        previousTitle = self.mainTitle.text()

        if previousTitle == "Interrupted" and previous_state == "Waiting for connection . . . " and not self.downloadSuccsess:
            self.mainTitle.setText("Resumed")
            self.status.setText("Connection Stablished, downloading . . .")
            # Recreating the download thread:
            d = threading.Thread(target=self.downloadFile)
            d.start()

    
    def extractReadyEvent(self,dirLits):
        print("extractReadyEvent: proccess started . . .")
        self.downloadSuccessTruenerSignal.emit()
        self.mainTitle.setText("Download Success !")
        self.status.setText("Download has been compeleted successfully.")
        self.rightBtnBox.setCurrentWidget(self.openBtnPage)        
        self.leftBtnBox.setCurrentWidget(self.doneBtnPage)
        self.rarFileDirectories = dirLits
        self.extractEvent()
        

    def extractEvent(self):
        print("extractEvent: proccess started . . .")
        self.extractor.startExtractSignal.emit(self.rarFileDirectories)



    def saveEvent(self):
        query = self.query
        name = self.name.text()
        siteName = self.siteName
        try:
            pathToEXE = self.exeDir[0]
        except:
            pathToEXE = self.exeDir

        pathToRAR = self.rarFileDirectories[0]
        d = {query:{"name":name, "siteName": siteName, "pathToExe":pathToEXE, "pathToRar": pathToRAR}}
        self.parent.hide()
        

        self.saveSignal.emit(d)


    def pauseEvent(self):
        self.status.setText("Paused")
        self.mainTitle.setText("Paused")
        self.downloader.downloadPauseSignal.emit()
        self.downloadPauseSignal.emit()
        self.pauseBtn.setText("Resume")
        self.pauseBtn.clicked.connect(self.resumeEvent)    

    def resumeEvent(self):
        self.status.setText("Resumed")
        self.mainTitle.setText("Resumed")
        self.pauseBtn.disconnect()
        self.downloader.downloadResumeSignal.emit()
        self.downloadResumeSignal.emit()
        self.pauseBtn.setText("Pause")
        self.pauseBtn.clicked.connect(self.pauseEvent)    

    def downloadStartEvent(self):
        self.status.setText("Downloading . . .")
        self.mainTitle.setText("Now downloading")
    

    def cancleEvent(self):

        # self.internetStatusSignal.emit(False)
        self.parent.hide()
        self.pauseEvent()
        self.downloadCancleSignal.emit()
        self.downloader.downloadCancleSignal.emit()

