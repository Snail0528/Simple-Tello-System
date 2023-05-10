# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1232, 874)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_keyBoardControl = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_keyBoardControl.setGeometry(QtCore.QRect(940, 150, 111, 121))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_keyBoardControl.setFont(font)
        self.pushButton_keyBoardControl.setStyleSheet("#pushButton_keyBoardControl{\n"
"    background-color:rgb(61,60,98);\n"
"    color:rgb(255,255,255);\n"
"    border:3px solid rgb(61,60,98);\n"
"    border-radius:11px;\n"
"}\n"
"#pushButton_keyBoardControl:hover{\n"
"    background-color:rgb(241, 107, 114);\n"
"}\n"
"#pushButton_keyBoardControl:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.pushButton_keyBoardControl.setText("")
        self.pushButton_keyBoardControl.setObjectName("pushButton_keyBoardControl")
        self.pushButton_faceTracking = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_faceTracking.setGeometry(QtCore.QRect(940, 300, 111, 121))
        self.pushButton_faceTracking.setStyleSheet("#pushButton_faceTracking{\n"
"    background-color:rgb(61,60,98);\n"
"    color:rgb(255,255,255);\n"
"    border:3px solid rgb(61,60,98);\n"
"    border-radius:11px;\n"
"}\n"
"#pushButton_faceTracking:hover{\n"
"    background-color:rgb(241, 107, 114);\n"
"    color:rgb(255,255,255);\n"
"}\n"
"#pushButton_faceTracking:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.pushButton_faceTracking.setText("")
        self.pushButton_faceTracking.setObjectName("pushButton_faceTracking")
        self.pushButton_objectTracking = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_objectTracking.setGeometry(QtCore.QRect(940, 450, 111, 121))
        self.pushButton_objectTracking.setStyleSheet("#pushButton_objectTracking{\n"
"    background-color:rgb(61,60,98);\n"
"    color:rgb(255,255,255);\n"
"    border:3px solid rgb(61,60,98);\n"
"    border-radius:11px;\n"
"}\n"
"#pushButton_objectTracking:hover{\n"
"    background-color:rgb(241, 107, 114);\n"
"    color:rgb(255,255,255);\n"
"}\n"
"#pushButton_objectTracking:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.pushButton_objectTracking.setText("")
        self.pushButton_objectTracking.setObjectName("pushButton_objectTracking")
        self.pushButton_power = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_power.setGeometry(QtCore.QRect(560, 640, 171, 31))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_power.setFont(font)
        self.pushButton_power.setStyleSheet("#pushButton_power{\n"
"    color:rgb(255,255,255);\n"
"    border:3px solid rgb(241, 107, 114);\n"
"    border-radius:7px;\n"
"}\n"
"#pushButton_power:hover{\n"
"    background-color:rgb(241, 107, 114);\n"
"    color:rgb(255,255,255);\n"
"}\n"
"#pushButton_power:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.pushButton_power.setObjectName("pushButton_power")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 50, 861, 641))
        self.label.setStyleSheet("background-color: rgb(42, 39, 66);\n"
"border-top-left-radius:30px;\n"
"border-bottom-left-radius:30px;\n"
"border-top-right-radius:30px;\n"
"border-bottom-right-radius:30px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.kbicon = QtWidgets.QPushButton(self.centralwidget)
        self.kbicon.setGeometry(QtCore.QRect(970, 180, 51, 41))
        self.kbicon.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 132, 139, 0);;\n"
"    border:None;\n"
"}\n"
"")
        self.kbicon.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/icon/键盘.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kbicon.setIcon(icon)
        self.kbicon.setIconSize(QtCore.QSize(40, 40))
        self.kbicon.setCheckable(False)
        self.kbicon.setChecked(False)
        self.kbicon.setAutoExclusive(False)
        self.kbicon.setFlat(False)
        self.kbicon.setObjectName("kbicon")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(960, 220, 91, 31))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(960, 520, 71, 31))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(960, 370, 71, 31))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.fticon = QtWidgets.QPushButton(self.centralwidget)
        self.fticon.setGeometry(QtCore.QRect(970, 320, 51, 51))
        self.fticon.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 132, 139, 0);;\n"
