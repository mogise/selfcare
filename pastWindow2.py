# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pastWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

# 追加インポート
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import seaborn as sns
import pandas as pd
import datetime
import sip

FILE_PATH = 'test.csv' # 読み込むcsvファイル名
COLUMN_NUM = 4 # csvファイルのカラム数（dateを除く）
YEAR_LIST = ['2024', '2025', '2026']
MONTH_LIST = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']


class MatplotlibCanvas(FigureCanvasQTAgg):
    """MatplotLibグラフオブジェクトクラス
    """
    def __init__(self, parent=None, width=8, height=9, dpi=120):
        fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super(MatplotlibCanvas, self).__init__(fig)
        self.cmap = plt.get_cmap("tab10") # 色の種類 最大10色なので11項目以上はエラーになると思う

    def plot(self, df, columns, startDate, endDate):
        self.ax.clear()
        drawDf = df[startDate:endDate] # データ取得範囲を指定

        

        # 項目ごとにグラフ表示/非表示を切り替える
        t = 0
        bottom = 0
        for column in columns:
            self.ax.bar(drawDf.index, drawDf.iloc[:, t], bottom=bottom)
            bottom += drawDf.iloc[:, t]
            t += 1
            # if columns[column]:
            #     self.ax.plot(drawDf.index, drawDf[column], label=column, marker='o', color=self.cmap(t))
            # t += 1
        #self.ax.set_title('Title')
        #self.ax.set_xlabel('Date')
        #self.ax.set_ylabel('Value')
        self.ax.set_xlim([startDate, endDate]) # 描画範囲を指定

        title = startDate.strftime('%Y') + '  ' + startDate.strftime('%m/%d') + ' ~ ' + endDate.strftime('%m/%d')
        self.ax.set_title(title)
        
        # self.ax.set_yticks([1, 2, 3, 4, 5])
        self.ax.legend(title=drawDf.columns.name, prop = {'family': 'MS Gothic'})
        self.ax.grid(True)
        
        labels = self.ax.get_xticklabels()
        plt.setp(labels, rotation=45, fontsize=12)
        
        plt.subplots_adjust(bottom=0.2) # X軸ラベルが見切れるので調整


