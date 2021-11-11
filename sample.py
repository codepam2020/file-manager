# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_xml.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from PyPDF2.pdf import *
import sys
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(498, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 440, 451, 31))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 451, 321))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(20, 30, 411, 192))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 240, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 280, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(180, 240, 93, 71))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(340, 240, 93, 71))
        self.pushButton_7.setObjectName("pushButton_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 350, 451, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_2.setGeometry(QtCore.QRect(20, 20, 321, 51))
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 30, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox.raise_()
        self.pushButton.raise_()
        self.groupBox_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_6.clicked.connect(self.add_PDF)
        self.pushButton_2.clicked.connect(self.set_PDF)
        self.pushButton_7.clicked.connect(self.del_PDF)
        self.pushButton_4.clicked.connect(self.up_PDF)
        self.pushButton_5.clicked.connect(self.down_PDF)
        self.pushButton.clicked.connect(self.merge_PDF)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HoguPDF"))
        self.pushButton.setText(_translate("MainWindow", "합치기"))
        self.groupBox.setTitle(_translate("MainWindow", ""))
        self.pushButton_4.setText(_translate("MainWindow", "위 이동"))
        self.pushButton_5.setText(_translate("MainWindow", "아래 이동"))
        self.pushButton_6.setText(_translate("MainWindow", "리스트 추가"))
        self.pushButton_7.setText(_translate("MainWindow", "리스트 제거"))
        self.groupBox_2.setTitle(_translate("MainWindow", "<저장 위치>"))
        self.pushButton_2.setText(_translate("MainWindow", "설정"))

    def add_PDF(self):
        fname = QFileDialog.getOpenFileName(None)
        self.listWidget.addItem(QListWidgetItem(fname[0]))

    def set_PDF(self):
        dirname = QFileDialog.getExistingDirectory(None)
        self.listWidget_2.clear()
        self.listWidget_2.addItem(QListWidgetItem(dirname))

    def del_PDF(self):
        self.listWidget.takeItem(self.listWidget.currentRow())

    def up_PDF(self):
        row = self.listWidget.currentRow()
        if row > 0:
            item = self.listWidget.takeItem(row)
            self.listWidget.insertItem(row - 1, item)
            self.listWidget.setCurrentRow(row - 1)

    def down_PDF(self):
        row = self.listWidget.currentRow()
        if row < self.listWidget.count() - 1:
            item = self.listWidget.takeItem(row)
            self.listWidget.insertItem(row + 1, item)
            self.listWidget.setCurrentRow(row + 1)

    def merge_PDF(self):

        count = self.listWidget.count()
        print(count)
        output = PdfFileWriter()

        for x in range(0, count):
            src = self.listWidget.item(x)
            print(src.text())
            input = PdfFileReader(open(src.text(), "rb"))
            for j in range(input.getNumPages()):
                output.addPage(input.getPage(j))

        dest = (self.listWidget_2.item(0)).text() + "\\Merged.pdf"
        print(dest)
        outstream = open(dest, "wb")
        output.write(outstream)
        outstream.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
