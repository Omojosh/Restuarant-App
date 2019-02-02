# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anotherfoodapp.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 750)
        MainWindow.setStyleSheet("background-color: rgba(11, 1, 1, 122);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.totalAmountBox = QtWidgets.QTextEdit(self.centralwidget)
        self.totalAmountBox.setGeometry(QtCore.QRect(500, 500, 111, 51))
        self.totalAmountBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.totalAmountBox.setPlaceholderText("")
        self.totalAmountBox.setObjectName("totalAmountBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 219, 101, 31))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 oblique 14pt \"Cantarell\";\n"
"background-color: rgb(211, 215, 207);")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 510, 101, 31))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 oblique 13pt \"Cantarell\";\n"
"background-color: rgb(211, 215, 207);\n"
"point size: 12pt")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(67, 500, 101, 51))
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 oblique 13pt \"Cantarell\";\n"
"background-color: rgb(211, 215, 207);\n"
"point size: 12pt")
        self.label_4.setObjectName("label_4")
        self.jollofCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.jollofCheck.setGeometry(QtCore.QRect(70, 160, 101, 28))
        self.jollofCheck.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 oblique 13pt \"Cantarell\";\n"
"alternate-background-color: rgb(204, 0, 0);\n"
"background-color: rgb(211, 215, 207);")
        self.jollofCheck.setObjectName("jollofCheck")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(70, 500, 101, 51))
        self.label_1.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 oblique 13pt \"Cantarell\";\n"
"background-color: rgb(211, 215, 207);\n"
"point size: 12pt")
        self.label_1.setObjectName("label_1")
        self.clearBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn.setGeometry(QtCore.QRect(500, 580, 111, 41))
        self.clearBtn.setStyleSheet("font: 75 oblique 15pt \"Cantarell\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(200, 0, 0);")
        self.clearBtn.setObjectName("clearBtn")
        self.totalMealBtn = QtWidgets.QPushButton(self.centralwidget)
        self.totalMealBtn.setGeometry(QtCore.QRect(210, 580, 151, 41))
        self.totalMealBtn.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(211, 215, 207);\n"
"font: 75 oblique 15pt \"Cantarell\";")
        self.totalMealBtn.setObjectName("totalMealBtn")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(213, 340, 151, 51))
        self.textEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 70, 471, 20))
        self.label_6.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(204, 0, 0);\n"
"font: 75 oblique 12pt \"Cantarell\";")
        self.label_6.setObjectName("label_6")
        self.reciept = QtWidgets.QTextEdit(self.centralwidget)
        self.reciept.setGeometry(QtCore.QRect(460, 100, 301, 111))
        self.reciept.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.reciept.setObjectName("reciept")
        self.dt = QtWidgets.QDateEdit(self.centralwidget)
        self.dt.setGeometry(QtCore.QRect(390, 350, 110, 29))
        self.dt.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.dt.setCalendarPopup(True)
        self.dt.setObjectName("dt")
        self.comboBoxD = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxD.setGeometry(QtCore.QRect(210, 220, 151, 31))
        self.comboBoxD.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(211, 215, 207);")
        self.comboBoxD.setObjectName("comboBoxD")
        self.comboBoxD.addItem("")
        self.comboBoxD.addItem("")
        self.comboBoxD.addItem("")
        self.comboBoxD.addItem("")
        self.comboBoxD.addItem("")
        self.comboBoxD.addItem("")
        self.comboBoxD.addItem("")
        self.comboBoxD.addItem("")
        self.comboBoxD.addItem("")
        self.comboBoxD.setItemText(8, "")
        self.mealTotal = QtWidgets.QTextEdit(self.centralwidget)
        self.mealTotal.setGeometry(QtCore.QRect(210, 500, 151, 51))
        self.mealTotal.setStyleSheet("color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.mealTotal.setPlaceholderText("")
        self.mealTotal.setObjectName("mealTotal")
        self.friedCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.friedCheck.setGeometry(QtCore.QRect(70, 110, 101, 31))
        self.friedCheck.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 oblique 13pt \"Cantarell\";\n"
"alternate-background-color: rgb(204, 0, 0);\n"
"background-color: rgb(211, 215, 207);")
        self.friedCheck.setObjectName("friedCheck")
        self.drinksSpin = QtWidgets.QSpinBox(self.centralwidget)
        self.drinksSpin.setGeometry(QtCore.QRect(390, 220, 71, 31))
        self.drinksSpin.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(211, 215, 207);\n"
