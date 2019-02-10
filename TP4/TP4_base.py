import sys

from PyQt5.QtCore import QTimer, QRect
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import *
import os
import MyComponents.MyWidget_exo1 as exo1
import MyComponents.MyWidget_exo2 as exo2
os.system('mkdir -p "$XDG_RUNTIME_DIR"')


class MyImageViewerWidget(QFrame):

    def __init__(self, *args):
        super(MyImageViewerWidget, self).__init__(*args)
        self.setGeometry(0, 0, 800, 600)
       # self.ui= exo1.Ui_Form()
        #self.ui.setupUi(self)
        self.ui = exo2.Ui_Form()
        self.ui.setupUi(self)
        self.index=0
        self.timer = QTimer()
        self.ui.mLabel.setFixedSize(300,300)
        self.ui.mButtonBrowse.hide()
        self.ui.mLineEdit.hide()
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

        self.ui.mLabel.setPixmap(QPixmap(self.bigimage.copy(self.rects[0])))

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





    def LoadFiles(self):
        print("Loading files...")
        self.path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if self.path :
            self.ui.mLineEdit.setText(self.path)
            self.file= os.listdir(self.path)
            self.fullpath = str(self.path+"/"+self.file[self.index])
            self.px = QPixmap(self.fullpath)
            self.ui.mLabel.setPixmap(self.px.scaled(self.ui.mLabel.width(),self.ui.mLabel.height()))




    def Next(self):
        if(self.index +1 ==len(self.rects)):
            self.index=0
            self.ui.mLabel.setPixmap(QPixmap(self.bigimage.copy(self.rects[self.index])))
        else:
             self.index = self.index + 1
             self.ui.mLabel.setPixmap(QPixmap(self.bigimage.copy(self.rects[self.index])))

        #if(self.index +1 ==len(self.file)):
         #   self.index=0
          #  self.fullpath = str(self.path+"/"+self.file[self.index])
          #  print(self.fullpath)
           # self.px = QPixmap(self.fullpath)
           # self.ui.mLabel.setPixmap(self.px.scaled(self.ui.mLabel.width(),self.ui.mLabel.height()))
            #self.update()

        # #else:
        #  #   print("Next image")
        #     self.index = self.index + 1
        #     self.fullpath = str(self.path+"/"+self.file[self.index])
        #     print(self.fullpath)
        #     self.px = QPixmap(self.fullpath)
        #     self.ui.mLabel.setPixmap(self.px.scaled(self.ui.mLabel.width(),self.ui.mLabel.height()))
        #     self.update()


    def Previous(self):

        if(self.index==0):

            self.index=len(self.rects)-1
            self.ui.mLabel.setPixmap(QPixmap(self.bigimage.copy(self.rects[self.index])))

        else:
            self.index = self.index-1
            self.ui.mLabel.setPixmap(QPixmap(self.bigimage.copy(self.rects[self.index])))


   #print("Previous image")
    #    if(self.index==0):
     #       self.index=len(self.file)-1
        #    self.fullpath = str(self.path+"/"+self.file[self.index])
         #   print(self.fullpath)
          #  self.px = QPixmap(self.fullpath)
           # self.ui.mLabel.setPixmap(self.px.scaled(self.ui.mLabel.width(),self.ui.mLabel.height()))
            #self.update()
      #  else:
       #     self.index = self.index-1
        #    self.fullpath = str(self.path+"/"+self.file[self.index])
         #   print(self.fullpath)
          #  self.px = QPixmap(self.fullpath)
           # self.ui.mLabel.setPixmap(self.px.scaled(self.ui.mLabel.width(),self.ui.mLabel.height()))
            #self.update()



class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        # attributs de la fenetre principale
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Simple diaporama application')

        # donnée membre qui contiendra la frame associée à la widget crée par QtDesigner
        self.mDisplay = MyImageViewerWidget(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    app.exec_()
