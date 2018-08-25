# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(400, 460)
        Calculator.setMaximumSize(QtCore.QSize(400, 460))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Calculator.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(Calculator)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton_multiply = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_multiply.setGeometry(QtCore.QRect(300, 190, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_multiply.setFont(font)
        self.pushButton_multiply.setWhatsThis("multiply")
        self.pushButton_multiply.setStyleSheet("QPushButton{\n"
"    background: #008B18;\n"
"    color: white;\n"
"    border: 1px groove #46EB69;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #009D1D;\n"
"    color: white;\n"
"    border: 1px outset #008B18;\n"
"}")
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(300, 249, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setWhatsThis("plus")
        self.pushButton_plus.setStyleSheet("QPushButton{\n"
"    background: #008B18;\n"
"    color: white;\n"
"    border: 1px groove #46EB69;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #009D1D;\n"
"    color: white;\n"
"    border: 1px outset #008B18;\n"
"}")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_minus = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(300, 319, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.pushButton_minus.setFont(font)
        self.pushButton_minus.setWhatsThis("minus")
        self.pushButton_minus.setStyleSheet("QPushButton{\n"
"    background: #008B18;\n"
"    color: white;\n"
"    border: 1px groove #46EB69;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #009D1D;\n"
"    color: white;\n"
"    border: 1px outset #008B18;\n"
"}")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_equals = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_equals.setGeometry(QtCore.QRect(300, 390, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.pushButton_equals.setFont(font)
        self.pushButton_equals.setStyleSheet("QPushButton{\n"
"    background: #008B18;\n"
"    color: white;\n"
"    border: 1px groove #46EB69;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #009D1D;\n"
"    color: white;\n"
"    border: 1px outset #008B18;\n"
"}")
        self.pushButton_equals.setObjectName("pushButton_equals")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 401, 131))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    background: #5DF274;\n"
"    padding-right: 2px;\n"
"}")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.pushButton_divide = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_divide.setGeometry(QtCore.QRect(300, 130, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_divide.setFont(font)
        self.pushButton_divide.setWhatsThis("divide")
        self.pushButton_divide.setStyleSheet("QPushButton{\n"
"    background: #008B18;\n"
"    color: white;\n"
"    border: 1px groove #46EB69;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #009D1D;\n"
"    color: white;\n"
"    border: 1px outset #008B18;\n"
"}")
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.pushButton_percent = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_percent.setGeometry(QtCore.QRect(200, 129, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_percent.setFont(font)
        self.pushButton_percent.setWhatsThis("percent")
        self.pushButton_percent.setStyleSheet("QPushButton{\n"
"    background: #008B18;\n"
"    color: white;\n"
"    border: 1px groove #46EB69;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #009D1D;\n"
"    color: white;\n"
"    border: 1px outset #008B18;\n"
"}")
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(0, 129, 201, 101))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setStyleSheet("QPushButton{\n"
"    background: #008B18;\n"
"    color: white;\n"
"    border: 1px groove #46EB69;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #009D1D;\n"
"    color: white;\n"
"    border: 1px outset #008B18;\n"
"}")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 279, 100, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_4.setWhatsThis("4")
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    background: #008B18;\n"
"    color: white;\n"
"    border: 1px groove #46EB69;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #009D1D;\n"
"    color: white;\n"
"    border: 1px outset #008B18;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 279, 100, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_5.setWhatsThis("5")
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    background: #008B18;\n"
"    color: white;\n"
"    border: 1px groove #46EB69;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #009D1D;\n"
"    color: white;\n"
"    border: 1px outset #008B18;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 280, 100, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_6.setWhatsThis("6")
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    background: #008B18;\n"
"    color: white;\n"
"    border: 1px groove #46EB69;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #009D1D;\n"
"    color: white;\n"
"    border: 1px outset #008B18;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 330, 100, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_1.setWhatsThis("1")
        self.pushButton_1.setAccessibleName("")
        self.pushButton_1.setStyleSheet("QPushButton{\n"
"    background: #008B18;\n"
"    color: white;\n"
"    border: 1px groove #46EB69;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #009D1D;\n"
"    color: white;\n"
"    border: 1px outset #008B18;\n"
"}")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 329, 100, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_2.setWhatsThis("2")
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background: #008B18;\n"
"    color: white;\n"
"    border: 1px groove #46EB69;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #009D1D;\n"
"    color: white;\n"
"    border: 1px outset #008B18;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 329, 100, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_3.setToolTip("")
        self.pushButton_3.setToolTipDuration(-1)
        self.pushButton_3.setWhatsThis("3")
        self.pushButton_3.setAccessibleName("")
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background: #008B18;\n"
"    color: white;\n"
"    border: 1px groove #46EB69;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #009D1D;\n"
"    color: white;\n"
"    border: 1px outset #008B18;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_0.setGeometry(QtCore.QRect(0, 390, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_0.setWhatsThis("0")
        self.pushButton_0.setAccessibleName("")
        self.pushButton_0.setStyleSheet("QPushButton{\n"
"    background: #008B18;\n"
"    color: white;\n"
"    border: 1px groove #46EB69;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #009D1D;\n"
"    color: white;\n"
"    border: 1px outset #008B18;\n"
"}")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_decimal = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_decimal.setGeometry(QtCore.QRect(200, 390, 100, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_decimal.setFont(font)
        self.pushButton_decimal.setStyleSheet("QPushButton{\n"
"    background: #008B18;\n"
"    color: white;\n"
"    border: 1px groove #46EB69;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #009D1D;\n"
"    color: white;\n"
"    border: 1px outset #008B18;\n"
"}")
        self.pushButton_decimal.setObjectName("pushButton_decimal")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 230, 100, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_7.setWhatsThis("7")
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    background: #008B18;\n"
"    color: white;\n"
"    border: 1px groove #46EB69;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #009D1D;\n"
"    color: white;\n"
"    border: 1px outset #008B18;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_8.setGeometry(QtCore.QRect(100, 230, 100, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_8.setWhatsThis("8")
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    background: #008B18;\n"
"    color: white;\n"
"    border: 1px groove #46EB69;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #009D1D;\n"
"    color: white;\n"
"    border: 1px outset #008B18;\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_9.setGeometry(QtCore.QRect(200, 230, 100, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_9.setWhatsThis("9")
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    background: #008B18;\n"
"    color: white;\n"
"    border: 1px groove #46EB69;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #009D1D;\n"
"    color: white;\n"
"    border: 1px outset #008B18;\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        Calculator.setCentralWidget(self.centralWidget)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Bangla Calculator"))
        self.pushButton_multiply.setText(_translate("Calculator", "×"))
        self.pushButton_plus.setText(_translate("Calculator", "+"))
        self.pushButton_minus.setText(_translate("Calculator", "-"))
        self.pushButton_equals.setText(_translate("Calculator", "="))
        self.label.setText(_translate("Calculator", "০"))
        self.pushButton_divide.setText(_translate("Calculator", "÷"))
        self.pushButton_percent.setText(_translate("Calculator", "%"))
        self.pushButton_clear.setText(_translate("Calculator", "C"))
        self.pushButton_4.setText(_translate("Calculator", "৪"))
        self.pushButton_5.setText(_translate("Calculator", "৫"))
        self.pushButton_6.setText(_translate("Calculator", "৬"))
        self.pushButton_1.setText(_translate("Calculator", "১"))
        self.pushButton_2.setText(_translate("Calculator", "২"))
        self.pushButton_3.setText(_translate("Calculator", "৩"))
        self.pushButton_0.setText(_translate("Calculator", "০"))
        self.pushButton_decimal.setText(_translate("Calculator", "."))
        self.pushButton_7.setText(_translate("Calculator", "৭"))
        self.pushButton_8.setText(_translate("Calculator", "৮"))
        self.pushButton_9.setText(_translate("Calculator", "৯"))

