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
        desktop=QtWidgets.QApplication.desktop()
        screenHeight=desktop.screenGeometry().height()
        screenWidth=desktop.screenGeometry().width()
        # print(screenHeight,screenWidth)
        uiWidth=int((500/1920)*screenWidth)
        uiHeight=int((700/1080)*screenHeight)
        fontSize=13
        voiceWidth=int((250/1920)*screenWidth)
        voiceHeight=int((200/1080)*screenHeight)
        voicePosX=(uiWidth-voiceWidth)//2
        voicePosY=0
        labelWidth=uiWidth//3*2
        labelHeight=int((160/1080)*screenHeight)
        labelPosX=(uiWidth-labelWidth)//2
        labelPosY=voicePosY+voiceHeight
        label2Width=int((350/1920)*screenWidth)
        label2Height=int((30/1080)*screenHeight)
        label2PosX=(uiWidth-label2Width)//2
        label2PosY=labelPosY+labelHeight+int((80/1080)*screenHeight)
        label3Width=uiWidth//4*3
        label3Height=int((51/1080)*screenHeight)
        label3PosX=(uiWidth-label3Width)//2
        label3PosY=label2PosY+label2Height+int((10/1080)*screenHeight)
        label4Width=label3Width
        label4Height=label3Height
        label4PosX=(uiWidth-label4Width)//2
        label4PosY=label3PosY+label3Height+int((10/1080)*screenHeight)
        buttonWidth=int((200/1920)*screenWidth)
        buttonHeight=int((31/1080)*screenHeight)
        buttonPosX=(uiWidth-buttonWidth)//2
        buttonPosY=uiHeight-buttonHeight-int((40/1080)*screenHeight)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(uiWidth, uiHeight)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(label3PosX, label3PosY, label3Width, label3Height))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(fontSize)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(label2PosX, label2PosY, label2Width, label2Height))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(fontSize)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.voiceFig = QtWidgets.QLabel(self.centralwidget)
        self.voiceFig.setGeometry(QtCore.QRect(voicePosX, voicePosY, voiceWidth, voiceHeight))
        self.voiceFig.setText("")
        self.gif = QMovie("icon/voice.gif")
        self.voiceFig.setMovie(self.gif)
        self.gif.start()
        self.voiceFig.setScaledContents(True)
        self.voiceFig.setObjectName("voiceFig")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(labelPosX, labelPosY, labelWidth, labelHeight))
        self.label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(fontSize)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 117, 210);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(label4PosX, label4PosY, label4Width, label4Height))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(fontSize)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.recognizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.recognizeButton.setGeometry(QtCore.QRect(buttonPosX, buttonPosY, buttonWidth, buttonHeight))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(fontSize)
        self.recognizeButton.setFont(font)
        self.recognizeButton.setStyleSheet("QPushButton {\n"
                                     "    background-color: #2196F3;\n"
                                     "    border: none;\n"
                                     "    color: white;\n"
                                     "    padding: 8px 16px;\n"
                                     "    text-align: center;\n"
                                     "    text-decoration: none;\n"
                                     "    display: inline-block;\n"
                                     "    font-size: 14px;\n"
                                     "    font-weight: 500;\n"
                                     "    border-radius: 4px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: #64B5F6;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color: #1976D2;\n"
                                     "}")
        self.recognizeButton.setObjectName("recognizeButton")
        self.recognizeButton.setText("Recognize")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voice Assistant"))
        self.label_3.setText(_translate("MainWindow", "1. Open the system settings by saying \"Open Settings\""))
        self.label_2.setText(_translate("MainWindow", "You can:"))
        self.label.setText(_translate("MainWindow", "Hi! How can I help?"))
        self.label_4.setText(_translate("MainWindow", "2. Take some notes by saying \"Open Notepad\""))
        self.recognizeButton.setText(_translate("MainWindow", "Start Recognition"))
