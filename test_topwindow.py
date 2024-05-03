# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'topWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 1000)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 700, 411, 221))
        self.calendarWidget.setObjectName("calendarWidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 590, 351, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(410, 590, 371, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.pushButton_Past = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Past.setGeometry(QtCore.QRect(510, 750, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Past.setFont(font)
        self.pushButton_Past.setObjectName("pushButton_Past")
        self.pushButton_Resist = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Resist.setGeometry(QtCore.QRect(510, 840, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Resist.setFont(font)
        self.pushButton_Resist.setObjectName("pushButton_Resist")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 90, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 190, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 260, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 310, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 350, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 440, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(110, 490, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(100, 540, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(150, 140, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.sleepRadio_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.sleepRadio_1.setGeometry(QtCore.QRect(240, 90, 21, 16))
        self.sleepRadio_1.setText("")
        self.sleepRadio_1.setObjectName("sleepRadio_1")
        self.sleepRadio = QtWidgets.QButtonGroup(MainWindow)
        self.sleepRadio.setObjectName("sleepRadio")
        self.sleepRadio.addButton(self.sleepRadio_1)
        self.sleepRadio_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.sleepRadio_2.setGeometry(QtCore.QRect(340, 90, 21, 16))
        self.sleepRadio_2.setText("")
        self.sleepRadio_2.setObjectName("sleepRadio_2")
        self.sleepRadio.addButton(self.sleepRadio_2)
        self.sleepRadio_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.sleepRadio_3.setGeometry(QtCore.QRect(440, 90, 21, 16))
        self.sleepRadio_3.setText("")
        self.sleepRadio_3.setObjectName("sleepRadio_3")
        self.sleepRadio.addButton(self.sleepRadio_3)
        self.sleepRadio_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.sleepRadio_4.setGeometry(QtCore.QRect(540, 90, 21, 16))
        self.sleepRadio_4.setText("")
        self.sleepRadio_4.setObjectName("sleepRadio_4")
        self.sleepRadio.addButton(self.sleepRadio_4)
        self.sleepRadio_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.sleepRadio_5.setGeometry(QtCore.QRect(640, 90, 21, 16))
        self.sleepRadio_5.setText("")
        self.sleepRadio_5.setObjectName("sleepRadio_5")
        self.sleepRadio.addButton(self.sleepRadio_5)
        self.trustMeRadio_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.trustMeRadio_4.setGeometry(QtCore.QRect(540, 440, 21, 16))
        self.trustMeRadio_4.setText("")
        self.trustMeRadio_4.setObjectName("trustMeRadio_4")
        self.trustMeRadio = QtWidgets.QButtonGroup(MainWindow)
        self.trustMeRadio.setObjectName("trustMeRadio")
        self.trustMeRadio.addButton(self.trustMeRadio_4)
        self.trustMeRadio_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.trustMeRadio_1.setGeometry(QtCore.QRect(240, 440, 21, 16))
        self.trustMeRadio_1.setText("")
        self.trustMeRadio_1.setObjectName("trustMeRadio_1")
        self.trustMeRadio.addButton(self.trustMeRadio_1)
        self.trustMeRadio_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.trustMeRadio_3.setGeometry(QtCore.QRect(440, 440, 21, 16))
        self.trustMeRadio_3.setText("")
        self.trustMeRadio_3.setObjectName("trustMeRadio_3")
        self.trustMeRadio.addButton(self.trustMeRadio_3)
        self.trustMeRadio_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.trustMeRadio_2.setGeometry(QtCore.QRect(340, 440, 21, 16))
        self.trustMeRadio_2.setText("")
        self.trustMeRadio_2.setObjectName("trustMeRadio_2")
        self.trustMeRadio.addButton(self.trustMeRadio_2)
        self.trustMeRadio_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.trustMeRadio_5.setGeometry(QtCore.QRect(640, 440, 21, 16))
        self.trustMeRadio_5.setText("")
        self.trustMeRadio_5.setObjectName("trustMeRadio_5")
        self.trustMeRadio.addButton(self.trustMeRadio_5)
        self.mealRadio_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.mealRadio_3.setGeometry(QtCore.QRect(440, 140, 21, 16))
        self.mealRadio_3.setText("")
        self.mealRadio_3.setObjectName("mealRadio_3")
        self.mealRadio = QtWidgets.QButtonGroup(MainWindow)
        self.mealRadio.setObjectName("mealRadio")
        self.mealRadio.addButton(self.mealRadio_3)
        self.mealRadio_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.mealRadio_5.setGeometry(QtCore.QRect(640, 140, 21, 16))
        self.mealRadio_5.setText("")
        self.mealRadio_5.setObjectName("mealRadio_5")
        self.mealRadio.addButton(self.mealRadio_5)
        self.mealRadio_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.mealRadio_1.setGeometry(QtCore.QRect(240, 140, 21, 16))
        self.mealRadio_1.setText("")
        self.mealRadio_1.setObjectName("mealRadio_1")
        self.mealRadio.addButton(self.mealRadio_1)
        self.mealRadio_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.mealRadio_2.setGeometry(QtCore.QRect(340, 140, 21, 16))
        self.mealRadio_2.setText("")
        self.mealRadio_2.setObjectName("mealRadio_2")
        self.mealRadio.addButton(self.mealRadio_2)
        self.mealRadio_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.mealRadio_4.setGeometry(QtCore.QRect(540, 140, 21, 16))
        self.mealRadio_4.setText("")
        self.mealRadio_4.setObjectName("mealRadio_4")
        self.mealRadio.addButton(self.mealRadio_4)
        self.trustOtherRadio_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.trustOtherRadio_5.setGeometry(QtCore.QRect(640, 490, 21, 16))
        self.trustOtherRadio_5.setText("")
        self.trustOtherRadio_5.setObjectName("trustOtherRadio_5")
        self.trustOtherRadio = QtWidgets.QButtonGroup(MainWindow)
        self.trustOtherRadio.setObjectName("trustOtherRadio")
        self.trustOtherRadio.addButton(self.trustOtherRadio_5)
        self.trustOtherRadio_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.trustOtherRadio_1.setGeometry(QtCore.QRect(240, 490, 21, 16))
        self.trustOtherRadio_1.setText("")
        self.trustOtherRadio_1.setObjectName("trustOtherRadio_1")
        self.trustOtherRadio.addButton(self.trustOtherRadio_1)
        self.trustOtherRadio_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.trustOtherRadio_2.setGeometry(QtCore.QRect(340, 490, 21, 16))
        self.trustOtherRadio_2.setText("")
        self.trustOtherRadio_2.setObjectName("trustOtherRadio_2")
        self.trustOtherRadio.addButton(self.trustOtherRadio_2)
        self.trustOtherRadio_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.trustOtherRadio_3.setGeometry(QtCore.QRect(440, 490, 21, 16))
        self.trustOtherRadio_3.setText("")
        self.trustOtherRadio_3.setObjectName("trustOtherRadio_3")
        self.trustOtherRadio.addButton(self.trustOtherRadio_3)
        self.trustOtherRadio_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.trustOtherRadio_4.setGeometry(QtCore.QRect(540, 490, 21, 16))
        self.trustOtherRadio_4.setText("")
        self.trustOtherRadio_4.setObjectName("trustOtherRadio_4")
        self.trustOtherRadio.addButton(self.trustOtherRadio_4)
        self.stressRadio_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.stressRadio_5.setGeometry(QtCore.QRect(640, 260, 21, 16))
        self.stressRadio_5.setText("")
        self.stressRadio_5.setObjectName("stressRadio_5")
        self.stressRadio = QtWidgets.QButtonGroup(MainWindow)
        self.stressRadio.setObjectName("stressRadio")
        self.stressRadio.addButton(self.stressRadio_5)
        self.stressRadio_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.stressRadio_1.setGeometry(QtCore.QRect(240, 260, 21, 16))
        self.stressRadio_1.setText("")
        self.stressRadio_1.setObjectName("stressRadio_1")
        self.stressRadio.addButton(self.stressRadio_1)
        self.stressRadio_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.stressRadio_2.setGeometry(QtCore.QRect(340, 260, 21, 16))
        self.stressRadio_2.setText("")
        self.stressRadio_2.setObjectName("stressRadio_2")
        self.stressRadio.addButton(self.stressRadio_2)
        self.stressRadio_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.stressRadio_3.setGeometry(QtCore.QRect(440, 260, 21, 16))
        self.stressRadio_3.setText("")
        self.stressRadio_3.setObjectName("stressRadio_3")
        self.stressRadio.addButton(self.stressRadio_3)
        self.stressRadio_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.stressRadio_4.setGeometry(QtCore.QRect(540, 260, 21, 16))
        self.stressRadio_4.setText("")
        self.stressRadio_4.setObjectName("stressRadio_4")
        self.stressRadio.addButton(self.stressRadio_4)
        self.fitRadio_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.fitRadio_5.setGeometry(QtCore.QRect(640, 190, 21, 16))
        self.fitRadio_5.setText("")
        self.fitRadio_5.setObjectName("fitRadio_5")
        self.fitRadio = QtWidgets.QButtonGroup(MainWindow)
        self.fitRadio.setObjectName("fitRadio")
        self.fitRadio.addButton(self.fitRadio_5)
        self.fitRadio_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.fitRadio_1.setGeometry(QtCore.QRect(240, 190, 21, 16))
        self.fitRadio_1.setText("")
        self.fitRadio_1.setObjectName("fitRadio_1")
        self.fitRadio.addButton(self.fitRadio_1)
        self.fitRadio_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.fitRadio_2.setGeometry(QtCore.QRect(340, 190, 21, 16))
        self.fitRadio_2.setText("")
        self.fitRadio_2.setObjectName("fitRadio_2")
        self.fitRadio.addButton(self.fitRadio_2)
        self.fitRadio_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.fitRadio_3.setGeometry(QtCore.QRect(440, 190, 21, 16))
        self.fitRadio_3.setText("")
        self.fitRadio_3.setObjectName("fitRadio_3")
        self.fitRadio.addButton(self.fitRadio_3)
        self.fitRadio_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.fitRadio_4.setGeometry(QtCore.QRect(540, 190, 21, 16))
        self.fitRadio_4.setText("")
        self.fitRadio_4.setObjectName("fitRadio_4")
        self.fitRadio.addButton(self.fitRadio_4)
        self.conditionRadio_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.conditionRadio_5.setGeometry(QtCore.QRect(640, 310, 21, 16))
        self.conditionRadio_5.setText("")
        self.conditionRadio_5.setObjectName("conditionRadio_5")
        self.conditionRadio = QtWidgets.QButtonGroup(MainWindow)
        self.conditionRadio.setObjectName("conditionRadio")
        self.conditionRadio.addButton(self.conditionRadio_5)
        self.conditionRadio_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.conditionRadio_1.setGeometry(QtCore.QRect(240, 310, 21, 16))
        self.conditionRadio_1.setText("")
        self.conditionRadio_1.setObjectName("conditionRadio_1")
        self.conditionRadio.addButton(self.conditionRadio_1)
        self.conditionRadio_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.conditionRadio_2.setGeometry(QtCore.QRect(340, 310, 21, 16))
        self.conditionRadio_2.setText("")
        self.conditionRadio_2.setObjectName("conditionRadio_2")
        self.conditionRadio.addButton(self.conditionRadio_2)
        self.conditionRadio_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.conditionRadio_3.setGeometry(QtCore.QRect(440, 310, 21, 16))
        self.conditionRadio_3.setText("")
        self.conditionRadio_3.setObjectName("conditionRadio_3")
        self.conditionRadio.addButton(self.conditionRadio_3)
        self.conditionRadio_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.conditionRadio_4.setGeometry(QtCore.QRect(540, 310, 21, 16))
        self.conditionRadio_4.setText("")
        self.conditionRadio_4.setObjectName("conditionRadio_4")
        self.conditionRadio.addButton(self.conditionRadio_4)
        self.concentrationRadio_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.concentrationRadio_5.setGeometry(QtCore.QRect(640, 360, 21, 16))
        self.concentrationRadio_5.setText("")
        self.concentrationRadio_5.setObjectName("concentrationRadio_5")
        self.concentrationRadio = QtWidgets.QButtonGroup(MainWindow)
        self.concentrationRadio.setObjectName("concentrationRadio")
        self.concentrationRadio.addButton(self.concentrationRadio_5)
        self.concentrationRadio_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.concentrationRadio_1.setGeometry(QtCore.QRect(240, 360, 21, 16))
        self.concentrationRadio_1.setText("")
        self.concentrationRadio_1.setObjectName("concentrationRadio_1")
        self.concentrationRadio.addButton(self.concentrationRadio_1)
        self.concentrationRadio_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.concentrationRadio_2.setGeometry(QtCore.QRect(340, 360, 21, 16))
        self.concentrationRadio_2.setText("")
        self.concentrationRadio_2.setObjectName("concentrationRadio_2")
        self.concentrationRadio.addButton(self.concentrationRadio_2)
        self.concentrationRadio_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.concentrationRadio_3.setGeometry(QtCore.QRect(440, 360, 21, 16))
        self.concentrationRadio_3.setText("")
        self.concentrationRadio_3.setObjectName("concentrationRadio_3")
        self.concentrationRadio.addButton(self.concentrationRadio_3)
        self.concentrationRadio_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.concentrationRadio_4.setGeometry(QtCore.QRect(540, 360, 21, 16))
        self.concentrationRadio_4.setText("")
        self.concentrationRadio_4.setObjectName("concentrationRadio_4")
        self.concentrationRadio.addButton(self.concentrationRadio_4)
        self.trustFromOtherRadio_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.trustFromOtherRadio_5.setGeometry(QtCore.QRect(640, 540, 21, 16))
        self.trustFromOtherRadio_5.setText("")
        self.trustFromOtherRadio_5.setObjectName("trustFromOtherRadio_5")
        self.trustFromOtherRadio = QtWidgets.QButtonGroup(MainWindow)
        self.trustFromOtherRadio.setObjectName("trustFromOtherRadio")
        self.trustFromOtherRadio.addButton(self.trustFromOtherRadio_5)
        self.trustFromOtherRadio_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.trustFromOtherRadio_1.setGeometry(QtCore.QRect(240, 540, 21, 16))
        self.trustFromOtherRadio_1.setText("")
        self.trustFromOtherRadio_1.setObjectName("trustFromOtherRadio_1")
        self.trustFromOtherRadio.addButton(self.trustFromOtherRadio_1)
        self.trustFromOtherRadio_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.trustFromOtherRadio_2.setGeometry(QtCore.QRect(340, 540, 21, 16))
        self.trustFromOtherRadio_2.setText("")
        self.trustFromOtherRadio_2.setObjectName("trustFromOtherRadio_2")
        self.trustFromOtherRadio.addButton(self.trustFromOtherRadio_2)
        self.trustFromOtherRadio_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.trustFromOtherRadio_3.setGeometry(QtCore.QRect(440, 540, 21, 16))
        self.trustFromOtherRadio_3.setText("")
        self.trustFromOtherRadio_3.setObjectName("trustFromOtherRadio_3")
        self.trustFromOtherRadio.addButton(self.trustFromOtherRadio_3)
        self.trustFromOtherRadio_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.trustFromOtherRadio_4.setGeometry(QtCore.QRect(540, 540, 21, 16))
        self.trustFromOtherRadio_4.setText("")
        self.trustFromOtherRadio_4.setObjectName("trustFromOtherRadio_4")
        self.trustFromOtherRadio.addButton(self.trustFromOtherRadio_4)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(230, 40, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(430, 40, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(330, 40, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(530, 40, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(630, 40, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(50, 50, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(40, 220, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(40, 400, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(230, 220, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(330, 220, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(430, 220, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(530, 220, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(630, 220, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(630, 400, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(530, 400, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(330, 400, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(230, 400, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(430, 400, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(219, 10, 441, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.sleepRadio_1.toggled['bool'].connect(MainWindow.r_buttonSlot1) # type: ignore
        self.mealRadio_1.toggled['bool'].connect(MainWindow.r_buttonSlot1) # type: ignore
        self.fitRadio_1.toggled['bool'].connect(MainWindow.r_buttonSlot1) # type: ignore
        self.stressRadio_1.toggled['bool'].connect(MainWindow.r_buttonSlot1) # type: ignore
        self.conditionRadio_1.toggled['bool'].connect(MainWindow.r_buttonSlot1) # type: ignore
        self.concentrationRadio_1.toggled['bool'].connect(MainWindow.r_buttonSlot1) # type: ignore
        self.trustMeRadio_1.toggled['bool'].connect(MainWindow.r_buttonSlot1) # type: ignore
        self.trustOtherRadio_1.toggled['bool'].connect(MainWindow.r_buttonSlot1) # type: ignore
        self.trustFromOtherRadio_1.toggled['bool'].connect(MainWindow.r_buttonSlot1) # type: ignore
        self.mealRadio_2.toggled['bool'].connect(MainWindow.r_buttonSlot2) # type: ignore
        self.sleepRadio_2.toggled['bool'].connect(MainWindow.r_buttonSlot2) # type: ignore
        self.fitRadio_2.toggled['bool'].connect(MainWindow.r_buttonSlot2) # type: ignore
        self.stressRadio_2.toggled['bool'].connect(MainWindow.r_buttonSlot2) # type: ignore
        self.conditionRadio_2.toggled['bool'].connect(MainWindow.r_buttonSlot2) # type: ignore
        self.concentrationRadio_2.toggled['bool'].connect(MainWindow.r_buttonSlot2) # type: ignore
        self.trustMeRadio_2.toggled['bool'].connect(MainWindow.r_buttonSlot2) # type: ignore
        self.trustOtherRadio_2.toggled['bool'].connect(MainWindow.r_buttonSlot2) # type: ignore
        self.trustFromOtherRadio_2.toggled['bool'].connect(MainWindow.r_buttonSlot2) # type: ignore
        self.sleepRadio_3.toggled['bool'].connect(MainWindow.r_buttonSlot3) # type: ignore
        self.mealRadio_3.toggled['bool'].connect(MainWindow.r_buttonSlot3) # type: ignore
        self.fitRadio_3.toggled['bool'].connect(MainWindow.r_buttonSlot3) # type: ignore
        self.stressRadio_3.toggled['bool'].connect(MainWindow.r_buttonSlot3) # type: ignore
        self.conditionRadio_3.toggled['bool'].connect(MainWindow.r_buttonSlot3) # type: ignore
        self.concentrationRadio_3.toggled['bool'].connect(MainWindow.r_buttonSlot3) # type: ignore
        self.trustMeRadio_3.toggled['bool'].connect(MainWindow.r_buttonSlot3) # type: ignore
        self.trustOtherRadio_3.toggled['bool'].connect(MainWindow.r_buttonSlot3) # type: ignore
        self.trustFromOtherRadio_3.toggled['bool'].connect(MainWindow.r_buttonSlot3) # type: ignore
        self.sleepRadio_4.toggled['bool'].connect(MainWindow.r_buttonSlot4) # type: ignore
        self.mealRadio_4.toggled['bool'].connect(MainWindow.r_buttonSlot4) # type: ignore
        self.fitRadio_4.toggled['bool'].connect(MainWindow.r_buttonSlot4) # type: ignore
        self.stressRadio_4.toggled['bool'].connect(MainWindow.r_buttonSlot4) # type: ignore
        self.conditionRadio_4.toggled['bool'].connect(MainWindow.r_buttonSlot4) # type: ignore
        self.concentrationRadio_4.toggled['bool'].connect(MainWindow.r_buttonSlot4) # type: ignore
        self.trustMeRadio_4.toggled['bool'].connect(MainWindow.r_buttonSlot4) # type: ignore
        self.trustOtherRadio_4.toggled['bool'].connect(MainWindow.r_buttonSlot4) # type: ignore
        self.trustFromOtherRadio_4.toggled['bool'].connect(MainWindow.r_buttonSlot4) # type: ignore
        self.sleepRadio_5.toggled['bool'].connect(MainWindow.r_buttonSlot5) # type: ignore
        self.mealRadio_5.toggled['bool'].connect(MainWindow.r_buttonSlot5) # type: ignore
        self.fitRadio_5.toggled['bool'].connect(MainWindow.r_buttonSlot5) # type: ignore
        self.stressRadio_5.toggled['bool'].connect(MainWindow.r_buttonSlot5) # type: ignore
        self.conditionRadio_5.toggled['bool'].connect(MainWindow.r_buttonSlot5) # type: ignore
        self.concentrationRadio_5.toggled['bool'].connect(MainWindow.r_buttonSlot5) # type: ignore
        self.trustMeRadio_5.toggled['bool'].connect(MainWindow.r_buttonSlot5) # type: ignore
        self.trustOtherRadio_5.toggled['bool'].connect(MainWindow.r_buttonSlot5) # type: ignore
        self.trustFromOtherRadio_5.toggled['bool'].connect(MainWindow.r_buttonSlot5) # type: ignore
        self.pushButton_Resist.pressed.connect(MainWindow.pushResistButtonSlot) # type: ignore
        self.pushButton_Past.pressed.connect(MainWindow.pushPastButtonSlot) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "セルフチェック トップ"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "予防・回復対処："))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", "備考："))
        self.pushButton_Past.setText(_translate("MainWindow", "過去のデータを見る"))
        self.pushButton_Resist.setText(_translate("MainWindow", "登録"))
        self.label_2.setText(_translate("MainWindow", "セルフチェック"))
        self.label.setText(_translate("MainWindow", "睡眠"))
        self.label_3.setText(_translate("MainWindow", "運動"))
        self.label_4.setText(_translate("MainWindow", "不安・ストレスがない"))
        self.label_5.setText(_translate("MainWindow", "身体の調子"))
        self.label_6.setText(_translate("MainWindow", "集中力"))
        self.label_7.setText(_translate("MainWindow", "自分を信頼"))
        self.label_8.setText(_translate("MainWindow", "他人を信頼"))
        self.label_9.setText(_translate("MainWindow", "他人から信頼"))
        self.label_10.setText(_translate("MainWindow", "食事"))
        self.label_11.setText(_translate("MainWindow", "1"))
        self.label_12.setText(_translate("MainWindow", "3"))
        self.label_13.setText(_translate("MainWindow", "2"))
        self.label_14.setText(_translate("MainWindow", "4"))
        self.label_15.setText(_translate("MainWindow", "5"))
        self.label_16.setText(_translate("MainWindow", "生活基盤"))
        self.label_17.setText(_translate("MainWindow", "心と体のサイン"))
        self.label_18.setText(_translate("MainWindow", "信頼のサイン"))
        self.label_19.setText(_translate("MainWindow", "1"))
        self.label_20.setText(_translate("MainWindow", "2"))
        self.label_21.setText(_translate("MainWindow", "3"))
        self.label_22.setText(_translate("MainWindow", "4"))
        self.label_23.setText(_translate("MainWindow", "5"))
        self.label_24.setText(_translate("MainWindow", "5"))
        self.label_25.setText(_translate("MainWindow", "4"))
        self.label_26.setText(_translate("MainWindow", "2"))
        self.label_27.setText(_translate("MainWindow", "1"))
        self.label_28.setText(_translate("MainWindow", "3"))
        self.label_29.setText(_translate("MainWindow", "低い　　　　　　　　　　　　　　　　　　　　　　　　高い"))
        self.menu.setTitle(_translate("MainWindow", "セルフチェック"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
