# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FunctionUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(999, 664)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_keyBoardControl = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_keyBoardControl.setGeometry(QtCore.QRect(690, 110, 111, 121))
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
        self.pushButton_faceTracking.setGeometry(QtCore.QRect(690, 250, 111, 121))
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
        self.pushButton_objectTracking.setGeometry(QtCore.QRect(690, 390, 111, 121))
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
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(310, 510, 171, 31))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setStyleSheet("#pushButton_exit{\n"
"    background-color:rgb(241, 107, 114);\n"
"    color:rgb(255,255,255);\n"
"    border:3px solid rgb(241, 107, 114);\n"
"    border-radius:7px;\n"
"}\n"
"#pushButton_exit:hover{\n"
"    background-color:rgb(241, 107, 114);\n"
"    color:rgb(255,255,255);\n"
"}\n"
"#pushButton_exit:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 50, 681, 511))
        self.label.setStyleSheet("background-color: rgb(42, 39, 66);\n"
"border-top-left-radius:30px;\n"
"border-bottom-left-radius:30px;\n"
"border-top-right-radius:30px;\n"
"border-bottom-right-radius:30px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.kbicon = QtWidgets.QPushButton(self.centralwidget)
        self.kbicon.setGeometry(QtCore.QRect(720, 140, 51, 41))
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
        self.label_2.setGeometry(QtCore.QRect(710, 180, 91, 31))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(710, 460, 71, 31))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(710, 320, 71, 31))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.fticon = QtWidgets.QPushButton(self.centralwidget)
        self.fticon.setGeometry(QtCore.QRect(720, 270, 51, 51))
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
        self.oticon.setGeometry(QtCore.QRect(720, 410, 51, 51))
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
        self.label_5.setGeometry(QtCore.QRect(400, 50, 221, 41))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 Heavy")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label.raise_()
        self.pushButton_keyBoardControl.raise_()
        self.pushButton_faceTracking.raise_()
        self.pushButton_objectTracking.raise_()
        self.pushButton_exit.raise_()
        self.kbicon.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.fticon.raise_()
        self.oticon.raise_()
        self.label_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 999, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_keyBoardControl.clicked.connect(MainWindow.kbc)
        self.pushButton_faceTracking.clicked.connect(MainWindow.ft)
        self.pushButton_objectTracking.clicked.connect(MainWindow.ot)
        self.pushButton_exit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_exit.setText(_translate("MainWindow", "退出"))
        self.label_2.setText(_translate("MainWindow", " 键盘控制"))
        self.label_4.setText(_translate("MainWindow", "物体跟踪"))
        self.label_3.setText(_translate("MainWindow", "人脸跟踪"))
        self.label_5.setText(_translate("MainWindow", "Tello无人机控制系统"))

