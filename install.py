# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'install.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2145, 699)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(18, 70, 1971, 531))
        self.frame.setStyleSheet("border:1px solid grey;\n"
"border:none;\n"
"background:rgba(0,0,0,0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setMinimumSize(QtCore.QSize(1953, 513))
        self.stackedWidget.setMaximumSize(QtCore.QSize(1953, 513))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setGeometry(QtCore.QRect(0, 50, 1951, 261))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setStyleSheet("#frame_2 {\n"
"\n"
"\n"
"background:rgb(235, 235, 235);\n"
"color: rgb(130, 15, 55);\n"
"\n"
"border:none\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(600, 79, 21, 91))
        self.label.setStyleSheet("border-left:1px solid white")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(1440, 200, 111, 37))
        font = QtGui.QFont()
        font.setFamily("Raleway Thin")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"\n"
"background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.648, y2:0.642455, stop:0 rgba(152, 0, 0, 241), stop:1 rgba(152, 60, 24, 245));\n"
"border:1px solid rgb(234, 234, 234);\n"
"color:rgb(244, 244, 244);\n"
"}\n"
"\n"
"#pushButton_2:hover {\n"
"background:rgb(255, 255, 255);\n"
"}")
        self.pushButton_2.setIconSize(QtCore.QSize(21, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_3 = QtWidgets.QFrame(self.page)
        self.frame_3.setGeometry(QtCore.QRect(150, 20, 371, 321))
        self.frame_3.setStyleSheet("#frame_3 {background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.648, y2:0.642455, stop:0 rgba(152, 0, 0, 255), stop:1 rgba(152, 60, 24, 255));\n"
"\n"
"border-radius:10px}\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(40, 170, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Raleway Thin")
        font.setPointSize(-1)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font-size:13px;\n"
"color:rgb(189, 189, 189);\n"
"border:none;")
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(30, 50, 271, 36))
        font = QtGui.QFont()
        font.setFamily("Raleway Thin")
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font-size:30px;\n"
"color:rgb(189, 189, 189);\n"
"border:none;")
        self.label_3.setObjectName("label_3")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(109, 200, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Raleway Thin")
        font.setPointSize(-1)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("font-size:15px;\n"
"color:rgb(189, 189, 189);\n"
"border:none;")
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(39, 198, 51, 26))
        font = QtGui.QFont()
        font.setFamily("Raleway Thin")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font-size:15px;\n"
"color:rgb(189, 189, 189);\n"
"border:none;\n"
"font-weight:bold")
        self.label_10.setObjectName("label_10")
        self.frame_4 = QtWidgets.QFrame(self.page)
        self.frame_4.setGeometry(QtCore.QRect(720, 90, 601, 361))
        self.frame_4.setStyleSheet("background:rgb(242, 242, 242);\n"
"border-radius:10px")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea.setGeometry(QtCore.QRect(38, 70, 521, 261))
        self.scrollArea.setMinimumSize(QtCore.QSize(521, 261))
        self.scrollArea.setMaximumSize(QtCore.QSize(521, 261))
        self.scrollArea.setStyleSheet("/* HORIZONTAL SCROLLBAR */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(240, 240, 240);\n"
"    height: 15px;\n"
"    margin: 0 15px 0 15px;\n"
"    width:18px;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"/* HANDLE BAR HORIZONTAL */\n"
"QScrollBar::handle:horizontal {  \n"
"    background: rgba(240, 240, 240,.2);\n"
"    min-width: 10px;\n"
"    max_width:15px;\n"
"    width:18px;\n"
"    border-radius: 7px;\n"
"    height:1px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover{  \n"
"    background-color: rgba(240, 240, 240,.3);\n"
"    height:1px\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {  \n"
"    background-color: rgba(240, 240, 240,.4);\n"
"}\n"
"\n"
"/* BTN LEFT - SCROLLBAR */\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: nonergb(11, 11, 11);\n"
"    background-color: rgba(0,0,0,0);\n"
"    width: 18px;\n"
"    height:10px !important;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {  \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {  \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN RIGHT - SCROLLBAR */\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background-color: rgba(59, 59, 90,0);\n"
"    width: 15px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {  \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {  \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 521, 261))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(50, 20, 271, 36))
        font = QtGui.QFont()
        font.setFamily("Raleway Thin")
        font.setPointSize(-1)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font-size:30px;\n"
"color:rgb(99, 99, 99);\n"
"border:none;")
        self.label_4.setObjectName("label_4")
        self.frame_5 = QtWidgets.QFrame(self.page)
        self.frame_5.setGeometry(QtCore.QRect(680, 130, 591, 361))
        self.frame_5.setMinimumSize(QtCore.QSize(451, 361))
        self.frame_5.setStyleSheet("background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.636, y2:0.579545, stop:0 rgba(217, 107, 52, 255), stop:1 rgba(59, 2, 2, 255));\n"
"border-radius:10px")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_5.raise_()
        self.frame_4.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2145, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancle"))
        self.pushButton_2.setShortcut(_translate("MainWindow", "Esc"))
        self.label_5.setText(_translate("MainWindow", "KM PLAYER 64X"))
        self.label_3.setText(_translate("MainWindow", "Application found!"))
        self.label_11.setText(_translate("MainWindow", "www.sarzamindownload.com"))
        self.label_10.setText(_translate("MainWindow", "Host"))
        self.label_4.setText(_translate("MainWindow", "Versions:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
