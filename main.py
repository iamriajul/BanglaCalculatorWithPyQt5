from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton
from calculator_ui import Ui_Calculator


class mainWindow(QtWidgets.QMainWindow, Ui_Calculator):

    operationPressed = False
    firstValue = -1
    secondValue = -1

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton_0.clicked.connect(self.onPressedDigit)
        self.pushButton_1.clicked.connect(self.onPressedDigit)
        self.pushButton_2.clicked.connect(self.onPressedDigit)
        self.pushButton_3.clicked.connect(self.onPressedDigit)
        self.pushButton_4.clicked.connect(self.onPressedDigit)
        self.pushButton_5.clicked.connect(self.onPressedDigit)
        self.pushButton_6.clicked.connect(self.onPressedDigit)
        self.pushButton_7.clicked.connect(self.onPressedDigit)
        self.pushButton_8.clicked.connect(self.onPressedDigit)
        self.pushButton_9.clicked.connect(self.onPressedDigit)
        self.pushButton_decimal.clicked.connect(self.onPressedDigit)

        self.pushButton_plus.clicked.connect(self.onPressedOperation)
        self.pushButton_minus.clicked.connect(self.onPressedOperation)
        self.pushButton_multiply.clicked.connect(self.onPressedOperation)
        self.pushButton_divide.clicked.connect(self.onPressedOperation)
        self.pushButton_percent.clicked.connect(self.onPressedOperation)

        self.pushButton_clear.clicked.connect(self.onPressedClear)
        self.pushButton_equals.clicked.connect(self.onPressedEquals)


    def onPressedDigit(self):
        button : QPushButton = self.sender()
        if self.label.text() == "০" and self.operationPressed == False:
            self.label.setText(button.text())
        elif self.operationPressed != False:

            if self.label.text() == "০":
                self.label.setText(button.text())
            else:
                self.label.setText(self.label.text() + button.text())

            self.secondValue = float(self.bnNumToEn(self.label.text()))

        else:
            self.label.setText(self.label.text() + button.text())

    def onPressedOperation(self):
        button : QPushButton = self.sender()
        
        if self.label.text() != "০" and self.operationPressed == False:
            self.operationPressed = button.whatsThis()

            self.firstValue = float(self.bnNumToEn(self.label.text()))
            self.label.setText(self.enNumToBn("0"))

        if self.label.text() != "০" and self.operationPressed != False:

            result = -1
            if self.operationPressed == "plus":
                result = self.firstValue + self.secondValue
            elif self.operationPressed == "minus":
                result = self.firstValue - self.secondValue
            elif self.operationPressed == "multiply":
                result = self.firstValue * self.secondValue
            elif self.operationPressed == "divide":
                result = self.firstValue / self.secondValue
            elif self.operationPressed == "percent":
                result = (self.firstValue / 100) * self.secondValue

            self.firstValue = result
            self.operationPressed = button.whatsThis()
            self.label.setText(self.enNumToBn("0"))





    def onPressedEquals(self):
        if self.operationPressed == "plus":
            self.label.setText(self.enNumToBn(str(self.firstValue + self.secondValue)))
        elif self.operationPressed == "minus":
            self.label.setText(self.enNumToBn(str(self.firstValue - self.secondValue)))
        elif self.operationPressed == "multiply":
            self.label.setText(self.enNumToBn(str(self.firstValue * self.secondValue)))
        elif self.operationPressed == "divide":
            self.label.setText(self.enNumToBn(str(self.firstValue / self.secondValue)))
        elif self.operationPressed == "percent":
            self.label.setText(self.enNumToBn(str((self.firstValue / 100) * self.secondValue)))

        self.firstValue = float(self.bnNumToEn(self.label.text()))
        self.secondValue = -1



    def onPressedClear(self):
        self.label.setText("০")
        self.operationPressed = False
        self.firstValue = -1


    def enNumToBn(self, number : str):
        return number.replace("0", "০").replace("1", "১").replace("2", "২").replace("3", "৩").replace("4", "৪").replace("5", "৫").replace("6", "৬").replace("7", "৭").replace("8", "৮").replace("9", "৯")

    def bnNumToEn(self, number: str):
        return number.replace("০", "0").replace("১", "1").replace("২", "2").replace("৩", "3").replace("৪", "4").replace("৫", "5").replace("৬", "6").replace("৭", "7").replace("৮", "8").replace("৯", "9")