"    border:None;\n"
"}\n"
"")
        self.fticon.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("res/icon/人脸跟踪.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fticon.setIcon(icon1)
        self.fticon.setIconSize(QtCore.QSize(40, 40))
        self.fticon.setCheckable(False)
        self.fticon.setChecked(False)
        self.fticon.setAutoExclusive(False)
        self.fticon.setFlat(False)
        self.fticon.setObjectName("fticon")
        self.oticon = QtWidgets.QPushButton(self.centralwidget)
        self.oticon.setGeometry(QtCore.QRect(970, 470, 51, 51))
        self.oticon.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 132, 139, 0);;\n"
"    border:None;\n"
"}\n"
"")
        self.oticon.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("res/icon/物体检测数据集.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.oticon.setIcon(icon2)
        self.oticon.setIconSize(QtCore.QSize(40, 40))
        self.oticon.setCheckable(False)
        self.oticon.setChecked(False)
        self.oticon.setAutoExclusive(False)
        self.oticon.setFlat(False)
        self.oticon.setObjectName("oticon")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 60, 261, 41))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 Heavy")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.pushButton_battery = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_battery.setGeometry(QtCore.QRect(270, 150, 111, 121))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_battery.setFont(font)
        self.pushButton_battery.setStyleSheet("#pushButton_battery{\n"
"    background-color:rgb(61,60,98);\n"
"    color:rgb(255,255,255);\n"
"    border:3px solid rgb(61,60,98);\n"
"    border-radius:11px;\n"
"}\n"
"")
        self.pushButton_battery.setText("")
        self.pushButton_battery.setObjectName("pushButton_battery")
        self.pushButton_temperature = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_temperature.setGeometry(QtCore.QRect(270, 450, 111, 121))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_temperature.setFont(font)
        self.pushButton_temperature.setStyleSheet("#pushButton_temperature{\n"
"    background-color:rgb(61,60,98);\n"
"    color:rgb(255,255,255);\n"
"    border:3px solid rgb(61,60,98);\n"
"    border-radius:11px;\n"
"}\n"
"")
        self.pushButton_temperature.setText("")
        self.pushButton_temperature.setObjectName("pushButton_temperature")
        self.pushButton_wifi = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_wifi.setGeometry(QtCore.QRect(270, 300, 111, 121))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_wifi.setFont(font)
        self.pushButton_wifi.setStyleSheet("#pushButton_wifi{\n"
"    background-color:rgb(61,60,98);\n"
"    color:rgb(255,255,255);\n"
"    border:3px solid rgb(61,60,98);\n"
"    border-radius:11px;\n"
"}\n"
"")
        self.pushButton_wifi.setText("")
        self.pushButton_wifi.setObjectName("pushButton_wifi")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 230, 41, 31))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 380, 81, 31))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 530, 71, 31))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.kbicon_2 = QtWidgets.QPushButton(self.centralwidget)
        self.kbicon_2.setGeometry(QtCore.QRect(270, 180, 51, 41))
        self.kbicon_2.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 132, 139, 0);;\n"
"    border:None;\n"
"}\n"
"")
        self.kbicon_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("res/icon/电池.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kbicon_2.setIcon(icon3)
        self.kbicon_2.setIconSize(QtCore.QSize(40, 40))
        self.kbicon_2.setCheckable(False)
        self.kbicon_2.setChecked(False)
        self.kbicon_2.setAutoExclusive(False)
        self.kbicon_2.setFlat(False)
        self.kbicon_2.setObjectName("kbicon_2")
        self.kbicon_3 = QtWidgets.QPushButton(self.centralwidget)
        self.kbicon_3.setGeometry(QtCore.QRect(270, 330, 51, 41))
        self.kbicon_3.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 132, 139, 0);;\n"
