import random
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
import os
from CSVProcess import CSVProcess
import MIDwindows as MID

class Dialog(QDialog,MID.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.get_voc)

    def get_voc(self):
        if self.lineEdit.text() == "":
            QMessageBox.question(self, 'Message', "Please Enter vocabulary",
                                QMessageBox.Ok , QMessageBox.Ok)
        elif self.lineEdit_2.text() =="":
            QMessageBox.question(self, 'Message', "Please Enter vocabulary's Explanation",
                                QMessageBox.Ok , QMessageBox.Ok)
        else:
            msg = 'Sure to add %s %s %s ?' % (self.lineEdit.text(), self.comboBox.currentText(), self.lineEdit_2.text())
            reply = QMessageBox.question(self, 'Message', msg,
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            
            if reply == QMessageBox.Yes:
                import_csv =  CSVProcess()
                data =  [self.lineEdit.text(), self.lineEdit_2.text(), self.comboBox.currentText()]
                import_csv.Write_csv([data]) 
        
        




if __name__ == '__main__':    
    
  
    app = QtWidgets.QApplication(sys.argv)
    
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())