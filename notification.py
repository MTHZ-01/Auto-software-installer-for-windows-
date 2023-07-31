# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notification.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(120, 310, 571, 191))
        self.frame.setMinimumSize(QtCore.QSize(571, 191))
        self.frame.setMaximumSize(QtCore.QSize(571, 191))
        self.frame.setStyleSheet("background:rgb(242, 242, 242);\n"
"border-radius:15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(110, 30, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Raleway Thin")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("\n"
"color:rgb(104, 104, 104);\n"
"background:rgba(0,0,0,0);\n"
"padding-left:5px;\n"
"padding-bottom:3px;\n"
"font-weight:bold;")
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(113, 53, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Raleway Thin")
        font.setPointSize(12)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("\n"
"color:rgb(104, 104, 104);\n"
"background:rgba(0,0,0,0);\n"
"padding-left:5px;\n"
"padding-bottom:3px")
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(113, 70, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Raleway Thin")
        font.setPointSize(12)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("\n"
"color:rgb(189, 189, 189);\n"
"background:rgba(0,0,0,0);\n"
"padding-left:5px;\n"
"padding-bottom:3px")
        self.label_21.setText("")
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(28, 22, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Raleway Thin")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("border:1px solid rgb(132, 0, 0);\n"
"color:rgb(189, 189, 189);\n"
"background:rgba(0,0,0,0);\n"
"padding-left:5px;\n"
"padding-bottom:3px;\n"
"font-weight:bold;")
        self.label_22.setScaledContents(False)
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 119, 571, 71))
        self.frame_2.setStyleSheet("#frame_2 {\n"
"background:rgb(242, 238, 237);\n"
"border-top-right-radius:0px;\n"
"border-top-left-radius:0px;\n"
"border-top:1px solid rgb(249, 249, 249)\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(405, 16, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Raleway Thin")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("#pushButton{\n"
"\n"
"background:rgb(148, 27, 27);\n"
"border:3px solid rgb(236, 236, 236);\n"
"color:rgb(244, 244, 244);\n"
"\n"
"border-radius:0px;\n"
"}\n"
"\n"
"#pushButton:hover {\n"
"background:rgb(255, 255, 255);\n"
"}")
        self.pushButton.setIconSize(QtCore.QSize(21, 21))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_19.setText(_translate("MainWindow", "Searching started"))
        self.label_20.setText(_translate("MainWindow", "you will be transfered into another page . . ."))
        self.label_22.setText(_translate("MainWindow", "UI"))
        self.pushButton.setText(_translate("MainWindow", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