"border-color: rgb(46, 52, 54);")
        self.drinksSpin.setObjectName("drinksSpin")
        self.drinkTotal = QtWidgets.QTextEdit(self.centralwidget)
        self.drinkTotal.setGeometry(QtCore.QRect(210, 340, 151, 51))
        self.drinkTotal.setStyleSheet("color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.drinkTotal.setPlaceholderText("")
        self.drinkTotal.setObjectName("drinkTotal")
        self.friedSpin = QtWidgets.QSpinBox(self.centralwidget)
        self.friedSpin.setGeometry(QtCore.QRect(210, 110, 151, 29))
        self.friedSpin.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(211, 215, 207);\n"
"border-color: rgb(46, 52, 54);")
        self.friedSpin.setReadOnly(True)
        self.friedSpin.setMaximum(1000000000)
        self.friedSpin.setProperty("value", 0)
        self.friedSpin.setObjectName("friedSpin")
        self.jolfsSpin = QtWidgets.QSpinBox(self.centralwidget)
        self.jolfsSpin.setGeometry(QtCore.QRect(210, 160, 151, 29))
        self.jolfsSpin.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(211, 215, 207);\n"
"border-color: rgb(46, 52, 54);")
        self.jolfsSpin.setReadOnly(True)
        self.jolfsSpin.setMaximum(1000000000)
        self.jolfsSpin.setObjectName("jolfsSpin")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 340, 101, 51))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 oblique 13pt \"Cantarell\";\n"
"background-color: rgb(211, 215, 207);\n"
"point size: 12pt")
        self.label_2.setObjectName("label_2")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(70, 10, 691, 51))
        self.logo.setStyleSheet("font: 75 oblique 16pt \"Cantarell\";\n"
"color: rgb(204, 0, 0);\n"
"gridline-color: rgb(204, 0, 0);\n"
"border-color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.logo.setObjectName("logo")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 220, 101, 31))
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 oblique 14pt \"Cantarell\";\n"
"background-color: rgb(211, 215, 207);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 280, 101, 31))
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 oblique 14pt \"Cantarell\";\n"
"background-color: rgb(211, 215, 207);")
        self.label_8.setObjectName("label_8")
        self.drinkScroll = QtWidgets.QComboBox(self.centralwidget)
        self.drinkScroll.setGeometry(QtCore.QRect(210, 220, 151, 31))
        self.drinkScroll.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(211, 215, 207);")
        self.drinkScroll.setObjectName("drinkScroll")
        self.drinkScroll.addItem("")
        self.drinkScroll.addItem("")
        self.drinkScroll.addItem("")
        self.drinkScroll.addItem("")
        self.drinkScroll.addItem("")
        self.drinkScroll.addItem("")
        self.drinkScroll.addItem("")
        self.drinkScroll.addItem("")
        self.drinkScroll.addItem("")
        self.drinkScroll.addItem("")
        self.drinkScroll.setItemText(9, "")
        self.ogunfsScroll = QtWidgets.QComboBox(self.centralwidget)
        self.ogunfsScroll.setGeometry(QtCore.QRect(210, 280, 151, 28))
        self.ogunfsScroll.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(211, 215, 207);")
        self.ogunfsScroll.setObjectName("ogunfsScroll")
        self.ogunfsScroll.addItem("")
        self.ogunfsScroll.addItem("")
        self.ogunfsScroll.addItem("")
        self.ogunfsScroll.addItem("")
        self.ogunfsScroll.addItem("")
        self.ogunfsScroll.addItem("")
        self.ogunfsScroll.addItem("")
        self.ogunfsScroll.addItem("")
        self.ogunfsSpin = QtWidgets.QSpinBox(self.centralwidget)
        self.ogunfsSpin.setGeometry(QtCore.QRect(390, 280, 71, 31))
        self.ogunfsSpin.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(211, 215, 207);\n"
