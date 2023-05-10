# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(998, 600)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setStyleSheet("font-faimly:微软雅黑;")
        self.label_RightBackground = QtWidgets.QLabel(Form)
        self.label_RightBackground.setGeometry(QtCore.QRect(650, 60, 301, 471))
        self.label_RightBackground.setStyleSheet("border-top-right-radius:30px;\n"
"border-bottom-right-radius:30px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_RightBackground.setText("")
        self.label_RightBackground.setObjectName("label_RightBackground")
        self.labelLeftBackground = QtWidgets.QLabel(Form)
        self.labelLeftBackground.setGeometry(QtCore.QRect(60, 60, 591, 471))
        self.labelLeftBackground.setStyleSheet("border-image: url(:/images/images/wallhaven-6qdz1w.jpg);\n"
"border-top-left-radius:30px;\n"
"border-bottom-left-radius:30px;")
        self.labelLeftBackground.setText("")
        self.labelLeftBackground.setObjectName("labelLeftBackground")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(660, 150, 281, 261))
        self.widget_2.setObjectName("widget_2")
        self.lineEdit_account = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_account.setGeometry(QtCore.QRect(30, 100, 221, 41))
        self.lineEdit_account.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px;")
        self.lineEdit_account.setObjectName("lineEdit_account")
        self.lineEdit_password = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_password.setGeometry(QtCore.QRect(30, 180, 221, 41))
        self.lineEdit_password.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px;")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 221, 41))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 Heavy")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(710, 420, 181, 61))
        self.widget.setObjectName("widget")
        self.pushButton_login = QtWidgets.QPushButton(self.widget)
        self.pushButton_login.setGeometry(QtCore.QRect(40, 20, 93, 28))
        self.pushButton_login.setStyleSheet("#pushButton_login{\n"
"    background-color:rgb(0,0,0);\n"
"    color:rgb(255,255,255);\n"
"    border:3px solid rgb(0,0,0);\n"
"    border-radius:7px;\n"
"}\n"
"#pushButton_login:hover{\n"
"    background-color:rgb(255,255,255);\n"
"    color:rgb(0,0,0);\n"
"}\n"
"#pushButton_login:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_close = QtWidgets.QPushButton(Form)
        self.pushButton_close.setGeometry(QtCore.QRect(890, 70, 41, 28))
        self.pushButton_close.setStyleSheet("border:None;")
        self.pushButton_close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/icon/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_close.setIcon(icon)
        self.pushButton_close.setObjectName("pushButton_close")

        self.retranslateUi(Form)
        self.pushButton_close.clicked.connect(Form.close)
        self.pushButton_login.clicked.connect(Form.login)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_account.setPlaceholderText(_translate("Form", "账号:"))
        self.lineEdit_password.setPlaceholderText(_translate("Form", "密码："))
        self.label_2.setText(_translate("Form", "Tello无人机控制系统"))
        self.pushButton_login.setText(_translate("Form", "登录"))

import resource_rc
