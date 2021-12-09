from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyPDF2.pdf import *
from docx2pdf import convert
import comtypes.client
import sys
import sys
import os
import time


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 390)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 611, 361))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.comboBox = QtWidgets.QComboBox(self.tab_1)
        self.comboBox.setGeometry(QtCore.QRect(140, 30, 81, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textEdit = QtWidgets.QTextEdit(self.tab_1)
        self.textEdit.setGeometry(QtCore.QRect(140, 80, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.tab_1)
        self.label.setGeometry(QtCore.QRect(30, 30, 91, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 91, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_1)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 91, 31))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_1)
        self.textEdit_2.setGeometry(QtCore.QRect(140, 130, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_1)
        self.textEdit_3.setGeometry(QtCore.QRect(430, 130, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_4 = QtWidgets.QLabel(self.tab_1)
        self.label_4.setGeometry(QtCore.QRect(320, 130, 91, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_1)
        self.label_5.setGeometry(QtCore.QRect(30, 180, 61, 31))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.tab_1)
        self.pushButton.setGeometry(QtCore.QRect(460, 180, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 260, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(self.tab_1)
        self.label_6.setGeometry(QtCore.QRect(520, 310, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_21 = QtWidgets.QLabel(self.tab_1)
        self.label_21.setGeometry(QtCore.QRect(30, 310, 301, 16))
        self.label_21.setObjectName("label_21")
        self.label_7 = QtWidgets.QLabel(self.tab_1)
        self.label_7.setGeometry(QtCore.QRect(320, 80, 91, 31))
        self.label_7.setObjectName("label_7")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_1)
        self.comboBox_2.setGeometry(QtCore.QRect(430, 80, 121, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.listWidget = QtWidgets.QListWidget(self.tab_1)
        self.listWidget.setGeometry(QtCore.QRect(140, 180, 301, 41))
        self.listWidget.setObjectName("listWidget")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_1)
        self.comboBox_4.setGeometry(QtCore.QRect(250, 30, 81, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_1)
        self.comboBox_5.setGeometry(QtCore.QRect(360, 30, 81, 31))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_6 = QtWidgets.QComboBox(self.tab_1)
        self.comboBox_6.setGeometry(QtCore.QRect(470, 30, 81, 31))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
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

        #! Click events

        # file name change
        self.pushButton.clicked.connect(self.set_folder)
        self.pushButton_2.clicked.connect(self.name_change)

        # pdf concat
        self.pushButton_5.clicked.connect(self.move_up)
        self.pushButton_6.clicked.connect(self.move_down)
        self.pushButton_3.clicked.connect(self.file_add_concat)
        self.pushButton_4.clicked.connect(self.file_del_concat)
        self.pushButton_7.clicked.connect(self.file_save)
        self.pushButton_8.clicked.connect(self.file_merge)

        # pdf convert
        self.pushButton_9.clicked.connect(self.file_add_convert)
        self.pushButton_10.clicked.connect(self.file_del_convert)
        self.pushButton_11.clicked.connect(self.file_convert)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "file manager"))
        self.comboBox.setItemText(0, _translate("MainWindow", "연도선택X"))
        self.comboBox.setItemText(1, _translate("MainWindow", "YYYY"))
        self.comboBox.setItemText(2, _translate("MainWindow", "YY"))
        self.comboBox.setItemText(3, _translate("MainWindow", "YYYY년"))
        self.comboBox.setItemText(4, _translate("MainWindow", "YY년"))
        self.label.setText(_translate("MainWindow", "날짜 형식"))
        self.label_2.setText(_translate("MainWindow", "날짜 사이 단어"))
        self.label_3.setText(_translate("MainWindow", "접두사"))
        self.label_4.setText(_translate("MainWindow", "접미사"))
        self.label_5.setText(_translate("MainWindow", "폴더 경로"))
        self.label_21.setText(
            _translate("MainWindow", "*시간 선택시 ()표시에는 날짜 사이 단어가 표기됩니다")
        )
        self.pushButton.setText(_translate("MainWindow", "경로 설정"))
        self.pushButton_2.setText(_translate("MainWindow", "실행하기"))
        self.label_6.setText(_translate("MainWindow", "by codePam"))
        self.label_7.setText(_translate("MainWindow", "날짜 타입"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "날짜로 변경X"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "생성된 날짜"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "수정된 날짜"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "월선택X"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "MM"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "MM월"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "일선택X"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "DD"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "DD일"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "시간선택X"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "HH"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "HHmm"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "HH:mm"))
        self.comboBox_6.setItemText(4, _translate("MainWindow", "HH()mm"))
        self.comboBox_6.setItemText(5, _translate("MainWindow", "HH시"))
        self.comboBox_6.setItemText(6, _translate("MainWindow", "HH시mm분"))
        self.comboBox_6.setItemText(7, _translate("MainWindow", "HH시()mm분"))
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
        self.pushButton_11.setText(_translate("MainWindow", "변환"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "PDF로 변환")
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

    #! change file name functions
    # set folder for changing name
    def set_folder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory()
        self.listWidget.clear()
        self.listWidget.addItem(QtWidgets.QListWidgetItem(folder))

    # change file name function
    def name_change(self):
        try:
            folder = self.listWidget.item(0).text()
            file_list = os.listdir(folder)
            date_date_word = self.textEdit.toPlainText()
            head_word = self.textEdit_2.toPlainText()
            tail_word = self.textEdit_3.toPlainText()
            date_type_selected = self.comboBox_2.currentText()
            year_selected = self.comboBox.currentText()
            month_selected = self.comboBox_4.currentText()
            day_selected = self.comboBox_5.currentText()
            hour_selected = self.comboBox_6.currentText()

            for i in file_list:
                idx = i.rfind(".")
                if idx != -1:
                    if date_type_selected == "날짜로 변경X":
                        os.rename(
                            folder + "/" + i,
                            folder + "/" + head_word + i[:idx] + tail_word + i[idx:],
                        )
                    else:
                        # 날짜 타입 선택
                        if date_type_selected == "생성된 날짜":
                            date = os.path.getctime(folder + "/" + i)
                        else:
                            date = os.path.getmtime(folder + "/" + i)

                        # 연도 선택
                        if year_selected == "연도선택X":
                            year = ""
                        elif year_selected == "YYYY":
                            year = time.strftime("%Y", time.localtime(date))
                        elif year_selected == "YY":
                            year = time.strftime("%y", time.localtime(date))
                        elif year_selected == "YYYY년":
                            year = time.strftime("%Y년", time.localtime(date))
                        elif year_selected == "YY년":
                            year = time.strftime("%y년", time.localtime(date))

                        # 월 선택
                        if month_selected == "월선택X":
                            month = ""
                        elif month_selected == "MM":
                            month = time.strftime("%m", time.localtime(date))
                        elif month_selected == "MM월":
                            month = time.strftime("%m월", time.localtime(date))

                        # 일 선택
                        if day_selected == "일선택X":
                            day = ""
                        elif day_selected == "DD":
                            day = time.strftime("%d", time.localtime(date))
                        elif day_selected == "DD일":
                            day = time.strftime("%d일", time.localtime(date))

                        # 시간 선택
                        if hour_selected == "시간선택X":
                            hour = ""
                        elif hour_selected == "HH":
                            hour = time.strftime("%H", time.localtime(date))
                        elif hour_selected == "HHmm":
                            hour = time.strftime("%H%M", time.localtime(date))
                        elif hour_selected == "HH:mm":
                            hour = time.strftime("%H:%M", time.localtime(date))
                        elif hour_selected == "HH()mm":
                            hour = time.strftime(
                                "%H{}%M".format(date_date_word), time.localtime(date)
                            )
                        elif hour_selected == "HH시":
                            hour = time.strftime("%H시", time.localtime(date))
                        elif hour_selected == "HH시mm분":
                            hour = time.strftime("%H시%M분", time.localtime(date))
                        elif hour_selected == "HH시()mm분":
                            hour = time.strftime(
                                "%H시{}%M분".format(date_date_word), time.localtime(date)
                            )

                        # 날짜 사이 단어
                        if year and (month or day or hour):
                            word1 = date_date_word
                        else:
                            word1 = ""

                        if month and (day or hour):
                            word2 = date_date_word
                        else:
                            word2 = ""

                        if day and hour:
                            word3 = date_date_word
                        else:
                            word3 = ""

                        result = year + word1 + month + word2 + day + word3 + hour

                        try:
                            os.rename(
                                folder + "/" + i,
                                folder + "/" + head_word + result + tail_word + i[idx:],
                            )
                        except:
                            for count in range(len(folder)):
                                try:
                                    os.rename(
                                        folder + "/" + i,
                                        folder
                                        + "/"
                                        + head_word
                                        + result
                                        + tail_word
                                        + "("
                                        + str(count + 1)
                                        + ")"
                                        + i[idx:],
                                    )
                                except:
                                    pass

                        print(result)

            QMessageBox.about(self, "알림", "실행완료!")

        except:
            date_date_word = self.textEdit.toPlainText()
            head_word = self.textEdit_2.toPlainText()
            tail_word = self.textEdit_3.toPlainText()
            date_type_selected = self.comboBox_2.currentText()
            year_selected = self.comboBox.currentText()
            month_selected = self.comboBox_4.currentText()
            day_selected = self.comboBox_5.currentText()
            hour_selected = self.comboBox_6.currentText()

            QMessageBox.about(self, "에러발생!  ", "폴더 경로를 선택해주세요!")

    #! pdf concat functions
    # pdf concat move up
    def move_up(self):
        file_row = self.listWidget_2.currentRow()
        if file_row > 0:
            item = self.listWidget_2.takeItem(file_row)
            self.listWidget_2.insertItem(file_row - 1, item)
            self.listWidget_2.setCurrentRow(file_row - 1)

    # # pdf concat move down
    def move_down(self):
        file_row = self.listWidget_2.currentRow()
        if file_row < self.listWidget_2.count() - 1:
            item = self.listWidget_2.takeItem(file_row)
            self.listWidget_2.insertItem(file_row + 1, item)
            self.listWidget_2.setCurrentRow(file_row + 1)

    # pdf concat file add
    def file_add_concat(self):
        file_name = QFileDialog.getOpenFileNames(
            None, "PDF 파일 불러오기", "", "pdf 파일 (*.pdf)"
        )
        count = len(file_name[0])

        for i in range(count):
            self.listWidget_2.addItem(QListWidgetItem(file_name[0][i]))

    # pdf concat file delete
    def file_del_concat(self):
        self.listWidget_2.takeItem(self.listWidget_2.currentRow())

    # pdf concat set save file location
    def file_save(self):
        location = QFileDialog.getExistingDirectory(None)
        self.listWidget_3.clear()
        self.listWidget_3.addItem(QListWidgetItem(location))

    # pdf concat file merge
    def file_merge(self):

        try:
            num = self.listWidget_2.count()
            output = PdfFileWriter()
            folder = self.listWidget_3.item(0).text()
            file_list = os.listdir(folder)
            for x in range(0, num):
                src = self.listWidget_2.item(x)
                input = PdfFileReader(open(src.text(), "rb"))
                for j in range(input.getNumPages()):
                    output.addPage(input.getPage(j))

            for num in range(len(file_list)):
                if len(list(filter(lambda l: "Merged.pdf" in l, file_list))) == 0:
                    result = folder + "/" + "Merged.pdf"
                else:
                    if (
                        len(
                            list(
                                filter(
                                    lambda l: "Merged({}).pdf".format(str(num + 1))
                                    in l,
                                    file_list,
                                )
                            )
                        )
                        == 0
                    ):
                        result = folder + "/" + "Merged({}).pdf".format(str(num + 1))
                        break
                    else:
                        pass
            outstream = open(result, "wb")
            output.write(outstream)
            QMessageBox.about(self, "알림  ", "병합 완료!")
            outstream.close()
        except:
            QMessageBox.about(self, "에러!  ", "저장 위치를 선택해주세요!")

    #! pdf convert functions
    # pdf convert file add
    def file_add_convert(self):
        file_type = self.comboBox_3.currentText()
        if file_type == "PowerPoint":
            file_name = QFileDialog.getOpenFileNames(
                None, "ppt 파일 불러오기", "", "ppt 파일(*.ppt *.pptx)"
            )
        else:
            file_name = QFileDialog.getOpenFileNames(
                None, "word 파일 불러오기", "", "word 파일(*.docx)"
            )
        count = len(file_name[0])

        for i in range(count):
            self.listWidget_5.addItem(QListWidgetItem(file_name[0][i]))

    # pdf convert file delete
    def file_del_convert(self):
        self.listWidget_5.takeItem(self.listWidget_5.currentRow())

    # pdf convert file convert
    def file_convert(self):
        try:
            file_type = self.comboBox_3.currentText()
            file_count = self.listWidget_5.count()
            if file_type == "PowerPoint":
                for x in range(file_count):
                    file = self.listWidget_5.item(x).text().replace("/", "\\")
                    pre, etx = os.path.splitext(file)
                    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
                    powerpoint.Visible = 1
                    deck = powerpoint.Presentations.Open(file, WithWindow=False)
                    deck.SaveAs(pre + ".pdf", 32)
                    deck.Close()
                    powerpoint.Quit()

            else:
                for i in range(file_count):
                    input_file = self.listWidget_5.item(i).text()

                    convert(input_file)
            QMessageBox.about(self, "알림", "변환되었습니다!")
        except:
            QMessageBox.about(self, "에러! ", "에러!")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
