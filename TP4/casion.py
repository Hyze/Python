import sys
import time
import random

from PyQt5.QtCore import QTimer, QRect
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import *
import os
#import MyComponents.MyWidget_exo1 as exo1
#import MyComponents.MyWidget_exo2 as exo2
import MyComponents.casino as casino
os.system('mkdir -p "$XDG_RUNTIME_DIR"')


class MyImageViewerWidget(QFrame):

    def __init__(self, *args):
        super(MyImageViewerWidget, self).__init__(*args)
        self.setGeometry(0, 0, 940, 300)
       # self.ui= exo1.Ui_Form()
        #self.ui.setupUi(self)
        self.ui = casino.Ui_Form()
        self.ui.setupUi(self)
        self.index=0
        self.timer = QTimer()

        self.ui.Gauche.setFixedSize(300,300)
        self.ui.Centre.setFixedSize(300,300)
        self.ui.Droite.setFixedSize(300,300)
        self.ui.Start.setText("GO")
        self.ui.Start = QPushButton()
        self.bigimage: QImage = QImage("slot_machine_symbols.png")


        self.rects: list = [
            QRect(0, 0, 300, 300),
            QRect(300, 0, 300, 300),
            QRect(600, 0, 300, 300),
            QRect(0, 300, 300, 300),
            QRect(300, 300, 300, 300),
            QRect(600, 300, 300, 300),
            QRect(0, 600, 300, 300),
            QRect(300, 600, 300, 300),
            QRect(600, 600, 300, 300),
        ]

        self.ui.Gauche.setPixmap(QPixmap(self.bigimage.copy(self.rects[0])))
        self.ui.Droite.setPixmap(QPixmap(self.bigimage.copy(self.rects[1])))
        self.ui.Centre.setPixmap(QPixmap(self.bigimage.copy(self.rects[2])))
        self.ui.Gauche = QLabel()
        self.ui.Centre = QLabel()
        self.ui.Droite = QLabel()



    def Animate(self):
        print("Animate")

        if not self.ui.mTimer.isChecked():
            self.timer.stop()

            self.ui.mTimer.setText("Start")
        else:
            self.timer.start(500)
            self.timer.timeout.connect(self.next_auto)

            self.ui.mTimer.setText("Stop")

    def next_auto(self):
        self.Next()


    def casino(self):
        print('start')

        symbols = ["#", "?", "~", "$"]  # The symbols on the reels

        user = ""
        random.seed()
        test = int(4 * random.random())

        while (user != "exit"):


            a=QRect()
            b=QRect()
            c=QRect()

            for i in range (0,20):

                # take care, sleep needs an argument in seconds, not millis
                time.sleep( (50 + 25 * i)/1000)   # slow down while the loop runs

                c = self.rects[random.randint(0, 3)]
                self.ui.Gauche.setPixmap(QPixmap(self.bigimage.copy(c)))
                if( i < 10 ):
                    a = self.rects[random.randint(0, 3)]
                    self.ui.Centre.setPixmap(QPixmap(self.bigimage.copy(a)))
                if( i < 15 ):
                    b = self.rects[random.randint(0, 3)]
                    self.ui.Droite.setPixmap(QPixmap(self.bigimage.copy(b)))

                self.update()

            self.casino()
            self.ui.Gauche.setPixmap(QPixmap(self.bigimage.copy(a)))
            self.ui.Droite.setPixmap(QPixmap(self.bigimage.copy(b)))
            self.ui.Centre.setPixmap(QPixmap(self.bigimage.copy(c)))


            if((a == b) and (b == c)) :
                user = input("You win the jackpot. Press enter to play again or type \"exit\" to exit")

            # le test ternaire condition ? a : b s'ecrit en pyhton a if condition else b
            elif (((1 if (a == "$") else 0) + (1 if (b == "$") else 0) + (1 if (c == "$") else 0)) == 2) :  # check if at least two $
                user = input("You win. Press enter to play again or type \"exit\" to exit")
            else :
                user = input("You lose. Press enter to play again or type \"exit\" to exit")


    def Next(self):
        if(self.index +1 ==len(self.rects)):
            self.index=0
            self.ui.mLabel.setPixmap(QPixmap(self.bigimage.copy(self.rects[self.index])))
        else:
             self.index = self.index + 1
             self.ui.mLabel.setPixmap(QPixmap(self.bigimage.copy(self.rects[self.index])))



    def Previous(self):

        if(self.index==0):

            self.index=len(self.rects)-1
            self.ui.mLabel.setPixmap(QPixmap(self.bigimage.copy(self.rects[self.index])))

        else:
            self.index = self.index-1
            self.ui.mLabel.setPixmap(QPixmap(self.bigimage.copy(self.rects[self.index])))



class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        # attributs de la fenetre principale
        self.setGeometry(100, 100, 940, 300)
        self.setWindowTitle('Simple diaporama application')

        # donnée membre qui contiendra la frame associée à la widget crée par QtDesigner
        self.mDisplay = MyImageViewerWidget(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    app.exec_()
