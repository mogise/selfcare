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
import matplotlib.dates as mdates
matplotlib.use('Qt5Agg')
from PyQt5.QtWidgets import QFileDialog
from matplotlib.dates import date2num, num2date
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
        self.cmap = plt.get_cmap("tab20") # 色の種類 最大10色なので11項目以上はエラーになると思う

    def plot(self, df, columns, startDate, endDate, rangeMode, mode):
        self.ax.clear()
        self.ax.grid(True)
        self.ax.set_axisbelow(True)
        dw=0.2 # 横並びのときの棒の幅

        drawDf = df[startDate:endDate] # データ取得範囲を指定

        # タイトルを設定
        title = startDate.strftime('%Y') + '  ' + startDate.strftime('%m/%d') + ' ~ ' + endDate.strftime('%m/%d')
        self.ax.set_title(title)

        # 月表示なら積み上げ、週表示なら横並びの棒グラフ
        if(rangeMode == 'month'):
            bottom = 0
            for i in range(mode, mode+3):
                self.ax.bar(drawDf.index, drawDf.iloc[:, i], bottom=bottom, label=columns[i], color=self.cmap(mode+i))
                bottom += drawDf.iloc[:, i]
        else:
            # 各日について3つの項目の棒グラフを並べる。2つ目の棒を中心にとる
            for i in range(mode, mode+3):
                x = date2num(drawDf.index)
                self.ax.bar(align='center', x=x+dw*((i%3)-1), width=dw, height=drawDf[columns[i]], label=columns[i], color=self.cmap(mode+i))

        # グラフの描画範囲を設定
        # そのままだと端が見切れてしまうので、オフセットを設ける）
        xLimStart = num2date(date2num(startDate) - 0.5)
        xLimEnd = num2date(date2num(endDate) + 0.5)
        self.ax.set_xlim([xLimStart, xLimEnd]) # 描画範囲を指定

        #凡例の設定
        self.ax.legend(prop = {'family': 'MS Gothic'}, loc="upper center", ncol=4)
        
        # 目盛の設定
        self.ax.xaxis.set_major_locator(mdates.DayLocator())
        labels = self.ax.get_xticklabels()
        plt.setp(labels, rotation=90, fontsize=9)
        
        plt.subplots_adjust(bottom=0.2) # X軸ラベルが見切れるので調整


class Ui_MainWindow(QtWidgets.QWidget):
    """UIメインクラス
    """

    # ********************************
    # セットアップ関数
    # ********************************
    def setupUi(self, MainWindow):

        # グラフデータ関連の初期値
        self.canv = MatplotlibCanvas(self) # グラフを描画するキャンバスオブジェクト
        self.df = [] # csvのデータを格納するデータフレーム
        self.columns = [] # 項目別のグラフ表示/非表示を管理する
        self.mode = 0 # 表示する大項目の切り替え。mode=0なら生活基盤、3なら心と体、6なら信頼
        self.rangeMode = 'month' # 月表示か週表示か

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 950)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 0, 1100, 900))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 270, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1230, 820, 260, 80))
        font = QtGui.QFont()
        font.setFamily("メイリオ")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(1160, 40, 400, 120))
        # font = QtGui.QFont()
        # font.setFamily("メイリオ")
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(30, 40, 80, 60))
        # font = QtGui.QFont()
        # font.setFamily("メイリオ")
        font.setPointSize(9)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 40, 70, 60))
        # font = QtGui.QFont()
        # font.setFamily("メイリオ")
        font.setPointSize(11)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_3.setGeometry(QtCore.QRect(260, 40, 80, 60))
        # font = QtGui.QFont()
        # font.setFamily("メイリオ")
        # font.setPointSize(11)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(110, 40, 60, 60))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(220, 40, 60, 60))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(340, 40, 60, 60))
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(1160, 180, 400, 190))
        # font = QtGui.QFont()
        # font.setFamily("メイリオ")
        # font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        
        
        self.radioBtn_1 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioBtn_1.setGeometry(QtCore.QRect(30, 30, 190, 70))
        self.radioBtn_1.setFont(font)
        self.radioBtn_1.setChecked(True)
        
        self.radioBtn_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioBtn_2.setGeometry(QtCore.QRect(30, 70, 190, 70))
        self.radioBtn_2.setFont(font)
        
        self.radioBtn_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioBtn_3.setGeometry(QtCore.QRect(30, 110, 190, 70))
        self.radioBtn_3.setFont(font)


        # カレンダー
        self.calendar = QtWidgets.QCalendarWidget(MainWindow)
        self.calendar.setGeometry(QtCore.QRect(1160, 400, 400, 350))
        self.calendar.setGridVisible(True)
        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)


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
        
        
        self.radioBtn_1.toggled.connect(self.updateRadio)
        self.radioBtn_2.toggled.connect(self.updateRadio)
        self.radioBtn_3.toggled.connect(self.updateRadio)

        

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
        self.changeCalView()
        

    def updateCombo_3(self, value):
        """週を変更したとき
        """
        year = int(self.comboBox.currentText())
        month = int(self.comboBox_2.currentText())
        
        # "全て" or "週ごと"
        if self.comboBox_3.currentIndex() == 0:
            dateRange = self.getMonthRange(year=year, month=month)
            self.rangeMode = 'month'
        else:
            week = int(self.comboBox_3.currentText())
            dateRange = self.getWeekRange(year=year, month=month, weekOfMonth=week)
            self.rangeMode = 'week'
        self.drawPlt(startDate=dateRange['startDate'], endDate=dateRange['endDate'])
        
        
    def updateRadio(self, values):
        """ラジオボタンを更新したとき
        """
        radioBtn = self.sender()
        if radioBtn is None or not isinstance(radioBtn, QtWidgets.QRadioButton):
            return
        txt = radioBtn.text()
        if txt == '生活基盤':
            self.mode = 0
        elif txt == '心と体のサイン':
            self.mode = 3
        elif txt == '信頼のサイン':
            self.mode = 6
            
        year = int(self.comboBox.currentText())
        month = int(self.comboBox_2.currentText())
            
        # "全て" or "週ごと"
        if self.comboBox_3.currentIndex() == 0:
            dateRange = self.getMonthRange(year=year, month=month)
            self.rangeMode = 'month'
        else:
            week = int(self.comboBox_3.currentText())
            dateRange = self.getWeekRange(year=year, month=month, weekOfMonth=week)
            self.rangeMode = 'week'
        self.drawPlt(startDate=dateRange['startDate'], endDate=dateRange['endDate'])

    def changeCalView(self):
        year = int(self.comboBox.currentText())
        month = int(self.comboBox_2.currentText())
        self.calendar.setCurrentPage(year, month)

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
        self.canv.plot(df=self.df, columns=self.columns, startDate=startDate, endDate=endDate, rangeMode=self.rangeMode, mode=self.mode)
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
        for key in keys:
            self.columns.append(key) # グラフの項目名を追加する
            
            
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
        self.radioBtn_1.setText(_translate("MainWindow", "生活基盤"))
        self.radioBtn_2.setText(_translate("MainWindow", "心と体のサイン"))
        self.radioBtn_3.setText(_translate("MainWindow", "信頼のサイン"))
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