class Ui_MainWindow(object):
    """UIメインクラス
    """

    # ********************************
    # セットアップ関数
    # ********************************
    def setupUi(self, MainWindow):

        # グラフデータ関連の初期値
        self.canv = MatplotlibCanvas(self) # グラフを描画するキャンバスオブジェクト
        self.df = [] # csvのデータを格納するデータフレーム
        self.columns = {} # 項目別のグラフ表示/非表示を管理する


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 950)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 0, 1140, 900))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 270, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1260, 800, 262, 82))
        font = QtGui.QFont()
        font.setFamily("メイリオ")
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(1240, 40, 302, 302))
        # font = QtGui.QFont()
        # font.setFamily("メイリオ")
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(60, 60, 102, 62))
        # font = QtGui.QFont()
        # font.setFamily("メイリオ")
        font.setPointSize(9)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(60, 140, 102, 62))
        # font = QtGui.QFont()
        # font.setFamily("メイリオ")
        font.setPointSize(11)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_3.setGeometry(QtCore.QRect(60, 220, 102, 62))
        # font = QtGui.QFont()
        # font.setFamily("メイリオ")
        # font.setPointSize(11)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(180, 60, 62, 62))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(180, 140, 62, 62))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(180, 220, 62, 62))
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(1240, 360, 302, 402))
        # font = QtGui.QFont()
        # font.setFamily("メイリオ")
        # font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")

        # チェックボックスを配列で作成
        self.checkBoxes = []
        checkBoxSizeX = 182
        checkBoxSizeY = 62
        checkBoxBaseX = 30 # 1つめの位置
        checkBoxBaseY = 30 
        checkBoxSpaceY = 40 # 間隔
        # font = QtGui.QFont()
        # font.setFamily("メイリオ")
        font.setPointSize(9)
        for i in range(COLUMN_NUM):
            self.checkBoxes.append(QtWidgets.QCheckBox(self.groupBox_2)) # グループボックス内に配置する
            self.checkBoxes[i].setGeometry(QtCore.QRect(checkBoxBaseX, checkBoxBaseY+(checkBoxSpaceY * i), checkBoxSizeX, checkBoxSizeY))
            self.checkBoxes[i].setFont(font)
            self.checkBoxes[i].setChecked(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 42))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        # コンボボックスの初期設定
        today = datetime.date.today()
        self.comboWeekList = []
        self.comboBox.addItems(YEAR_LIST)
        self.comboBox_2.addItems(MONTH_LIST)
        # 初期値を今日の日付に合わせる
        self.comboBox_2.setCurrentIndex(today.month-1)
        self.comboBox_3.addItem('全て')
        self.calcComboValues()
        # 関数の関連付け
        self.comboBox.currentIndexChanged['QString'].connect(self.updateCombo_1_2)
        self.comboBox_2.currentIndexChanged['QString'].connect(self.updateCombo_1_2)
        self.comboBox_3.currentIndexChanged['QString'].connect(self.updateCombo_3)

        # チェックボックス関数の関連付け
        for i in range(COLUMN_NUM):
            self.checkBoxes[i].stateChanged.connect(self.updateChecks)
        

    # ********************************
    # 更新関数
    # ********************************
    def calcComboValues(self):
        """「表示する週」コンボボックスの選択肢を更新する関数
        """
        self.clearComboValues()
        self.comboWeekList = []
        year = int(self.comboBox.currentText())
        month = int(self.comboBox_2.currentText())
        tempDate = pd.Timestamp(year=year, month=month, day=1)
        count = 1
        while tempDate.month == month:
            self.comboWeekList.append(str(count))
            count += 1
            tempDate += pd.DateOffset(weeks=1)
        self.comboBox_3.addItems(self.comboWeekList)

        
    def clearComboValues(self):
        """「表示する週」コンボボックスから「全て」以外を削除する
        """
        self.comboBox_3.setCurrentIndex(0)
        t = self.comboBox_3.count()
        for _ in range(t):
            self.comboBox_3.removeItem(1)
        
        
    def updateCombo_1_2(self, value):
        """年または月を変更したとき
        """
        year = int(self.comboBox.currentText())
        month = int(self.comboBox_2.currentText())
        self.calcComboValues()

        # "全て" or "週ごと"
        if self.comboBox_3.currentIndex() == 0:
            dateRange = self.getMonthRange(year=year, month=month)
        else:
            week = int(self.comboBox_3.currentText())
            dateRange = self.getWeekRange(year=year, month=month, weekOfMonth=week)
        self.drawPlt(startDate=dateRange['startDate'], endDate=dateRange['endDate'])
        

    def updateCombo_3(self, value):
        """週を変更したとき
        """
        year = int(self.comboBox.currentText())
        month = int(self.comboBox_2.currentText())
        
        # "全て" or "週ごと"
        if self.comboBox_3.currentIndex() == 0:
            dateRange = self.getMonthRange(year=year, month=month)
        else:
            week = int(self.comboBox_3.currentText())
            dateRange = self.getWeekRange(year=year, month=month, weekOfMonth=week)
        self.drawPlt(startDate=dateRange['startDate'], endDate=dateRange['endDate'])


    def updateChecks(self, values):
        """チェックボックスを更新したとき
        """
        t = 0
        for col in self.columns:
            self.columns[col] = self.checkBoxes[t].isChecked()
            t += 1

        year = int(self.comboBox.currentText())
        month = int(self.comboBox_2.currentText())
        if self.comboBox_3.currentIndex() == 0:
            dateRange = self.getMonthRange(year=year, month=month)
        else:
            week = int(self.comboBox_3.currentText())
            dateRange = self.getWeekRange(year=year, month=month, weekOfMonth=week)

        self.drawPlt(startDate=dateRange['startDate'], endDate=dateRange['endDate'])


    # ********************************
    # グラフ描画関数
    # ********************************
    def drawPlt(self, startDate, endDate):
        """グラフ描画処理
        """
        # 描画クリア
        plt.close()
        try:
            self.verticalLayout.removeWidget(self.canv)
            sip.delete(self.canv)
            self.canv = None
        except Exception as e:
            print(e)
            pass
        
        # 再描画
        self.canv = MatplotlibCanvas(self)
        self.verticalLayout.addWidget(self.canv)
        self.canv.plot(df=self.df, columns=self.columns, startDate=startDate, endDate=endDate)
        self.canv.draw()

    def getWeekRange(self, year, month, weekOfMonth):
        """指定された週の範囲を取得する
        """
        # 月の初日
        firstDayOfMonth = pd.Timestamp(year=year, month=month, day=1)
        
        # 月の最初の月曜日を見つける
        firstMonday = firstDayOfMonth + pd.DateOffset(days=(0 - firstDayOfMonth.weekday()))

        # 指定された週の開始日と終了日
        startDate = firstMonday + pd.DateOffset(weeks=weekOfMonth-1)
        endDate = startDate + pd.DateOffset(days=6)
        
        return {'startDate':startDate, 'endDate':endDate}
    

    def getMonthRange(self, year, month):
        """指定された月の範囲を取得する
        """
        startDate = pd.Timestamp(year=year, month=month, day=1)
        endDate = pd.Timestamp(year=year, month=month, day=1) + pd.DateOffset(months=1, days=-1)
        
        return {'startDate':startDate, 'endDate':endDate}
    

    # ********************************
    # 初期化関数
    # ********************************  
    def readCsv(self, filePath):
        """csvファイル読み込み
        """
        self.df = pd.read_csv(filePath, encoding='utf-8', parse_dates=['date']).fillna(0)
        self.df.set_index('date', inplace=True)
        
    
    def getInitColumns(self):
        """カラム名を取得し初期値をセットする
        """
        keys = self.df.keys()
        t = 0
        for key in keys:
            self.columns[key] = True # 項目ごとのグラフ表示/非表示を設定する。初期値は全表示
            self.checkBoxes[t].setObjectName(key) # チェックボックスの内部名を設定する
            self.checkBoxes[t].setText(key) # チェックボックスの表示名を設定する
            t += 1
            
            
    def drawInitPlt(self):
        """初期グラフを今日の日付に合わせて表示する
        """
        today = datetime.date.today()
        dateRange = self.getMonthRange(year=today.year, month=today.month)
        self.drawPlt(startDate=dateRange['startDate'], endDate=dateRange['endDate'])
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "前の画面に戻る"))
        self.groupBox.setTitle(_translate("MainWindow", "表示する範囲"))
        self.label_2.setText(_translate("MainWindow", "年"))
        self.label_3.setText(_translate("MainWindow", "月"))
        self.label_4.setText(_translate("MainWindow", "週目"))
        self.groupBox_2.setTitle(_translate("MainWindow", "表示する項目"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    # 初期処理
    ui.readCsv(filePath=FILE_PATH)
    ui.getInitColumns()
    ui.drawInitPlt()

    sys.exit(app.exec_())
