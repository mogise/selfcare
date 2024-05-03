from PyQt5 import QtCore, QtGui, QtWidgets
import seaborn as sns
import pandas as pd
import datetime


class pastSubWindow(QtWidgets.QWidget):
  def __init__(self, parent=None, data=None):
    self.w = QtWidgets.QDialog(parent)
    self.w.resize(800, 1000)

    self.labelFont = QtGui.QFont()
    self.labelFont.setFamily("メイリオ")
    self.labelFont.setPointSize(12)

    date = data['date']
    strDate = date.strftime('%Y/%m/%d')

    self.title = self.makeLabel(strDate + ' のセルフチェック記録', None, 50, 10)
    self.cat_1 = self.makeLabel('【生活基盤】', None, 50, 100)
    self.cat_2 = self.makeLabel('【心と体のサイン】', None, 50, 300)
    self.cat_3 = self.makeLabel('【信頼のサイン】', None, 50, 500)
    self.cat_4 = self.makeLabel('【予防・回復対処】', None, 50, 700)
    self.cat_5 = self.makeLabel('【気付き・備考】', None, 400, 700)

    self.labelFont.setPointSize(11)
    self.cat_1_1 = self.makeLabel('睡眠', str(data['data']['睡眠']), 70, 150)

  def show(self):
    self.w.exec_()


  def makeLabel(self, title, content, pos_x, pos_y):
    """ラベルを作成する関数
    """
    label = QtWidgets.QLabel(self.w)
    label.setGeometry(QtCore.QRect(pos_x, pos_y, 400, 80))
    label.setFont(self.labelFont)
    # label.setObjectName('label_' + str(id))
    if content == None:
      label.setText(title)
    else:
      label.setText(title + ': ' + content)

    return label