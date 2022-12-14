# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Battleship-Copy2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    """
    An object class representing the main graphical window for a 'Ui_MainWindow' object.
    """
    def setupUi(self, MainWindow) -> None:
        """
        Function to set up the positions and attributes of objects to display within the user interface.
        :param MainWindow: The graphical window type the Ui_MainWindow object will display as a QtWidgets.QMainWindow() function.
        :return: None
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 700)
        MainWindow.setMinimumSize(QtCore.QSize(750, 700))
        MainWindow.setMaximumSize(QtCore.QSize(750, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_fire = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_fire.setGeometry(QtCore.QRect(300, 490, 161, 41))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(20)
        self.pushButton_fire.setFont(font)
        self.pushButton_fire.setObjectName("pushButton_fire")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(280, -10, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_player = QtWidgets.QLabel(self.centralwidget)
        self.label_player.setGeometry(QtCore.QRect(140, 80, 55, 21))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(10)
        self.label_player.setFont(font)
        self.label_player.setObjectName("label_player")
        self.label_computer = QtWidgets.QLabel(self.centralwidget)
        self.label_computer.setGeometry(QtCore.QRect(550, 80, 55, 21))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(10)
        self.label_computer.setFont(font)
        self.label_computer.setObjectName("label_computer")
        self.label_playerboard = QtWidgets.QLabel(self.centralwidget)
        self.label_playerboard.setGeometry(QtCore.QRect(30, 110, 281, 241))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.label_playerboard.setFont(font)
        self.label_playerboard.setLineWidth(1)
        self.label_playerboard.setTextFormat(QtCore.Qt.AutoText)
        self.label_playerboard.setScaledContents(False)
        self.label_playerboard.setIndent(0)
        self.label_playerboard.setObjectName("label_playerboard")
        self.label_computerboard = QtWidgets.QLabel(self.centralwidget)
        self.label_computerboard.setGeometry(QtCore.QRect(440, 110, 281, 241))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.label_computerboard.setFont(font)
        self.label_computerboard.setLineWidth(1)
        self.label_computerboard.setTextFormat(QtCore.Qt.AutoText)
        self.label_computerboard.setScaledContents(False)
        self.label_computerboard.setIndent(0)
        self.label_computerboard.setObjectName("label_computerboard")
        self.lineEdit_input = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_input.setGeometry(QtCore.QRect(310, 450, 141, 22))
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.label_key = QtWidgets.QLabel(self.centralwidget)
        self.label_key.setGeometry(QtCore.QRect(230, 50, 311, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.label_key.setFont(font)
        self.label_key.setObjectName("label_key")
        self.label_prompt = QtWidgets.QLabel(self.centralwidget)
        self.label_prompt.setGeometry(QtCore.QRect(280, 370, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setBold(False)
        font.setWeight(50)
        self.label_prompt.setFont(font)
        self.label_prompt.setObjectName("label_prompt")
        self.label_rules = QtWidgets.QLabel(self.centralwidget)
        self.label_rules.setGeometry(QtCore.QRect(200, 540, 361, 111))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(6)
        self.label_rules.setFont(font)
        self.label_rules.setScaledContents(False)
        self.label_rules.setIndent(-1)
        self.label_rules.setObjectName("label_rules")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 751, 651))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("beach.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.pushButton_fire.raise_()
        self.label_title.raise_()
        self.label_player.raise_()
        self.label_computer.raise_()
        self.label_playerboard.raise_()
        self.label_computerboard.raise_()
        self.lineEdit_input.raise_()
        self.label_key.raise_()
        self.label_prompt.raise_()
        self.label_rules.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow) -> None:
        """
        Function to set and specify the text the different objects will display on the graphical user interface.
        :param MainWindow: The graphical window type the Ui_MainWindow object will display as a QtWidgets.QMainWindow() function.
        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Battleship"))
        self.pushButton_fire.setText(_translate("MainWindow", "Fire"))
        self.label_title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">BATTLESHIP</p></body></html>"))
        self.label_player.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">You</p></body></html>"))
        self.label_computer.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">CPU</p></body></html>"))
        self.label_playerboard.setText(_translate("MainWindow", "   1  2  3  4  5  6  7  8  9 10\n"
"A ?????? ?????? ?????? ?????? ?????? ?????? ?????? ?????? ?????? ??????\n"
"B ?????? ?????? ?????? ?????? ?????? ?????? ?????? ?????? ?????? ??????\n"
"C ?????? ?????? ?????? ?????? ?????? ?????? ?????? ?????? ?????? ??????\n"
"D ?????? ?????? ?????? ?????? ?????? ?????? ?????? ?????? ?????? ??????\n"
"E ?????? ?????? ?????? ?????? ?????? ?????? ?????? ?????? ?????? ??????\n"
"F ?????? ?????? ?????? ?????? ?????? ?????? ?????? ?????? ?????? ??????\n"
"G ?????? ?????? ?????? ?????? ?????? ?????? ?????? ?????? ?????? ??????\n"
"H ?????? ?????? ?????? ?????? ?????? ?????? ?????? ?????? ?????? ??????\n"
"I ?????? ?????? ?????? ?????? ?????? ?????? ?????? ?????? ?????? ??????\n"
"J ?????? ?????? ?????? ?????? ?????? ?????? ?????? ** ~~ ??????"))
        self.label_computerboard.setText(_translate("MainWindow", "   1  2  3  4  5  6  7  8  9 10\n"
"A ?? ?? ?? ?? ?? ?? ?? ?? ?? ??\n"
"B ?? ?? ?? ?? ?? ?? ?? ?? ?? ??\n"
"C ?? ?? ?? ?? ?? ?? ?? ?? ?? ??\n"
"D ?? ?? ?? ?? ?? ?? ?? ?? ?? ??\n"
"E ?? ?? ?? ?? ?? ?? ?? ?? ?? ??\n"
"F ?? ?? ?? ?? ?? ?? ?? ?? ?? ??\n"
"G ?? ?? ?? ?? ?? ?? ?? ?? ?? ??\n"
"H ?? ?? ?? ?? ?? ?? ?? ?? ?? ??\n"
"I ?? ?? ?? ?? ?? ?? ?? ?? ?? ??\n"
"J ?? ?? ?? ?? ?? ?? ?? ?? ** ??????"))
        self.label_key.setText(_translate("MainWindow", "\"??????\" = Sea  \"~~\" = Ship  \"**\" = Miss  \"??????\" = Hit"))
        self.label_prompt.setText(_translate("MainWindow", "Enter Coordinates Here (Ex: \"a1\")"))
        self.label_rules.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Rules:</p><p align=\"center\">You and your opponent will take turns firing at a specified coordinate (Ex: &quot;a1&quot;).</p><p align=\"center\">Try to sink all of your opponents ships by landing a hit on their coordinates.</p><p align=\"center\">If you manage to sink all of your opponent\'s ships, you win.</p><p align=\"center\">If all of your ships sink, you lose.</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