"    border:None;\n"
"}\n"
"")
        self.kbicon_3.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("res/icon/wifi_填充.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kbicon_3.setIcon(icon4)
        self.kbicon_3.setIconSize(QtCore.QSize(40, 40))
        self.kbicon_3.setCheckable(False)
        self.kbicon_3.setChecked(False)
        self.kbicon_3.setAutoExclusive(False)
        self.kbicon_3.setFlat(False)
        self.kbicon_3.setObjectName("kbicon_3")
        self.kbicon_4 = QtWidgets.QPushButton(self.centralwidget)
        self.kbicon_4.setGeometry(QtCore.QRect(270, 470, 51, 41))
        self.kbicon_4.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 132, 139, 0);;\n"
"    border:None;\n"
"}\n"
"")
        self.kbicon_4.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("res/icon/温度.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kbicon_4.setIcon(icon5)
        self.kbicon_4.setIconSize(QtCore.QSize(40, 40))
        self.kbicon_4.setCheckable(False)
        self.kbicon_4.setChecked(False)
        self.kbicon_4.setAutoExclusive(False)
        self.kbicon_4.setFlat(False)
        self.kbicon_4.setObjectName("kbicon_4")
        self.label_battery = QtWidgets.QLabel(self.centralwidget)
        self.label_battery.setGeometry(QtCore.QRect(320, 180, 61, 41))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_battery.setFont(font)
        self.label_battery.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_battery.setText("")
        self.label_battery.setObjectName("label_battery")
        self.label_wifi = QtWidgets.QLabel(self.centralwidget)
        self.label_wifi.setGeometry(QtCore.QRect(320, 330, 61, 41))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_wifi.setFont(font)
        self.label_wifi.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_wifi.setText("")
        self.label_wifi.setObjectName("label_wifi")
        self.label_temperature = QtWidgets.QLabel(self.centralwidget)
        self.label_temperature.setGeometry(QtCore.QRect(320, 470, 61, 41))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_temperature.setFont(font)
        self.label_temperature.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_temperature.setText("")
        self.label_temperature.setObjectName("label_temperature")
        self.label_stream = QtWidgets.QLabel(self.centralwidget)
        self.label_stream.setGeometry(QtCore.QRect(400, 160, 511, 401))
        self.label_stream.setText("")
        self.label_stream.setObjectName("label_stream")
        self.label.raise_()
        self.pushButton_keyBoardControl.raise_()
        self.pushButton_faceTracking.raise_()
        self.pushButton_objectTracking.raise_()
        self.pushButton_power.raise_()
        self.kbicon.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.fticon.raise_()
        self.oticon.raise_()
        self.label_5.raise_()
        self.pushButton_battery.raise_()
        self.pushButton_temperature.raise_()
        self.pushButton_wifi.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.kbicon_2.raise_()
        self.kbicon_3.raise_()
        self.kbicon_4.raise_()
        self.label_battery.raise_()
        self.label_wifi.raise_()
        self.label_temperature.raise_()
        self.label_stream.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1232, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_keyBoardControl.clicked.connect(MainWindow.kbc)
        self.pushButton_faceTracking.clicked.connect(MainWindow.ft)
        self.pushButton_objectTracking.clicked.connect(MainWindow.ot)
        self.pushButton_power.clicked.connect(MainWindow.openframe)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_power.setText(_translate("MainWindow", "开启视频流"))
        self.label_2.setText(_translate("MainWindow", " 键盘控制"))
        self.label_4.setText(_translate("MainWindow", "物体跟踪"))
        self.label_3.setText(_translate("MainWindow", "人脸跟踪"))
        self.label_5.setText(_translate("MainWindow", "Tello无人机功能界面"))
        self.label_6.setText(_translate("MainWindow", " 电量"))
        self.label_7.setText(_translate("MainWindow", "wifi强度"))
        self.label_8.setText(_translate("MainWindow", "设备温度"))

