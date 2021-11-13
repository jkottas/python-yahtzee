#specifically using Python 3.9.8 because PySide2 is not supported in Python 3.10
# pip install PySide2
import sys

from PySide2.QtWidgets import QApplication
from Yahtzee import Yahtzee


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    yahtzee = Yahtzee()
    yahtzee.show()
    
    # Run the main Qt loop
    app.exec_()