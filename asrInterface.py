# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asrInterface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        ui_width=400
        ui_height=500
        font_size=13
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(ui_width, ui_height)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 280, 250, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(font_size)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 250, 250, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(font_size)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.voiceFig = QtWidgets.QLabel(self.centralwidget)
        self.voiceFig.setGeometry(QtCore.QRect(120, 50, 160, 121))
        self.voiceFig.setText("")
        self.gif = QMovie("icon/voice.gif")
        self.voiceFig.setMovie(self.gif)
        self.gif.start()
        self.voiceFig.setScaledContents(True)
        self.voiceFig.setObjectName("voiceFig")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 160, 200, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(font_size)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 117, 210);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 310, 250, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(font_size)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.recognizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.recognizeButton.setGeometry(QtCore.QRect(100, 440, 200, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(font_size)
        self.recognizeButton.setFont(font)
        self.recognizeButton.setStyleSheet("background-color: rgb(0, 117, 210);\n"
                                           "color: rgb(255, 255, 255);")
        self.recognizeButton.setObjectName("recognizeButton")
        self.recognizeButton.setText("Recognize")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voice Assistant"))
        self.label_3.setText(_translate("MainWindow", "1. Enjoy music by saying \"Play music\""))
        self.label_2.setText(_translate("MainWindow", "You can:"))
        self.label.setText(_translate("MainWindow", "Hi! How can I help?"))
        self.label_4.setText(_translate("MainWindow", "2. Take some notes by saying \"Open Notepad\""))
        self.recognizeButton.setText(_translate("MainWindow", "Start Recognition"))