"border-color: rgb(46, 52, 54);")
        self.ogunfsSpin.setObjectName("ogunfsSpin")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 420, 101, 51))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 oblique 13pt \"Cantarell\";\n"
"background-color: rgb(211, 215, 207);\n"
"point size: 12pt")
        self.label_3.setObjectName("label_3")
        self.meatTotal = QtWidgets.QTextEdit(self.centralwidget)
        self.meatTotal.setGeometry(QtCore.QRect(210, 420, 151, 51))
        self.meatTotal.setStyleSheet("color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.meatTotal.setPlaceholderText("")
        self.meatTotal.setObjectName("meatTotal")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(72, 640, 691, 41))
        self.label_9.setStyleSheet("background-color: rgb(211, 215, 207);\n"
"font: 75 oblique 13pt \"Cantarell\";\n"
"color: rgb(204, 0, 0);")
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
  ###########################################################
        self.friedCheck.stateChanged.connect(self.changeIt)
        self.jollofCheck.stateChanged.connect(self.changeAm)
        self.totalMealBtn.clicked.connect(self.calculateIt)
        self.clearBtn.clicked.connect(self.clearIt)

    def changeIt(self, state):
            if state == QtCore.Qt.Checked:
                    self.friedSpin.setReadOnly(False)
            else:
                    self.friedSpin.setReadOnly(True)
                    self.friedSpin.clear()

    def changeAm(self,state):
            if state == QtCore.Qt.Checked:
                    self.jolfsSpin.setReadOnly(False)
            else:
                    self.jolfsSpin.setReadOnly(True)
                    self.jolfsSpin.clear()

    def calculateIt(self):
            friedQty = int(self.friedSpin.value()) * (100)
            jollofQty = int(self.jolfsSpin.value()) * (150)
            foodSum = friedQty + jollofQty
            self.mealTotal.setText(str(foodSum)) 
            CocaColaA = ["Coca-Cola","Malt","Beta-Malt"]
            pepsiA = ["Pepsi", "7up", "Mirinda"]
            expD = ["Heinekein", "Henessy"]
            if self.drinkScroll.currentText() in CocaColaA:
                    dPrice = 150
            elif self.drinkScroll.currentText() in pepsiA:
                    dPrice = 100
            elif self.drinkScroll.currentText() in expD:
                    dPrice = 500
            drinkSum = int(self.drinksSpin.value()) * dPrice
            self.drinkTotal.setText(str(drinkSum))
            ogunfFam = ['Ogunfe', 'Dog', 'Pork']
            pomsFam = ['Ponmo', "Bokoto"]
            beefFam = ['Beef', 'Tinu']
            if self.ogunfsScroll.currentText() in ogunfFam:
                    mPrice = 300
            elif self.ogunfsScroll.currentText() in pomsFam:
                    mPrice = 150
            elif self.ogunfsScroll.currentText() in beefFam:
                    mPrice = 100
            meatSum = int(self.ogunfsSpin.value()) * mPrice
            self.meatTotal.setText(str(meatSum))
            allFoodTotal = int(meatSum) + int(drinkSum) + int(foodSum)
            self.totalAmountBox.setText(str(allFoodTotal))
            dat = self.dt.date()
            dateDisplay = "{}/ {}/ {}".format(dat.day(), dat.month(), dat.year())
            drinkCal = "Your drink Amt is #" + str(drinkSum) + "\n"
            meatCal = "Your meat Amt is #"+ str(meatSum) + "\n"
            mealCal = "Your meal Amt is #" + str(foodSum) + "\n"
            totalAmt = "Total amount is #" + str(allFoodTotal) + "\n"
            self.reciept.setText(drinkCal+ meatCal + mealCal + totalAmt + "Date is "  +dateDisplay)
  
    def clearIt(self):
            self.drinkScroll.setCurrentText("Reset")
            self.ogunfsScroll.setCurrentText("Reset")
            self.friedCheck.setChecked(False)
            self.jollofCheck.setChecked(False)
            self.friedSpin.clear()
            self.jolfsSpin.clear()
            self.totalAmountBox.clear()
            self.mealTotal.clear()
            self.meatTotal.clear()
            self.drinkTotal.clear()
            self.reciept.clear()
            self.drinksSpin.clear()
            self.ogunfsSpin.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "   Drinks"))
        self.label_5.setText(_translate("MainWindow", "Total Amount"))
        self.label_4.setText(_translate("MainWindow", "  Meal Total"))
        self.jollofCheck.setText(_translate("MainWindow", "  Jollof "))
        self.label_1.setText(_translate("MainWindow", "  Meal Total"))
        self.clearBtn.setText(_translate("MainWindow", "Clear Meal"))
        self.totalMealBtn.setText(_translate("MainWindow", "Total Meal"))
        self.label_6.setText(_translate("MainWindow", "***Please, you have to tick the boxes before you order, Thank You."))
        self.dt.setDisplayFormat(_translate("MainWindow", "dd-MMM-yyyy"))
        self.comboBoxD.setItemText(0, _translate("MainWindow", "Coca-Cola"))
        self.comboBoxD.setItemText(1, _translate("MainWindow", "Pepsi"))
        self.comboBoxD.setItemText(2, _translate("MainWindow", "Mirinda"))
        self.comboBoxD.setItemText(3, _translate("MainWindow", "Heinekein"))
        self.comboBoxD.setItemText(4, _translate("MainWindow", "Henessy"))
        self.comboBoxD.setItemText(5, _translate("MainWindow", "7up"))
        self.comboBoxD.setItemText(6, _translate("MainWindow", "Beta-Malt"))
        self.comboBoxD.setItemText(7, _translate("MainWindow", "Malt"))
        self.friedCheck.setText(_translate("MainWindow", " Fried Rice"))
        self.drinkTotal.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "  Drinks Total"))
        self.logo.setText(_translate("MainWindow", "                                     FOOD & DRINKS RESTAURANT   "))
        self.label_7.setText(_translate("MainWindow", "   Drinks"))
        self.label_8.setText(_translate("MainWindow", "    Meat"))
        self.drinkScroll.setCurrentText(_translate("MainWindow", "Reset"))
        self.drinkScroll.setItemText(0, _translate("MainWindow", "Reset"))
        self.drinkScroll.setItemText(1, _translate("MainWindow", "Coca-Cola"))
        self.drinkScroll.setItemText(2, _translate("MainWindow", "Pepsi"))
        self.drinkScroll.setItemText(3, _translate("MainWindow", "Mirinda"))
        self.drinkScroll.setItemText(4, _translate("MainWindow", "Heinekein"))
        self.drinkScroll.setItemText(5, _translate("MainWindow", "Henessy"))
        self.drinkScroll.setItemText(6, _translate("MainWindow", "7up"))
        self.drinkScroll.setItemText(7, _translate("MainWindow", "Beta-Malt"))
        self.drinkScroll.setItemText(8, _translate("MainWindow", "Malt"))
        self.ogunfsScroll.setItemText(0, _translate("MainWindow", "Reset"))
        self.ogunfsScroll.setItemText(1, _translate("MainWindow", "Ogunfe"))
        self.ogunfsScroll.setItemText(2, _translate("MainWindow", "Beef"))
        self.ogunfsScroll.setItemText(3, _translate("MainWindow", "Ponmo"))
        self.ogunfsScroll.setItemText(4, _translate("MainWindow", "Pork"))
        self.ogunfsScroll.setItemText(5, _translate("MainWindow", "Dog"))
        self.ogunfsScroll.setItemText(6, _translate("MainWindow", "Tinu"))
        self.ogunfsScroll.setItemText(7, _translate("MainWindow", "Bokoto"))
        self.label_3.setText(_translate("MainWindow", "  Meat Total"))
        self.label_9.setText(_translate("MainWindow", "                                          Copyright@ Omojosh 2019"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

