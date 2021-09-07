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

from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6 import QtGui
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PyQt5.QtGui import QIcon 
import sys


class Ui_MainWindow(object):
    def setup_ui(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(35, 50, 1300, 620)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QWidget(MainWindow)
        self.horizontalLayout = QHBoxLayout(self.centralwidget) 
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
	
        # LEFT FRAME
        self.frame_left = QFrame(self.centralwidget)
        self.frame_left.setMaximumSize(QSize(350, 620))
        self.frame_left.setStyleSheet("background-color: rgb(255, 255, 255)")
        
        # icon 
        self.icon_label = QLabel(self.frame_left)
        self.icon_label.setGeometry(135, 40, 80, 80)
        self.icon_label.setPixmap('C:\\Users\\PC\\Desktop\\Gabriel\\ui_lol\\Basic-window-Pyside-Pyqt5-main\\img\\L.png')

        # ask
        self.ask = QPushButton(self.frame_left)
        self.ask.setGeometry(270, 20, 20, 20)
        self.ask.setIcon(QtGui.QPixmap('C:\\Users\\PC\\Desktop\\Gabriel\\ui_lol\\Basic-window-Pyside-Pyqt5-main\\img\\duvida.png'))
        self.ask.setIconSize(QSize(20, 20))
        self.ask.setStyleSheet("border: none;")


        # Login 
        self.name_login = QLabel(self.frame_left)
        self.name_login.setGeometry(110, 160, 130, 40)
        self.name_login.setText("Fazer login")
        self.name_login.setStyleSheet(
            "QLabel {"
                "font: 700 20pt \"Tw Cen MT\";"
            "}"
        )

        # Username
        self.username = QLineEdit(self.frame_left)
        self.username.setGeometry(30, 220, 280, 55)
        self.username.setPlaceholderText("Nome de usuário")
        self.username.setStyleSheet(
            "QLineEdit {"
                "background-color: rgb(239, 239, 236);"
                "border-color: rgb(0, 0, 0);"
                "font: 700 10pt \"Segoe UI\";"
                "border-radius: 1px;"
                "color: rgb(157, 157, 157);"
            "}"
            "QLineEdit:hover {"
                "border: 2px solid rgb(0, 0, 0)"
            "}"
        )

        # Password
        self.password = QLineEdit(self.frame_left)
        self.password.setGeometry(30, 290, 280, 55)
        self.password.setPlaceholderText("Senha")
        self.password.setStyleSheet(
            "QLineEdit {"
                "background-color: rgb(239, 239, 236);"
                "border-color: rgb(0, 0, 0);"
                "font: 700 10pt \"Segoe UI\";"
                "border-radius: 1px;"
                "color: rgb(157, 157, 157);"
            "}"
            "QLineEdit:hover {"
                "border: 2px solid rgb(0, 0, 0)"
            "}"
        )


        # Facebook button 
        self.facebook = QPushButton(self.frame_left)
        self.facebook.setGeometry(30, 356, 87, 28)
        self.facebook.setCursor(Qt.PointingHandCursor)
        self.facebook.setIcon(QtGui.QPixmap('C:\\Users\\PC\\Desktop\\Gabriel\\ui_lol\\Basic-window-Pyside-Pyqt5-main\\img\\face.png'))
        self.facebook.setIconSize(QSize(40, 40))
        self.facebook.setStyleSheet(
            "QPushButton {"
                "background-color: rgb(0, 83, 249);"
                "border-radius: 4px;"
            "}"
            "QPushButton:hover {"
                "background-color: rgb(12, 90, 255);"
            "}"
        )

        # google button
        self.google = QPushButton(self.frame_left)
        self.google.setGeometry(125, 356, 87, 28)
        self.google.setCursor(Qt.PointingHandCursor)
        self.google.setIcon(QtGui.QPixmap('C:\\Users\\PC\\Desktop\\Gabriel\\ui_lol\\Basic-window-Pyside-Pyqt5-main\\img\\google.png'))
        self.google.setIconSize(QSize(22, 22))
        self.google.setStyleSheet(
            "QPushButton {"
                "background-color: rgb(250, 250, 250);"
                "border-radius: 4px;"
            "}"
            "QPushButton:hover {"
                "background-color: rgb(245, 245, 245);"
            "}"
        )

        # google button
        self.apple = QPushButton(self.frame_left)
        self.apple.setGeometry(223, 356, 87, 29)
        self.apple.setCursor(Qt.PointingHandCursor)
        self.apple.setIcon(QtGui.QPixmap('C:\\Users\\PC\\Desktop\\Gabriel\\ui_lol\\Basic-window-Pyside-Pyqt5-main\\img\\apple.png'))
        self.apple.setIconSize(QSize(17, 17))
        self.apple.setStyleSheet(
            "QPushButton {"
                "background-color: rgb(0, 0, 0);"
                "border-radius: 4px;"
            "}"
            "QPushButton:hover {"
                "background-color: rgb(12, 12, 12);"
            "}"
        )

        # checkbox
        self.checkbox = QCheckBox(self.frame_left)
        self.checkbox.setGeometry(30, 390, 91, 20)
        self.checkbox.setCursor(Qt.PointingHandCursor)
        self.checkbox.setText("Manter login")
        self.checkbox.setStyleSheet(
            "QCheckBox{"
            "	font: 700 9pt \"Segoe UI\";"
            "	color: rgb(150, 150, 150);"
            "}"
            "QCheckBox::indicator{"
            "	background-color: rgb(200, 200, 200);"
            "	border-radius: 10px;"
            "}"
            "QCheckBox::indicator:checked{"
            "	background-color: rgb(255, 39, 43);"
            "}"
            "QCheckBox:hover{"
            "	color: rgb(157, 157, 157);"
            "}"
        )

        # go button
        self.go_button = QPushButton(self.frame_left)
        self.go_button.setGeometry(140, 440, 60, 60)
        self.go_button.setCursor(Qt.PointingHandCursor)
        self.go_button.setText("→")
        self.go_button.setStyleSheet(
            "QPushButton {"
                "background-color: transparent;"
                "border: 2px solid rgb(230, 230, 230);"
                "font: 700 35pt \"Segoe UI\";"
                "border-radius: 12px;"
                "color: rgb(230, 230, 230);"
            "}"
            "QPushButton:hover{"
                "color: rgb(255, 255, 255);"
                "border: 2px solid rgb(201, 0, 54);"
                "background-color: rgb(201, 0, 54);"
            "}"
        )

        # can't go
        self.cant_log = QPushButton(self.frame_left)
        self.cant_log.setGeometry(80, 550, 170, 20)
        self.cant_log.setText("Não consegue iniciar sessão?")
        self.cant_log.setCursor(Qt.PointingHandCursor)
        self.cant_log.setStyleSheet(
            "QPushButton{"
                "color: rgb(157, 157, 157);"
                "font: 8pt \"Showcard Gothic\";"
                "border: none"
            "}"
            "QPushButton:hover{"
                "color: #000"
            "}"
        )

        # create account
        self.new_account = QPushButton(self.frame_left)
        self.new_account.setGeometry(80, 570, 170, 20)
        self.new_account.setText("Criar conta")
        self.new_account.setCursor(Qt.PointingHandCursor)
        self.new_account.setStyleSheet(
            "QPushButton{"
                "color: rgb(157, 157, 157);"
                "font: 8pt \"Showcard Gothic\";"
                "border: none"
            "}"
            "QPushButton:hover{"
                "color: #000"
            "}"
        )

        # version 
        self.version = QLabel(self.frame_left)
        self.version.setGeometry(270, 575, 70, 20)
        self.version.setText("Beta")
        self.version.setCursor(Qt.PointingHandCursor)
        self.version.setStyleSheet(
            "QLabel{"
                "color: rgb(180, 180, 180);"
                "font: 8pt \"Showcard Gothic\";"
                "border: none"
            "}"
            "QLabel:hover{"
                "color: rgb(140, 140, 140);"
            "}"
        )

        # IMAGE FRAME
        self.frame_image = QFrame(self.centralwidget)

        self.back_image = QLabel(self.frame_image)
        self.back_image.setGeometry(0, 0, 950, 620)
        self.back_image.setPixmap('C:\\Users\\PC\\Desktop\\Gabriel\\ui_lol\\Basic-window-Pyside-Pyqt5-main\\img\\22.png')

        # close button
        self.close_btn = QPushButton(self.frame_image)
        self.close_btn.setGeometry(920, 0, 30, 30)
        self.close_btn.setText("X")
        self.close_btn.setCursor(Qt.PointingHandCursor)
        self.close_btn.setStyleSheet(
            "background-color: transparent;"
            "font: 11pt \"Segoe UI\";"
        	"color: rgb(235, 235, 235);"
        )
        self.close_btn.clicked.connect(self.close)

        # ? button
        self.quest = QPushButton(self.frame_image)
        self.quest.setGeometry(890, 0, 30, 30)
        self.quest.setText("?")
        self.quest.setCursor(Qt.PointingHandCursor)
        self.quest.setStyleSheet(
            "background-color: transparent;"
            "font: 11pt \"Segoe UI\";"
        	"color: rgb(235, 235, 235);"
        )

        # minimize button
        self.minimize = QPushButton(self.frame_image)
        self.minimize.setGeometry(860, 0, 30, 30)
        self.minimize.setText("-")
        self.minimize.setCursor(Qt.PointingHandCursor)
        self.minimize.setStyleSheet(
            "background-color: transparent;"
            "font: 11pt \"Segoe UI\";"
        	"color: rgb(235, 235, 235);"
        )

        # adv button
        self.adv = QPushButton(self.frame_image)
        self.adv.setGeometry(15, 20, 80, 80)
        self.adv.setCursor(Qt.PointingHandCursor)
        self.adv.setIcon(QtGui.QPixmap('C:\\Users\\PC\\Desktop\\Gabriel\\ui_lol\\Basic-window-Pyside-Pyqt5-main\\img\\btnadv.png'))
        self.adv.setIconSize(QSize(60, 60))
        self.adv.setStyleSheet("Background-color: transparent; border: none;")

        # config button 
        self.config = QPushButton(self.frame_image)
        self.config.setGeometry(860, 540, 40, 40)
        self.config.setCursor(Qt.PointingHandCursor)
        self.config.setIcon(QtGui.QPixmap('C:\\Users\\PC\\Desktop\\Gabriel\\ui_lol\\Basic-window-Pyside-Pyqt5-main\\img\\config.png'))
        self.config.setIconSize(QSize(40, 40))
        self.config.setStyleSheet("Background-color: transparent; border: none;")
        
        
	#ADD TO LAYOUT
        self.horizontalLayout.addWidget(self.frame_left)
        self.horizontalLayout.addWidget(self.frame_image)
        MainWindow.setCentralWidget(self.centralwidget)


    def close(self):
        sys.exit()

