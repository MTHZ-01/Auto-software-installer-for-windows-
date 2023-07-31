from window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from downloadBox import installerGUI, downloaderGUI
from win10toast import ToastNotifier
import threading
from linkDownloader import download_file as df
from PyQt5.QtCore import pyqtSignal ,QObject 
from PyQt5.QtCore import QRect, QPropertyAnimation
from server import server
from notif import notif
from multiplayer import play
from PyQt5.QtMultimedia import QSound
import os
import PyQt5.QtCore as qtCore
from PyQt5.QtMultimedia import QMediaPlayer , QMediaContent
from PyQt5.QtCore import pyqtSignal ,QObject
from optionWidget import option
import time
import sys
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut, QDesktopWidget
from functools import partial
import pickle as p
from PyQt5.QtGui import QIcon
import qtawesome as qta
from operationSaver import saveProgress , openProgress , remover
from historyContainer import historyContainer
from historyWidget import historyWidget
import socket
from runner import runner
from PyQt5.QtWidgets import QWidget, QHBoxLayout, \
    QGraphicsDropShadowEffect, QPushButton, QApplication, QComboBox


class run(Ui_MainWindow):
    linkFound = pyqtSignal()
    addDownloadSignal = pyqtSignal(str,dict)
    timesUpSignal = pyqtSignal()
    addSignal2 = pyqtSignal(QtWidgets.QFrame)
    hideSignal = pyqtSignal()
    didNotFindLink = pyqtSignal()
    downloadOptionClickedSignal = pyqtSignal()
    notifSignal = pyqtSignal(QtWidgets.QFrame)
    notifSoundPlaySignal = pyqtSignal()
    serverDownSignal = pyqtSignal()
    fileOpenedSignal =pyqtSignal(dict)
    fileProblemSignal = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        
        self.bootSound = play("C:/Users/Alucard's PC/Desktop/c/SOUND/BOOT.mp3")
        SoundThread = threading.Thread(target=self.bootSound.play_sound)
        SoundThread.start()
        
    



    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        styleSheet = "QMainWindow::separator { width: 0px; height: 0px; }"
        MainWindow.setStyleSheet(styleSheet)
        self.shadow = QGraphicsDropShadowEffect(blurRadius=6, xOffset=0, yOffset=4)

        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))


        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)        

        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        # Btn signals:
        self.pushButton_2.clicked.connect(lambda: os.system('TASKKILL /F /PID ' + str(os.getpid())))
        self.pushButton_7.clicked.connect(self.historyBtnEvent)

        # Custom signals:
        self.fileOpenedSignal.connect(self.historySuccessEvent)
        self.fileProblemSignal.connect(self.historyFailEvent)

        # Attempting to get the cycle:
        self.addSignal2.connect(self.verticalLayout.addWidget)
        self.didNotFindLink.connect(lambda: self.notify(5,"Didn't find","We didn't find the application","you were looking for 😭"))
        self.toggle_top()
        self.toggle_top()
        self.toggle_top()




        def notifSound():
            self.c = play("C:/Users/Alucard's PC/Desktop/c/SOUND/notif.wav")
            self.soundT = threading.Thread(target=self.c.play_sound)
            self.soundT.start()
            
        self.notifSoundPlaySignal.connect(notifSound)




        self.pushButton_3.clicked.connect(self.linkFinderThread)


        ## signals:
        self.addDownloadSignal.connect(self.addDownloadOption)
        self.serverDownSignal.connect(self.serverDownSignalEvent)
        #


        self.addedNotifs = []
        self.addedPopUps = []

        self.verticalLayout.parentWidget().lower()

        # Shadows:
        lstOfShadowWidgets = [self.frame_11,self.pushButton_3,self.pushButton_7]
        shadow = QGraphicsDropShadowEffect(blurRadius=6, xOffset=0, yOffset=1)
        shadow1 = QGraphicsDropShadowEffect(blurRadius=6, xOffset=0, yOffset=1)
        shadow2 = QGraphicsDropShadowEffect(blurRadius=6, xOffset=0, yOffset=1)
        shadow3 = QGraphicsDropShadowEffect(blurRadius=6, xOffset=0, yOffset=1)
        lstOfShadowWidgets[0].setGraphicsEffect(shadow)
        lstOfShadowWidgets[1].setGraphicsEffect(shadow1)
        lstOfShadowWidgets[2].setGraphicsEffect(shadow2)
        self.comboBox.setGraphicsEffect(shadow3)


    def serverDownSignalEvent(self):
        self.notify(8,"API ERROR","API maulfunctioned.","try again.")

    

    

    def linkFinderThread(self):

        IPaddress=socket.gethostbyname(socket.gethostname())

        if IPaddress == "127.0.0.1":
            self.notify(5,"No connection","You are not connected to the internet.")
            return
        query = self.lineEdit.text()
        if query == "":
            print("empty")

            self.notify(3,"Empty Value","please enter software name")
            return 
        
        

        self.pushButton_3.setText("Searching . . .")
        self.pushButton_3.setEnabled(False)



        self.notify(7,"Searching . . .","you'll be directed to another page" )
        self.notifSoundPlaySignal.emit()



        self.finderThred = threading.Thread(target=self.linkFinder)
        self.finderThred.start()



        


    def linkFinder(self):
        query = self.lineEdit.text()
        
        def serverDownEvent():
            self.serverDownSignal.emit()
            return

        try:
            comboVal = self.comboBox.currentText()
            site = ""
            if comboVal == "yasdl":
                print("yasdl")
                site = "yasdl"
            elif comboVal == "sarzmindownload":
                print("sarzamin")
                site = "sarzamin"

            s = server(query, site)
            j = s.jsonDict

            if j == {}:
                self.notify(5,"Couldn't find", "We couldn't find the specified query","Anywhere.")
                return
            

        except Exception as e:
            print(e)
            print("failed !")
            self.pushButton_3.setText("Find")
            self.pushButton_3.setEnabled(True)
            self.serverDownSignal.emit()
            
            return

        self.addDownloadSignal.emit(query,j)

    
        
    def notify(self,duration:int,title ="",line_1="", Line_2 = ""):
        self.verticalLayout.parentWidget().raise_()
        for item in self.addedNotifs:
            item.hide()
        n = notif(self.verticalLayout,duration)
        n.title.setText(title)
        n.line1.setText(line_1)
        n.line2.setText(Line_2)
        self.notifSoundPlaySignal.emit()
        self.addedNotifs.append(n.parent)        


    def stimulize(self):
        self.popUpStack.raise_()
        # self.verticalLayout_3.raise_()
        self.popUpStack.setStyleSheet("""
        #popUpStack {background:rgba(1,1,1,.9)}
        """)

    def normalize(self):
        self.popUpStack.lower()
        self.popUpStack.setStyleSheet("""
    background:rgba(1,1,1,0)
    """)


    def addDownloadOption(self,query,jsonDict):
        # o = option(x.VersionArea,"foo", "sada")
        x = installerGUI(self.verticalLayout_3,jsonDict, query,siteName=self.comboBox.currentText() )
        # self.verticalLayout_3.addWidget(x.parent)
        for i in self.addedPopUps:
            i.hide()
        self.addedPopUps.append(x.parent)
        self.stimulize()
        for i in jsonDict:
            print(i)
            print(jsonDict[i])
            o = option(x.VersionArea,i, jsonDict[i][0])
            # x.VersionArea.addWidget(o.parent)
            o.getButton.clicked.connect(partial(self.addDownloadState, self.comboBox.currentText(),jsonDict[i][0]))
            o.getButton.clicked.connect(x.parent.hide)
            o.getButton.clicked.connect(self.normalize)


        def cancleEvent():
            x.parent.hide()
            self.pushButton_3.setText("Find")
            self.pushButton_3.setEnabled(True)
            self.normalize()
        x.cancleBtn.clicked.connect(cancleEvent)
        







    def addDownloadState(self, siteName,url ):
        def downloadStartEvent():

            self.notify(5,"DownloadStarted","The file is now being","downloaded . . .")

        def downloadCancleEvent():                        
            self.pushButton_3.setText("Find")
            self.pushButton_3.setEnabled(True)
            self.notify(5,"Cancled ☠️","User canceled the download.")

        def downloadPauseEvent():

                
            self.notify(5,"Paused 😶‍🌫️","User paused the download.")

        def downloadResumeEvent():


            self.notify(5,"Resumed 😍","User resumed the download.")


        def netErrorEvent():

            self.notify(16,"Net error 😭","Your connection was interrupted!.")

            

        x = downloaderGUI(self.horizontalLayout,siteName,url,query= self.lineEdit.text() )
        def saveEvent(d):
            self.notify(5,"Saved !","Your search results has been saved!")
            self.pushButton_3.setText("Find")
            self.pushButton_3.setEnabled(True)
            
            saveProgress(d)

        x.saveSignal.connect(saveEvent)
        # x.networkErrorSignal.connect(netErrorEvent)
        # x.downloadStartSignal.connect(downloadStartEvent)
        x.downloadCancleSignal.connect(downloadCancleEvent)
        x.downloadPauseSignal.connect(downloadPauseEvent)
        x.downloadResumeSignal.connect(downloadResumeEvent)
        print(x.url)

        x.progressBar.setValue(0)

        # x.downloadFinishedSignal.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        # x.downloadFinishedSignal.connect(lambda:self.notify(5,"Succsess 😁👍","Download was finished succesfully"))

    # Event functions:
    def historyBtnEvent(self):


        f = openProgress()
        f.fileOpenedSignal.connect(self.fileOpenedSignal.emit)
        f.fileProblemSignal.connect(self.fileProblemSignal)
        f.OpenFile()

    def historyFailEvent(self):

        self.notify(5,"Failed to open","Application files had been moved or","modified.")


    def noHistoryEvent(self,d):
        if d == {}:
            self.notify(5,"No history","there are currently no history to show")


    def historySuccessEvent(self,d):
        if d == {}:
            self.noHistoryEvent(d)
            return
        self.stimulize()
        for i in self.addedPopUps:
            i.hide()
        h = historyContainer(self.verticalLayout_3)
        self.addedPopUps.append(h.parent)
        def backEvent():
            self.normalize()
            h.parent.hide()
        h.backBtn.clicked.connect(backEvent)
        
        for i in d:
            siteName = d[i]["siteName"]
            pathExe = d[i]["pathToExe"]
            pathRar = d[i]["pathToRar"]

            wh = historyWidget(h.historyArea,i,siteName,pathExe, pathRar)

            def runEvent(p):
                print("runing")
                r = runner()
                r.openfile(p)

            def delEvent(data):
                deletor = remover(data[0],data[1], data[2])
                self.notify(5,"Removed", "Files had been removed successfully!")

            wh.delSignal.connect(delEvent)
            wh.runSignal.connect(runEvent)


    def toggle_top(self):
        try:
            if self.windowFlags() & QtCore.Qt.WindowStaysOnTopHint:
                self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
                self.showNormal()
                self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
                self.show()
        except Exception as e:
            print("Didn't toggle")
            print(e)



class MyMainWindow(QtWidgets.QMainWindow, run):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.animation_started = False
        # self.toggle_top()



    def showEvent(self, event):
        try:

            if not self.animation_started:   
                self.animation_started = True
                self.animation = QPropertyAnimation(self, b"windowOpacity")
                self.animation.setDuration(500)
                self.animation.setStartValue(0)
                self.animation.setEndValue(1)
                self.animation.start()
        except:pass
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    def kill():
        os.system('TASKKILL /F /PID ' + str(os.getpid()))
    app.aboutToQuit.connect(kill)
    window = MyMainWindow()
    # window.move(app.desktop().screen().rect().center() - window.rect().center())
    window.show()

    sys.exit(app.exec_())