# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\111.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(711, 575)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chocoButton = QtWidgets.QPushButton(self.centralwidget)
        self.chocoButton.setEnabled(True)
        self.chocoButton.setGeometry(QtCore.QRect(190, 100, 111, 61))
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.chocoButton.setFont(font)
        self.chocoButton.setMouseTracking(False)
        self.chocoButton.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.chocoButton.setObjectName("chocoButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 30, 288, 55))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.chocoButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.chocoButton_2.setEnabled(True)
        self.chocoButton_2.setGeometry(QtCore.QRect(190, 190, 111, 61))
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.chocoButton_2.setFont(font)
        self.chocoButton_2.setMouseTracking(False)
        self.chocoButton_2.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.chocoButton_2.setObjectName("chocoButton_2")
        self.chocoButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.chocoButton_3.setEnabled(True)
        self.chocoButton_3.setGeometry(QtCore.QRect(190, 370, 111, 61))
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.chocoButton_3.setFont(font)
        self.chocoButton_3.setMouseTracking(False)
        self.chocoButton_3.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.chocoButton_3.setObjectName("chocoButton_3")
        self.chocoButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.chocoButton_4.setEnabled(True)
        self.chocoButton_4.setGeometry(QtCore.QRect(190, 280, 111, 61))
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.chocoButton_4.setFont(font)
        self.chocoButton_4.setMouseTracking(False)
        self.chocoButton_4.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.chocoButton_4.setObjectName("chocoButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 711, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.chocoButton.clicked.connect(MainWindow.start)
        self.chocoButton_2.clicked.connect(MainWindow.start)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.chocoButton, self.chocoButton_2)
        MainWindow.setTabOrder(self.chocoButton_2, self.chocoButton_4)
        MainWindow.setTabOrder(self.chocoButton_4, self.chocoButton_3)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chocoButton.setText(_translate("MainWindow", "초코"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#0d76e6;\">File Manager</span></p></body></html>"))
        self.chocoButton_2.setText(_translate("MainWindow", "초코"))
        self.chocoButton_3.setText(_translate("MainWindow", "초코"))
        self.chocoButton_4.setText(_translate("MainWindow", "초코"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())