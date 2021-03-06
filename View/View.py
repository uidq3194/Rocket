import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QLabel, QApplication, QWidget, QTextBrowser, QTextEdit, \
    QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QPalette, QIcon, QColor, QFont
from PyQt5.QtCore import pyqtSlot, Qt

import threading
import time
from Brain.Brain import MainBrain
textboxValue = ""
FinalAnsw = ""

class myThread (threading.Thread):
    print ("Start")
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        def getAnswer(unString):
            result = MainBrain(textboxValue)
            return result

        global textboxValue
        global FinalAnsw
        FinalAnsw = getAnswer(textboxValue)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'ChatBot'
        self.left = 40
        self.top = 40
        self.width = 650
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        pal = QPalette();
        pal.setColor(QPalette.Background, QColor(40, 40, 40));
        self.setAutoFillBackground(True);
        self.setPalette(pal);

        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setBold(True)
        font.setPixelSize(15)

        self.setStyleSheet("QTextEdit {color:#3d3838; font-size:12px; font-weight: bold}")

        historylabel = QLabel('View your conversation history here: ')
        historylabel.setStyleSheet('color: #82ecf9')
        historylabel.setFont(font)
        messagelabel = QLabel('Enter you message to the chat bot here:')
        messagelabel.setStyleSheet('color: #82ecf9')
        messagelabel.setFont(font)

        self.conversationBox = QTextBrowser(self)

        self.textbox = QTextEdit(self)

        self.button = QPushButton('Send message', self)
        self.button.setStyleSheet(
            "QPushButton { background-color:#82ecf9; color: #3d3838 }" "QPushButton:pressed { background-color: black }")

        grid = QGridLayout()
        grid.setSpacing(10)
        self.setLayout(grid)
        grid.addWidget(historylabel, 1, 0)
        grid.addWidget(self.conversationBox, 2, 0)
        grid.addWidget(messagelabel, 3, 0)
        grid.addWidget(self.textbox, 4, 0)
        grid.addWidget(self.button, 5, 0)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    def on_click(self):
        global textboxValue
        textboxValue = self.textbox.toPlainText()
        self.conversationBox.append("You: " + textboxValue)
        th = myThread()
        th.start()
        th.join()
        global FinalAnsw
        self.conversationBox.append("Rocket: " + FinalAnsw)
        self.textbox.setText("")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()