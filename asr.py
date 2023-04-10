from PyQt5 import QtWidgets, QtGui, QtCore, uic

from asrInterface import Ui_MainWindow
import sys

import speech_recognition as sr
import os
import threading


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.command = ""
        self.is_recording = False
        self.recognizeButton.setText("Click to Speak")
        # Connect the button click signal to the startRecording slot
        self.recognizeButton.pressed.connect(self.startRecording)
        self.recognizeButton.released.connect(self.stopRecording)

    def recognitionSpeech(self, audioList):
        # Use speech recognition module to recognize speech
        r = sr.Recognizer()
        try:
            self.label.setText("wait for a minute, I'm recognizing...")
            for audio in audioList:
                self.command += r.recognize_google(audio)
            self.label.setText("You said: " + self.command)
            self.openNotepad()
            self.openSettings()
            self.command = ""
        except sr.UnknownValueError:
            self.label.setText("Sorry, I did not understand that.")
        except sr.RequestError as e:
            self.label.setText("Could not request results ; {0}".format(e))

    def recordAudio(self):
        # Record audio using microphone until stopRecording is called
        audioList = []
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            while self.is_recording:
                audioList.append(r.listen(source, phrase_time_limit=3))
            self.recognitionSpeech(audioList)

    def startRecording(self):
        self.is_recording = True
        self.recognizeButton.setText("Listening...")
        self.label.setText("Listening...")
        thread = threading.Thread(target=self.recordAudio)
        thread.start()

    def stopRecording(self):
        self.is_recording = False
        self.recognizeButton.setText("Click to Speak")
        # while self.event.isSet():
        # self.label.setText("wait for a minute, I'm recognising...")
        # Check if the command contains "notepad" and open notepad if it does

    def openNotepad(self):
        if "notepad" in self.command.lower():
            os.system("notepad")

    def openSettings(self):
        if "settings" in self.command.lower():
             os.startfile("ms-settings:")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())
