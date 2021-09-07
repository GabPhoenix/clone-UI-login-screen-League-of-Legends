# /////////////////////////////////////////////
# 
# By: GABRIEL CARVALHO
# PROJECT MADE WITH: PyQt5 and PySide6
# V: 1.0.0
# 
# Before use the codes, read the README.md and the documentation
# of PyQt5 and Pyside6
# 
# /////////////////////////////////////////////

#IMPORT MODULES
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

#IMPORT MAIN WINDOW
from UI_screen import Ui_MainWindow

#MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #SETUP MAIN WINDOW
        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self)

        #Show Aplication
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())