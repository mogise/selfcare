from PyQt5.QtWidgets import QButtonGroup, QMainWindow

from topWindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # UIオブジェクトを作成
        self.ui.setupUi(self)  # UIをセットアップ

        # ラジオボタングループを作成
        #睡眠のラジオボタン
        self.sleepRadio = QButtonGroup(self)  
        self.sleepRadio(self.ui.sleepRadio_1)
        self.sleepRadio(self.ui.sleepRadio_2)
        self.sleepRadio(self.ui.sleepRadio_3)
        self.sleepRadio(self.ui.sleepRadio_4)
        self.sleepRadio(self.ui.sleepRadio_5)
        # ボタンが選択されたときの処理を接続
        self.sleep=self.sleepRadio.buttonToggled.connect(self.on_sleepRadio_toggled)
        
        #食事のラジオボタン
        self.mealRadio = QButtonGroup(self)  
        self.mealRadio(self.ui.mealRadio_1)
        self.mealRadio(self.ui.mealRadio_2)
        self.mealRadio(self.ui.mealRadio_3)
        self.mealRadio(self.ui.mealRadio_4)
        self.mealRadio(self.ui.mealRadio_5)
        # ボタンが選択されたときの処理を接続
        self.meal=self.mealRadio.buttonToggled.connect(self.on_mealRadio_toggled)   
        
        #運動のラジオボタン
        self.fitRadio = QButtonGroup(self)  
        self.fitRadio(self.ui.fitRadio_1)
        self.fitRadio(self.ui.fitRadio_2)
        self.fitRadio(self.ui.fitRadio_3)
        self.fitRadio(self.ui.fitRadio_4)
        self.fitRadio(self.ui.fitRadio_5)
        # ボタンが選択されたときの処理を接続
        self.fit=self.fitRadio.buttonToggled.connect(self.on_fitRadio_toggled)      
        
        #ストレスのラジオボタン
        self.stressRadio = QButtonGroup(self)  
        self.stressRadio(self.ui.stressRadio_1)
        self.stressRadio(self.ui.stressRadio_2)
        self.stressRadio(self.ui.stressRadio_3)
        self.stressRadio(self.ui.stressRadio_4)
        self.stressRadio(self.ui.stressRadio_5)
        # ボタンが選択されたときの処理を接続
        self.stress=self.stressRadio.buttonToggled.connect(self.on_stressRadio_toggled)      
        
        #身体の調子のラジオボタン
        self.conditionRadio = QButtonGroup(self)  
        self.conditionRadio(self.ui.conditionRadio_1)
        self.conditionRadio(self.ui.conditionRadio_2)
        self.conditionRadio(self.ui.conditionRadio_3)
        self.conditionRadio(self.ui.conditionRadio_4)
        self.conditionRadio(self.ui.conditionRadio_5)
        # ボタンが選択されたときの処理を接続
        self.condition=self.conditionRadio.buttonToggled.connect(self.on_conditionRadio_toggled)     
        
        #集中力のラジオボタン
        self.concentrationRadio = QButtonGroup(self)  
        self.concentrationRadio(self.ui.concentrationRadio_1)
        self.concentrationRadio(self.ui.concentrationRadio_2)
        self.concentrationRadio(self.ui.concentrationRadio_3)
        self.concentrationRadio(self.ui.concentrationRadio_4)
        self.concentrationRadio(self.ui.concentrationRadio_5)
        # ボタンが選択されたときの処理を接続
        self.concentration=self.concentrationRadio.buttonToggled.connect(self.on_concentrationRadio_toggled)     
        
        #自分を信頼のラジオボタン
        self.trustMeRadio = QButtonGroup(self)  
        self.trustMeRadio(self.ui.trustMeRadio_1)
        self.trustMeRadio(self.ui.trustMeRadio_2)
        self.trustMeRadio(self.ui.trustMeRadio_3)
        self.trustMeRadio(self.ui.trustMeRadio_4)
        self.trustMeRadio(self.ui.trustMeRadio_5)
        # ボタンが選択されたときの処理を接続
        self.trustMe=self.trustMeRadio.buttonToggled.connect(self.on_trustMeRadio_toggled)     
        
        #他人を信頼のラジオボタン
        self.trustOtherRadio = QButtonGroup(self)  
        self.trustOtherRadio(self.ui.trustOtherRadio_1)
        self.trustOtherRadio(self.ui.trustOtherRadio_2)
        self.trustOtherRadio(self.ui.trustOtherRadio_3)
        self.trustOtherRadio(self.ui.trustOtherRadio_4)
        self.trustOtherRadio(self.ui.trustOtherRadio_5)
        # ボタンが選択されたときの処理を接続
        self.trustOther=self.trustOtherRadio.buttonToggled.connect(self.on_trustOtherRadio_toggled)     
        
        #他人から信頼のラジオボタン
        self.trustFromOtherRadio = QButtonGroup(self)  
        self.trustFromOtherRadio(self.ui.trustFromOtherRadio_1)
        self.trustFromOtherRadio(self.ui.trustFromOtherRadio_2)
        self.trustFromOtherRadio(self.ui.trustFromOtherRadio_3)
        self.trustFromOtherRadio(self.ui.trustFromOtherRadio_4)
        self.trustFromOtherRadio(self.ui.trustFromOtherRadio_5)
        # ボタンが選択されたときの処理を接続
        self.trustFromOther=self.trustFromOtherRadio.buttonToggled.connect(self.on_trustFromOtherRadio_toggled)    

        def on_sleepRadio_toggled(self,button,checked):
            if checked:
                if button == self.ui.sleepRadio_1:
                    return 1
                if button == self.ui.sleepRadio_2:
                    return 2
                if button == self.ui.sleepRadio_3:
                    return 3
                if button == self.ui.sleepRadio_4:
                    return 4
                if button == self.ui.sleepRadio_5:
                    return 5

        def on_mealRadio_toggled(self,button,checked):
            if checked:
                if button == self.ui.mealRadio_1:
                    return 1
                if button == self.ui.mealRadio_2:
                    return 2
                if button == self.ui.mealRadio_3:
                    return 3
                if button == self.ui.mealRadio_4:
                    return 4
                if button == self.ui.mealRadio_5:
                    return 5
                    
        def on_fitRadio_toggled(self,button,checked):
            if checked:
                if button == self.ui.fitRadio_1:
                    return 1
                if button == self.ui.fitRadio_2:
                    return 2
                if button == self.ui.fitRadio_3:
                    return 3
                if button == self.ui.fitRadio_4:
                    return 4
                if button == self.ui.fitRadio_5:
                    return 5
        def on_stressRadio_toggled(self,button,checked):
            if checked:
                if button == self.ui.sleepRadio_1:
                    return 1
                if button == self.ui.sleepRadio_2:
                    return 2
                if button == self.ui.sleepRadio_3:
                    return 3
                if button == self.ui.sleepRadio_4:
                    return 4
                if button == self.ui.sleepRadio_5:
                    return 5

        def on_conditionRadio_toggled(self,button,checked):
            if checked:    
                if button == self.ui.sleepRadio_1:
                    return 1
                if button == self.ui.sleepRadio_2:
                    return 2
                if button == self.ui.sleepRadio_3:
                    return 3
                if button == self.ui.sleepRadio_4:
                    return 4
                if button == self.ui.sleepRadio_5:
                    return 5

        def on_concentrationRadio_toggled(self,button,checked):
            if checked:
                if button == self.ui.sleepRadio_1:
                    return 1
                if button == self.ui.sleepRadio_2:
                    return 2
                if button == self.ui.sleepRadio_3:
                    return 3
                if button == self.ui.sleepRadio_4:
                    return 4
                if button == self.ui.sleepRadio_5:
                    return 5

        def on_trustMeRadio_toggled(self,button,checked):
            if checked:
                if button == self.ui.sleepRadio_1:
                    return 1
                if button == self.ui.sleepRadio_2:
                    return 2
                if button == self.ui.sleepRadio_3:
                    return 3
                if button == self.ui.sleepRadio_4:
                    return 4
                if button == self.ui.sleepRadio_5:
                    return 5

        def on_trustOtherRadio_toggled(self,button,checked):
            if checked:
                if button == self.ui.sleepRadio_1:
                    return 1
                if button == self.ui.sleepRadio_2:
                    return 2
                if button == self.ui.sleepRadio_3:
                    return 3
                if button == self.ui.sleepRadio_4:
                    return 4
                if button == self.ui.sleepRadio_5:
                    return 5

        def on_trustFromOtherRadio_toggled(self,button,checked):
            if checked:
                if button == self.ui.sleepRadio_1:
                    return 1
                if button == self.ui.sleepRadio_2:
                    return 2
                if button == self.ui.sleepRadio_3:
                    return 3
                if button == self.ui.sleepRadio_4:
                    return 4
                if button == self.ui.sleepRadio_5:
                    return 5
    
            
    def r_buttonSlot1(elem):
        elem = 1
        return elem
    def r_buttonSlot2(elem):
        elem = 2
        return elem
    def r_buttonSlot3(elem):
        elem = 3
        return elem
    def r_buttonSlot4(elem):
        elem = 4
        return elem
    def r_buttonSlot5(elem):
        elem = 5
        return elem
