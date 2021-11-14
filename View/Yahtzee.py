import sys
from PySide2 import QtWidgets
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QMainWindow, QPushButton
from form import Form

class Yahtzee(QMainWindow):

    @Slot()
    def say_hello(self):
        self.form = Form()
        self.form.show()
        # this form closes immediately because there's no permanent reference to form
        
    def __init__(self, parent=None):
        super(Yahtzee, self).__init__(parent)
        self.setWindowTitle("Yahtzee")

        #centralWidget = QtWidgets()
        

        # Create a button, connect it and show it
        button = QPushButton("Click me", self)
        button.clicked.connect(self.say_hello)
        button.show()