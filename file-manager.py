# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file-manager.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyPDF2.pdf import *
import pikepdf
import sys
import os
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(626, 390)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 611, 361))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.comboBox = QtWidgets.QComboBox(self.tab_1)
        self.comboBox.setGeometry(QtCore.QRect(140, 20, 121, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textEdit = QtWidgets.QTextEdit(self.tab_1)
        self.textEdit.setGeometry(QtCore.QRect(140, 70, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.tab_1)
        self.label.setGeometry(QtCore.QRect(30, 20, 91, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 91, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_1)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 91, 31))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_1)
        self.textEdit_2.setGeometry(QtCore.QRect(140, 120, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_1)
        self.textEdit_3.setGeometry(QtCore.QRect(420, 120, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_4 = QtWidgets.QLabel(self.tab_1)
        self.label_4.setGeometry(QtCore.QRect(320, 120, 91, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_1)
        self.label_5.setGeometry(QtCore.QRect(30, 170, 61, 31))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.tab_1)
        self.pushButton.setGeometry(QtCore.QRect(460, 170, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 260, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(self.tab_1)
        self.label_6.setGeometry(QtCore.QRect(520, 310, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_1)
        self.label_7.setGeometry(QtCore.QRect(320, 20, 91, 31))
        self.label_7.setObjectName("label_7")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_1)
        self.comboBox_2.setGeometry(QtCore.QRect(420, 20, 121, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.listWidget = QtWidgets.QListWidget(self.tab_1)
        self.listWidget.setGeometry(QtCore.QRect(140, 170, 301, 41))
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(520, 310, 71, 16))
        self.label_8.setObjectName("label_8")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_2.setGeometry(QtCore.QRect(20, 10, 291, 311))
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 120, 71, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(480, 120, 71, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(360, 30, 211, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(360, 70, 211, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.listWidget_3 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_3.setGeometry(QtCore.QRect(360, 210, 211, 41))
        self.listWidget_3.setObjectName("listWidget_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(360, 170, 211, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(420, 260, 91, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(520, 310, 71, 16))
        self.label_14.setObjectName("label_14")
        self.listWidget_5 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_5.setGeometry(QtCore.QRect(20, 10, 291, 311))
        self.listWidget_5.setObjectName("listWidget_5")
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(360, 20, 211, 31))
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_3.setGeometry(QtCore.QRect(360, 60, 211, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_9.setGeometry(QtCore.QRect(360, 120, 211, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_10.setGeometry(QtCore.QRect(360, 180, 211, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_11.setGeometry(QtCore.QRect(420, 260, 91, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(520, 310, 71, 16))
        self.label_15.setObjectName("label_15")
        self.listWidget_4 = QtWidgets.QListWidget(self.tab_4)
        self.listWidget_4.setGeometry(QtCore.QRect(20, 10, 291, 311))
        self.listWidget_4.setObjectName("listWidget_4")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_13.setGeometry(QtCore.QRect(360, 180, 211, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_17 = QtWidgets.QLabel(self.tab_4)
        self.label_17.setGeometry(QtCore.QRect(390, 30, 181, 20))
        self.label_17.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.label_17.setObjectName("label_17")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_12.setGeometry(QtCore.QRect(360, 120, 211, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_18 = QtWidgets.QLabel(self.tab_4)
        self.label_18.setGeometry(QtCore.QRect(390, 50, 171, 20))
        self.label_18.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab_4)
        self.label_19.setGeometry(QtCore.QRect(390, 70, 171, 20))
        self.label_19.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.label_19.setObjectName("label_19")
        self.checkBox = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox.setGeometry(QtCore.QRect(360, 40, 16, 16))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_14.setGeometry(QtCore.QRect(420, 260, 91, 31))
        self.pushButton_14.setObjectName("pushButton_14")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(30, 30, 161, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(30, 110, 231, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(30, 150, 371, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(140, 240, 301, 31))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(30, 70, 221, 16))
        self.label_13.setObjectName("label_13")
        self.label_20 = QtWidgets.QLabel(self.tab)
        self.label_20.setGeometry(QtCore.QRect(30, 180, 251, 31))
        self.label_20.setObjectName("label_20")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #! 버튼클릭과 관련 함수들 연결

        # 파일 이름 바꾸기 관련 functions
        self.pushButton.clicked.connect(self.set_folder)
        self.pushButton_2.clicked.connect(self.name_change)

        # pdf 병합 관련 functions
        self.pushButton_5.clicked.connect(self.up_PDF)
        self.pushButton_6.clicked.connect(self.down_PDF)
        self.pushButton_3.clicked.connect(self.add_PDF)
        self.pushButton_4.clicked.connect(self.del_PDF)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "File Manager"))
        self.comboBox.setItemText(0, _translate("MainWindow", "YYYYMMDDHHmm"))
        self.comboBox.setItemText(1, _translate("MainWindow", "YYYYMMDDHH"))
        self.comboBox.setItemText(2, _translate("MainWindow", "YYYYMMDD"))
        self.comboBox.setItemText(3, _translate("MainWindow", "YYMMDDHHmm"))
        self.comboBox.setItemText(4, _translate("MainWindow", "YYMMDDHH"))
        self.comboBox.setItemText(5, _translate("MainWindow", "YYMMDD"))
        self.label.setText(_translate("MainWindow", "날짜 형식"))
        self.label_2.setText(_translate("MainWindow", "날짜 사이 단어"))
        self.label_3.setText(_translate("MainWindow", "접두사"))
        self.label_4.setText(_translate("MainWindow", "접미사"))
        self.label_5.setText(_translate("MainWindow", "폴더 경로"))
        self.pushButton.setText(_translate("MainWindow", "경로 설정"))
        self.pushButton_2.setText(_translate("MainWindow", "실행하기"))
        self.label_6.setText(_translate("MainWindow", "by codePam"))
        self.label_7.setText(_translate("MainWindow", "날짜 타입"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "수정된 날짜"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "생성된 날짜"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "파일 이름 관리")
        )
        self.label_8.setText(_translate("MainWindow", "by codePam"))
        self.pushButton_3.setText(_translate("MainWindow", "파일 추가"))
        self.pushButton_4.setText(_translate("MainWindow", "파일 제거"))
        self.pushButton_5.setText(_translate("MainWindow", "위로 이동"))
        self.pushButton_6.setText(_translate("MainWindow", "아래로 이동"))
        self.pushButton_7.setText(_translate("MainWindow", "저장 위치 설정"))
        self.pushButton_8.setText(_translate("MainWindow", "병합"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "PDF 병합")
        )
        self.label_14.setText(_translate("MainWindow", "by codePam"))
        self.label_16.setText(_translate("MainWindow", "파일 형식"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "PowerPoint"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Word"))
        self.pushButton_9.setText(_translate("MainWindow", "파일 추가"))
        self.pushButton_10.setText(_translate("MainWindow", "파일 제거"))
        self.pushButton_11.setText(_translate("MainWindow", "전환"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "PDF로 전환")
        )
        self.label_15.setText(_translate("MainWindow", "by codePam"))
        self.pushButton_13.setText(_translate("MainWindow", "파일 제거"))
        self.label_17.setText(_translate("MainWindow", "본 pdf 파일(들)에 대해 잠금 해제"))
        self.pushButton_12.setText(_translate("MainWindow", "파일 추가"))
        self.label_18.setText(_translate("MainWindow", "및 편집을 할 수 있는 권한을"))
        self.label_19.setText(_translate("MainWindow", "갖고있습니다."))
        self.pushButton_14.setText(_translate("MainWindow", "잠금 해제"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "PDF 잠금해제")
        )
        self.label_9.setText(_translate("MainWindow", "제작자      codePam"))
        self.label_10.setText(
            _translate("MainWindow", "이메일      codepam2020@gmail.com")
        )
        self.label_11.setText(_translate("MainWindow", "문의사항이나 개선사항이 있으면 위 메일로 연락주세요"))
        self.label_12.setText(_translate("MainWindow", "@@@우석 컴퓨팅사고 창작대회 제출용@@@"))
        self.label_13.setText(
            _translate("MainWindow", "GitHub      github.com/codepam2020")
        )
        self.label_20.setText(_translate("MainWindow", "위 깃허브 주소에 코드를 공개해두었습니다"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab), _translate("MainWindow", "정보")
        )

    #! Button Click Funtions

    # 이름 바꾸는 폴더 설정
    def set_folder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory()
        self.listWidget.clear()
        self.listWidget.addItem(QtWidgets.QListWidgetItem(folder))

    # 파일 이름 바꾸기 함수
    def name_change(self):
        try:
            folder = self.listWidget.item(0).text()
            file_list = os.listdir(folder)
            date_date_word = self.textEdit.toPlainText()
            head_word = self.textEdit_2.toPlainText()
            tail_word = self.textEdit_3.toPlainText()
            date_style = self.comboBox.currentText()
            date_type = self.comboBox_2.currentText()

            # 수정된 날짜
            if date_type == "수정된 날짜":
                if date_style == "YYYYMMDDHHmm":
                    count = 1
                    for i in file_list:
                        idx = i.rfind(".")
                        if idx != -1:
                            m_time = os.path.getmtime(folder + "/" + i)
                            time_str = time.strftime(
                                f"%Y{date_date_word}%m{date_date_word}%d{date_date_word}%H{date_date_word}%M",
                                time.localtime(m_time),
                            )
                            try:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + i[idx:],
                                )
                            except:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + "("
                                    + str(count)
                                    + ")"
                                    + i[idx:],
                                )
                                count = count + 1
                        else:
                            pass
                elif date_style == "YYYYMMDDHH":
                    count = 1
                    for i in file_list:
                        idx = i.rfind(".")
                        if idx != -1:
                            m_time = os.path.getmtime(folder + "/" + i)
                            time_str = time.strftime(
                                f"%Y{date_date_word}%m{date_date_word}%d{date_date_word}%H",
                                time.localtime(m_time),
                            )
                            try:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + i[idx:],
                                )
                            except:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + "("
                                    + str(count)
                                    + ")"
                                    + i[idx:],
                                )
                                count = count + 1
                        else:
                            pass

                elif date_style == "YYYYMMDD":
                    count = 1
                    for i in file_list:
                        idx = i.rfind(".")
                        if idx != -1:
                            m_time = os.path.getmtime(folder + "/" + i)
                            time_str = time.strftime(
                                f"%Y{date_date_word}%m{date_date_word}%d",
                                time.localtime(m_time),
                            )
                            try:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + i[idx:],
                                )
                            except:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + "("
                                    + str(count)
                                    + ")"
                                    + i[idx:],
                                )
                                count = count + 1
                        else:
                            pass

                elif date_style == "YYMMDDHHmm":
                    count = 1
                    for i in file_list:
                        idx = i.rfind(".")
                        if idx != -1:
                            m_time = os.path.getmtime(folder + "/" + i)
                            time_str = time.strftime(
                                f"%y{date_date_word}%m{date_date_word}%d{date_date_word}%H{date_date_word}%M",
                                time.localtime(m_time),
                            )
                            try:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + i[idx:],
                                )
                            except:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + "("
                                    + str(count)
                                    + ")"
                                    + i[idx:],
                                )
                                count = count + 1
                        else:
                            pass

                elif date_style == "YYMMDDHH":
                    count = 1
                    for i in file_list:
                        idx = i.rfind(".")
                        if idx != -1:
                            m_time = os.path.getmtime(folder + "/" + i)
                            time_str = time.strftime(
                                f"%y{date_date_word}%m{date_date_word}%d{date_date_word}%H",
                                time.localtime(m_time),
                            )
                            try:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + i[idx:],
                                )
                            except:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + "("
                                    + str(count)
                                    + ")"
                                    + i[idx:],
                                )
                                count = count + 1
                        else:
                            pass

                elif date_style == "YYMMDD":
                    count = 1
                    for i in file_list:
                        idx = i.rfind(".")
                        if idx != -1:
                            m_time = os.path.getmtime(folder + "/" + i)
                            time_str = time.strftime(
                                f"%y{date_date_word}%m{date_date_word}%d",
                                time.localtime(m_time),
                            )
                            try:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + i[idx:],
                                )
                            except:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + "("
                                    + str(count)
                                    + ")"
                                    + i[idx:],
                                )
                                count = count + 1
                        else:
                            pass

                # 생성된 날짜
            else:
                if date_style == "YYYYMMDDHHmm":
                    count = 1
                    for i in file_list:
                        idx = i.rfind(".")
                        if idx != -1:
                            c_time = os.path.getctime(folder + "/" + i)
                            time_str = time.strftime(
                                f"%Y{date_date_word}%m{date_date_word}%d{date_date_word}%H{date_date_word}%M",
                                time.localtime(c_time),
                            )
                            try:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + i[idx:],
                                )
                            except:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + "("
                                    + str(count)
                                    + ")"
                                    + i[idx:],
                                )
                                count = count + 1
                        else:
                            pass
                elif date_style == "YYYYMMDDHH":
                    count = 1
                    for i in file_list:
                        idx = i.rfind(".")
                        if idx != -1:
                            c_time = os.path.getctime(folder + "/" + i)
                            time_str = time.strftime(
                                f"%Y{date_date_word}%m{date_date_word}%d{date_date_word}%H",
                                time.localtime(c_time),
                            )
                            try:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + i[idx:],
                                )
                            except:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + "("
                                    + str(count)
                                    + ")"
                                    + i[idx:],
                                )
                                count = count + 1
                        else:
                            pass

                elif date_style == "YYYYMMDD":
                    count = 1
                    for i in file_list:
                        idx = i.rfind(".")
                        if idx != -1:
                            c_time = os.path.getctime(folder + "/" + i)
                            time_str = time.strftime(
                                f"%Y{date_date_word}%m{date_date_word}%d",
                                time.localtime(c_time),
                            )
                            try:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + i[idx:],
                                )
                            except:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + "("
                                    + str(count)
                                    + ")"
                                    + i[idx:],
                                )
                                count = count + 1
                        else:
                            pass

                elif date_style == "YYMMDDHHmm":
                    count = 1
                    for i in file_list:
                        idx = i.rfind(".")
                        if idx != -1:
                            c_time = os.path.getctime(folder + "/" + i)
                            time_str = time.strftime(
                                f"%y{date_date_word}%m{date_date_word}%d{date_date_word}%H{date_date_word}%M",
                                time.localtime(c_time),
                            )
                            try:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + i[idx:],
                                )
                            except:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + "("
                                    + str(count)
                                    + ")"
                                    + i[idx:],
                                )
                                count = count + 1
                        else:
                            pass

                elif date_style == "YYMMDDHH":
                    count = 1
                    for i in file_list:
                        idx = i.rfind(".")
                        if idx != -1:
                            c_time = os.path.getctime(folder + "/" + i)
                            time_str = time.strftime(
                                f"%y{date_date_word}%m{date_date_word}%d{date_date_word}%H",
                                time.localtime(c_time),
                            )
                            try:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + i[idx:],
                                )
                            except:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + "("
                                    + str(count)
                                    + ")"
                                    + i[idx:],
                                )
                                count = count + 1
                        else:
                            pass

                elif date_style == "YYMMDD":
                    count = 1
                    for i in file_list:
                        idx = i.rfind(".")
                        if idx != -1:
                            c_time = os.path.getctime(folder + "/" + i)
                            time_str = time.strftime(
                                f"%y{date_date_word}%m{date_date_word}%d",
                                time.localtime(c_time),
                            )
                            try:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + i[idx:],
                                )
                            except:
                                os.rename(
                                    folder + "/" + i,
                                    folder
                                    + "/"
                                    + head_word
                                    + time_str
                                    + tail_word
                                    + "("
                                    + str(count)
                                    + ")"
                                    + i[idx:],
                                )
                                count = count + 1
                        else:
                            pass

            # for i in file_list:
            #     m_time = os.path.getmtime(folder + "/" + i)
            #     print(time.strftime("20%y_%m_%d", time.localtime(m_time)))
        except:
            print("error")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

