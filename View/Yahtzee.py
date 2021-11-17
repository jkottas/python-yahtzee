import sys
from PySide2 import QtWidgets
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QDialog, QGridLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QWidget
from Model.player import Player
from View.form import Form

class Yahtzee(QMainWindow):

    @Slot()
    def say_hello(self):
        self.form = Form()
        self.form.show()
        # this form closes immediately because there's no permanent reference to form
        
    def __init__(self, parent=None):
        super(Yahtzee, self).__init__(parent)
        self.setWindowTitle("Yahtzee")

        p1 = Player("Jim", 6)

        # using layouts to make things look nice
        # https://www.pythonguis.com/tutorials/pyside-layouts/
        layout = QGridLayout()
        
        button = QPushButton("Click me", self)
        button.clicked.connect(self.say_hello)
        layout.addWidget(button, 0, 0)

        label = QLabel("howdy", self)
        label.setText(str(p1))
        layout.addWidget(label, 1, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)