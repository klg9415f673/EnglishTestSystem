import random
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
import os
from CSVProcess import CSVProcess
import mainwindows as ui
import MID


class MainWindow(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        # 綁定按鈕的事件處理
        self.Manual.triggered.connect(self.Import_Manual)        
        self.Excel.triggered.connect(self.Import_Excel)
        self.StartButton.clicked.connect(self.start) 
        self.CheckButton.setEnabled(False)
        self.CheckButton.clicked.connect(self.check)    
        self.RecordButton.clicked.connect(self.record)         
        self.RecordButton.setEnabled(False)       
        self.CloseButton.clicked.connect(self.close)# 並非綁定closeEvent而是綁定close
        self.Qlabel.setText('請按下Start開始測驗') 
        self.show()
        if os.path.isfile("Record.csv"):
            os.remove("Record.csv") 

    def closeEvent(self, event):  # 一定要叫closeEvent才會對應到self.close
        print('exit')
        reply = QMessageBox.question(self, 'Message', 'You sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 

    
    def start(self):
        global count
        if self.StartButton.text()== 'Start':
            print('start')           
            self.StartButton.setText('Next')   
            self.CheckButton.setEnabled(True) 
            count = 0
              
        else:
            print('next')
            count += 1
                    
        r_num = random.randint(0,len(dataset)-1-count) # 降低避免重複選擇單字功能的複雜度       
        index_voc = dataset.index(dataset[r_num])
        global vocabulary
        vocabulary = dataset.pop(index_voc) # 將測驗的單字取出
        dataset.append(vocabulary) # 再將取出的單字放到list最後一個
        print(dataset)
        EorC = random.randint(0,1)
        self.Alabel.setText('')        
        self.Qlabel.setText(vocabulary[EorC])             
        self.wordlabel.setText(vocabulary[2])  
        global checknum
        if EorC !=0:
            checknum = 0
        else:
            checknum = 1
        

    def check(self):
        print('check')
        self.Alabel.setText(vocabulary[checknum])                             
        self.RecordButton.setEnabled(True)

    def record(self):              
        print('record')           
        self.RecordButton.setEnabled(False)  
        CSV = CSVProcess("Record.csv")
        CSV.Write_csv([vocabulary])   
    
    def Import_Excel(self):
        print('Import Excel')

        ImportCSV, filetype = QFileDialog.getOpenFileName(self,
        "選取檔案",
        "./",
        "All Files (*);;Text Files (*.csv)")

        export_csv = CSVProcess(ImportCSV) #要新增的
        export_dataset = export_csv.Read_csv()

        import_csv =  CSVProcess()#被新增的
        import_csv.Write_csv(export_dataset)  

        reply = QMessageBox.question(self, 'Message', '請重開程式，以便讀取新的單字',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes :
            python = sys.executable
            os.execl(python, python, * sys.argv)
            


    
    def Import_Manual(self):
        print('Import Manual')
        dialog.show()




if __name__ == '__main__':    
    
    global dataset    
    test_CSV = CSVProcess() 
    dataset = test_CSV.Read_csv()
    app = QtWidgets.QApplication(sys.argv)

    global dialog
    dialog = MID.Dialog()
    
    window = MainWindow()
    sys.exit(app.exec_())