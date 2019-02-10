import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *

class MyMainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,500,300)
        self.setWindowTitle('My Main Window')
        self.label = QLabel("cliquer pour quitter")
        self.plain = QTextEdit()
        self.textbox = QLineEdit()
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
        self.textbox.text() ;
        self.bu = QPushButton("Go...")
        self.bu.clicked.connect(self.on_click)
        #self.bu.clicked.connect(self.DisplayMessage)
        layout = QVBoxLayout(self)
        layout.addWidget(self.textbox)
        layout.addWidget(self.label)
        layout.addWidget(self.plain)
        layout.addWidget(self.bu)
        self.setLayout(layout)



    def calcul(self,var):
        self.plain.clear()
        if(var.isdigit()):
            if(int(var)>0):
                n= int(var)
                value = [n]

                if(n > 1):

                    max = n

                    count = 1



                    while (n > 1):

                        if (n % 2 == 0):

                            n = n / 2

                        else:

                            n = 3 *n + 1
                        value.append(n)
                        count = count + 1

                    if (n > max):
                        max = n

                        print(n)


                    self.plain.append("nombre de termes dans la suite :" + str(count)+"\n")

                    self.plain.append("valeur max de la suite :" + str(max)+"\n")
                    self.plain.append(""+str(value));


            elif(n<=0):
                        self.plain.setText("Le nombre rentré doit etre supérieur a 0")
        else:
            self.plain.append("Vous devez rentrez un nombre")

    @pyqtSlot()
    def on_click(self):

        self.textboxValue= self.textbox.text()
        self.calcul(self.textboxValue)
        self.textbox.clear();

    def DisplayMessage(self):
        self.bu.setText("hello")

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Vous etes sur de vouloir quitter?", QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    app.exec_()








