from PyQt5 import QtWidgets, QtGui, QtCore, uic

from asrInterface import Ui_MainWindow
import sys

import speech_recognition as sr
import os


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.command = ""
        # Connect the button click signal to the recognize_speech slot
        self.recognizeButton.clicked.connect(self.recognize_speech)

    def recognize_speech(self):
        # Use speech recognition module to recognize speech
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            self.label.setText("Listening...")
            audio = r.listen(source)
        try:
            self.command = r.recognize_sphinx(audio)
            self.label.setText("You said: " + self.command)
        except sr.UnknownValueError:
            self.label.setText("Sorry, I did not understand that.")
        except sr.RequestError as e:
            self.label.setText("Could not request results from Google Speech Recognition service; {0}".format(e))

    def open_notepad(self):
        if "notepad" in self.command:
            os.system("notepad")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    # application.start_notepad()
    sys.exit(app.exec())
