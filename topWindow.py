# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'topWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

# ***** 追加インポート5/8 山本
import csv
import datetime
# ***** 追加 5/10 山本
# ***** pastWinow改修にともなう編集 5/15 寺島
# import pastWindow2
from pastWindow import pastWindow

class Ui_MainWindow(object):
    #data={'sleep':3,'meal':3,'fit':3,'stress':3,'condition':3,'concentration':3,'trustMe':3,'trustOther':3,'trustFromOther':3}
    def setupUi(self, MainWindow):

        fontSize_lg = 15
        fontSize_md = 10
        fontSize_sm = 11

        labelSize_lg = {'x':400 , 'y':30}
        labelSize_md = {'x':200 , 'y':30}
        labelSize_sm = {'x':120 , 'y':20}

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 840)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 630, 351, 91))
        font = QtGui.QFont()
        font.setPointSize(fontSize_sm)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(410, 630, 351, 91))
        font = QtGui.QFont()
        font.setPointSize(fontSize_sm)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.pushButton_Past = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Past.setGeometry(QtCore.QRect(120, 740, 181, 40))   #配置変更 5/8 山本
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Past.setFont(font)
        self.pushButton_Past.setObjectName("pushButton_Past")
        self.pushButton_Past.clicked.connect(self.pushPastButtonSlot)
        self.pushButton_Resist = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Resist.setGeometry(QtCore.QRect(500, 740, 181, 40)) #配置変更 5/8 山本
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Resist.setFont(font)
        self.pushButton_Resist.setObjectName("pushButton_Resist")
        self.pushButton_Resist.clicked.connect(self.pushResistButtonSlot)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 300, 31))
        font = QtGui.QFont()
        font.setPointSize(fontSize_lg)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 90, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 190, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 270, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 320, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 370, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 450, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(110, 500, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(100, 550, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(150, 140, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")


        # ***** ラジオボタン設置処理 2024/05/03 寺島
        
        radioBasePosX = 235 # 左端のラジオボタンのx座標
        radioBasePosY = 90 # 最初の項目のラジオボタンのy座標
        dY = 0 # y座標の位置調整用
        
        # 各項目について、5つのラジオボタンをグループ化する
        self.groupNameList = ['sleep', 'meal','fit','stress','condition','concentration','trustMe','trustOther','trustFromOther']
        self.radioGroupDict = {} # 各グループを参照しやすいように、まとめて辞書化する
        # ⇒これにより、self.radioGroups[self.groupNameList[n]] で項目ごとのボタングループを参照できる
        

        # 外側のループ: 各項目についてのループ
        for i in range(9): 
            self.radioGroupDict[self.groupNameList[i]] = QtWidgets.QButtonGroup(MainWindow) # ボタングループの辞書に空のグループを作成
            a = QtWidgets.QButtonGroup(MainWindow)
            
            # 内側のループ: 5つのラジオボタンを配置する
            for j in range(5):
                objectName = self.groupNameList[i] + '_' + str(j+1)
                posX = radioBasePosX + (100 * j)
                posY = radioBasePosY + dY
                val = j+1 # j番目のラジオボタンの内部値(id)はj+1
                
                radio = self.makeRadio(objectName, posX, posY) # ラジオボタン作成
                
                if j == 2:
                    radio.setChecked(True) # 初期状態では3にチェックをつけておく
                
                self.radioGroupDict[self.groupNameList[i]].addButton(radio, val) # 作成したラジオボタンをグループに追加
                
            dY += 50 # 次の項目へ移動するため、y座標を下げる
            
            if (i+1)%3 == 0:
                dY += 30 # 3項目ごとに次の大項目へ移動するため、さらにy座標を少し下げる
                

        # ***** ラジオボタン設置ここまで



        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(230, 50, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(430, 50, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(330, 50, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(530, 50, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(630, 50, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(30, 50, 300, 31))
        font = QtGui.QFont()
        font.setPointSize(fontSize_lg)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(10, 220, 300, 31))
        font = QtGui.QFont()
        font.setPointSize(fontSize_lg)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(10, 410, 300, 31))
        font = QtGui.QFont()
        font.setPointSize(fontSize_lg)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(230, 230, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(330, 230, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(430, 230, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(530, 230, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(630, 230, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(630, 410, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(530, 410, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(330, 410, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(230, 410, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(430, 410, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(219, 10, 441, 20))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignLeft)
        self.label_29.setObjectName("label_29")
        # ***** ラベル追加 5/13 山本
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(20, 600, 140, 20))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignTop)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(410, 600, 24, 20))
        font = QtGui.QFont()
        font.setPointSize(fontSize_md)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignTop)
        self.label_31.setObjectName("label_31")
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "セルフチェック トップ"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", ""))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", ""))
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
        self.label_29.setText(_translate("MainWindow", "低い　　　　　　　　　　　　　　　　　　　　　　　  　 高い"))
        self.label_30.setText(_translate("MainWindow", "予防・回復対処"))
        self.label_31.setText(_translate("MainWindow", "備考"))
        self.menu.setTitle(_translate("MainWindow", "セルフチェック"))



    # ***** ラジオボタン関係の関数 2024/05/06 寺島
    
    def makeRadio(self, objectName, pos_x, pos_y):
        size_x = 20
        size_y = 20
        
        radio = QtWidgets.QRadioButton("", self.centralwidget)
        radio.setObjectName(objectName)
        radio.setGeometry(QtCore.QRect(pos_x, pos_y, size_x, size_y))
        
        return radio
    
    # ***** ラジオボタン関連の関数ここまで
    
    
    # ***** 「登録」ボタン押下時処理 5/8 山本
    # *****              編集・追記 5/9 山本
    # *****              編集・追記 5/10 山本
    # ***** 　　　　　　　編集・追記 5/16 寺島
    def pushResistButtonSlot(self):
        FILE_PATH = 'data.csv' # 読み込むcsvファイル名
        #データをリストとしてまとめる
        data_to_write = [str(datetime.date.today())]#タイムスタンプ(date)を追加
        
        #各ラジオボタンの値を追加
        for name in self.groupNameList:
            val = self.radioGroupDict[name].checkedId()
            data_to_write.append(str(val))
            
        #テキストエディタの内容を追加
        notes = self.plainTextEdit.toPlainText().replace(",", "、")
        notes2 = self.plainTextEdit_2.toPlainText().replace(",", "、")
        #リストに追加
        data_to_write.append(notes)
        data_to_write.append(notes2)
        
        # csvにリスト内のデータを書き込む
        with open(FILE_PATH,'a',encoding='utf-8') as f:# 現状とりあえずtest.csvで設定してあります。
                            #'a'で追記(append)モード。
            writer = csv.writer(f)
            writer.writerow(data_to_write)
            # ***** 完了の旨のメッセージボックスを表示 5/10 山本
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Information)
            msg_box.setText('登録完了')
            msg_box.setInformativeText('本日のセルフチェックの登録が完了しました。')
            msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
            # メッセージボックスを表示
            msg_box.exec_()
    # ***** 「登録」ボタン押下時処理 ここまで

    
    # ***** 「過去のデータを見る」ボタン押下時処理 5/10 山本
    # *****                     機能実装        5/13 山本 
    # ***** pastWinodw改修にともなう編集　　　　　5/15 寺島
    def pushPastButtonSlot(self):
        self.pWindow = pastWindow()
        self.pWindow.show()
    # ***** 「過去のデータを見る」ボタン押下時処理 ここまで
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
