from PyQt5 import QtCore, QtGui, QtWidgets
import seaborn as sns
import pandas as pd
import datetime


class pastSubWindow(QtWidgets.QWidget):
  def __init__(self, parent=None, data=None):
    self.w = QtWidgets.QDialog(parent)
    self.w.resize(800, 700)
    self.w.setWindowTitle("セルフチェック 過去の記録-詳細")

    self.labelFont = QtGui.QFont()
    self.labelFont.setFamily("メイリオ")
    self.labelFont.setPointSize(16)
    self.labelFont.setBold(True)

    date = data['date']
    strDate = date.strftime('%Y/%m/%d')

    self.title = self.makeLabel(strDate + ' のセルフチェック記録', None, 50, 20)
    
    self.labelFont.setPointSize(12)
    self.cat_1 = self.makeLabel('【生活基盤】', None, 50, 100)
    self.cat_2 = self.makeLabel('【心と体のサイン】', None, 250, 100)
    self.cat_3 = self.makeLabel('【信頼のサイン】', None, 520, 100)
    self.cat_4 = self.makeLabel('【予防・回復対処】', None, 50, 350)
    self.cat_5 = self.makeLabel('【気付き・備考】', None, 400, 350)

    self.labelFont.setBold(False)
    self.labelFont.setPointSize(11)
    self.cat_1_1 = self.makeLabel('睡眠', str(data['data']['睡眠']), 70, 150)
    self.cat_1_2 = self.makeLabel('食事', str(data['data']['食事']), 70, 200)
    self.cat_1_3 = self.makeLabel('運動', str(data['data']['運動']), 70, 250)
    self.cat_2_1 = self.makeLabel('不安・ストレスが無い', str(data['data']['不安・ストレス']), 270, 150)
    self.cat_2_2 = self.makeLabel('身体の調子', str(data['data']['身体の調子']), 270, 200)
    self.cat_2_3 = self.makeLabel('集中力が高い', str(data['data']['集中力']), 270, 250)
    self.cat_3_1 = self.makeLabel('自分を信頼', str(data['data']['自分を信頼']), 540, 150)
    self.cat_3_2 = self.makeLabel('他人を信頼', str(data['data']['他人を信頼']), 540, 200)
    self.cat_3_3 = self.makeLabel('他人から信頼', str(data['data']['他人から信頼']), 540, 250)
    
    self.cat_4_s = self.makeTextbox(data['data']['予防・回復対処'], 70, 400)
    self.cat_5_s = self.makeTextbox(data['data']['備考'], 420, 400)

  def show(self):
    self.w.exec_()


  def makeLabel(self, title, content, pos_x, pos_y):
    """ラベルを作成する関数
    """
    label = QtWidgets.QLabel(self.w)
    label.setGeometry(QtCore.QRect(pos_x, pos_y, 600, 80))
    label.setFont(self.labelFont)
    # label.setObjectName('label_' + str(id))
    if content == None:
      label.setText(title)
    else:
      label.setText(title + ': ' + content)
      
    return label
  
  def makeTextbox(self, content, pos_x, pos_y):
    """テキストボックスを作成する関数
    """
    tbox = QtWidgets.QTextEdit(self.w)
    tbox.setGeometry(QtCore.QRect(pos_x, pos_y, 300, 250))
    tbox.insertPlainText(content if content!=0 else "なし") # 記載なしのとき0が入力されるので、変換する
    tbox.setReadOnly(True)

    return tbox