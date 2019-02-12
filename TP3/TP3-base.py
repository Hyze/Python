import pickle
import random
import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import QPainter, QColor, QBrush, QIcon, QPixmap

os.system('mkdir -p "$XDG_RUNTIME_DIR"');
from PyQt5.QtWidgets import *


class myHisto(QLabel):

    def __init__(self, parent=None):
        QLabel.__init__(self, parent=parent)
        print('Constructeur de la classe myHisto')
        self.m_list = []

    def max(self):
        bin_max = 0
        for i in self.m_list:
            if i.m_amount > bin_max:
                bin_max = i.m_amount
        return bin_max


class Intervalle:
    def __init__(self, a=0, b=0):
        print('Constructeur de la classe Intervalle')
        self.m_x = a
        self.m_amount = b


class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        # attributs de la fenetre principale
        self.setGeometry(300, 300, 600, 450)
        self.setWindowTitle('Main Window')
        # Barre de status pour afficher les infos
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Zone d'informations, peut toujours servir")
        self.mHisto = myHisto()
        self.flague=False
        self.createActions()
        self.createMenus()

        self.setAcceptDrops(True)


    def createActions(self):
        print('Creation menu')
        # mise en relation article de menu -> slots **/
        self.exitAct = QAction("&Bye...", self)
        self.exitAct.setShortcut("Ctrl+B")
        self.exitAct.triggered.connect(self.exit)
        self.Open=QAction("&Open",self)
        self.Open.setShortcut("Ctrl+O")
        self.Open.triggered.connect(self.open)
        self.Save =QAction("&Save",self)
        self.Save.setShortcut("Ctrl+S")
        self.Save.triggered.connect(self.save)
        self.Restore=QAction("&Restore",self)
        self.Restore.setShortcut("Ctrl+R")
        self.Restore.triggered.connect(self.restore)
        self.Clear=QAction("&Clear",self)
        self.Clear.setShortcut("C")
        self.Clear.triggered.connect(self.clear)
        self.Color=QAction("&Color",self)


        self.couleur = QColor(255,0,0)
        pixmap = QPixmap(15,15)
        pixmap.fill((self.couleur))
        self.colorIcon = pixmap
        self.Color.setIcon(QIcon(self.colorIcon))

        self.Color.triggered.connect(self.color)



    def createMenus(self):
        fileMenu = self.menuBar().addMenu("&File")
        fileMenu.addAction(self.exitAct)
        fileMenu.addAction(self.Open)
        fileMenu.addAction(self.Save)
        fileMenu.addAction(self.Restore)
        Display = self.menuBar().addMenu("&Display ")
        Display.addAction(self.Clear)
        Display.addAction(self.Color)

    def exit(self):
        self.statusBar.showMessage("Invoked File|Bye ...")
        QApplication.quit()

    def open(self):
        self.mHisto.m_list=[]
        self.statusBar.showMessage("Histogramme Openned")
        self.options = QFileDialog.Options()
        self.options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=self.options)
        if self.fileName:
            self.file= QFile(self.fileName)
            self.file.open(QIODevice.ReadOnly|QIODevice.Text)
            while not self.file.atEnd():
                line = self.file.readLine()
                self.processLine(line)
            self.file.close()

        if(self.flague == False):
            self.flague=True
            self.update()
        else:
            self.update()


    def processLine(self,line):
        hysto= myHisto()
        list=[]
        ligne=line.split(" ")


        indiceBin=(str)(ligne[0])
        valeurBin=(str)(ligne[1])
        transtable= str.maketrans({"\\":"","n":""," ":"","'":"","b":""})
        indiceBin=(int)(indiceBin.translate(transtable))
        valeurBin=(int)(valeurBin.translate(transtable))

        #print(nb)
        i= Intervalle(indiceBin,valeurBin)
        list.append(i)
        self.mHisto.m_list.append(i)


    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()




    def dropEvent(self, event):
        for url in event.mimeData().urls():
            self.mHisto.m_list=[]
            self.name= url.toLocalFile()
            self.statusBar.showMessage(self.name)
            self.file= QFile(self.name)
            self.file.open(QIODevice.ReadOnly|QIODevice.Text)
            while not self.file.atEnd():
                line = self.file.readLine()
                self.processLine(line)

            self.file.close()
            if(self.flague == False):
                self.flague=True
                self.update()
            else:
                self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_R:
            for i in self.mHisto.m_list:
                x = random.randint(0,99)
                i.m_amount=x
            if(self.flague== False):
                self.flague=True
                self.update()



    def paintEvent(self, QPaintEvent):

        if(self.flague):
            taille =len(self.mHisto.m_list)
            echelle =self.height()/self.mHisto.max()
            qp=QPainter()
            qp.begin(self)
            for i in self.mHisto.m_list:
                qp.setBrush(QBrush(self.couleur))
                qp.drawRect(self.width()/taille*i.m_x,self.height()-echelle,(self.width()/taille*(i.m_x+1))-(self.width()/taille*i.m_x),(self.height()-(i.m_amount*echelle))-(self.height()-echelle))

            qp.end()
            self.update()
        else:
            self.update()


    def save(self):
        self.statusBar.showMessage("Histogramme Save")
        pickle.dump(self.mHisto.m_list,open("saveHisto.bin","wb"))

    def restore(self):
        self.statusBar.showMessage("Histogramme Restored")
        self.file= pickle.load(open("saveHisto.bin","rb"))
        self.mHisto.m_list=self.file
        if(self.flague == False):
            self.flague=True
            self.update()
        else:
            self.update()



    def clear(self):
        self.statusBar.showMessage("Histogramme Clear")
        self.mHisto.m_list=[]
        self.flague=False
        self.update()

    def color(self):
        try:
            self.color=QColorDialog.getColor()
        except (RuntimeError, TypeError, NameError):
            pass

        print(self.color)
        if self.color.isValid :
            self.couleur=self.color
            pixmap = QPixmap(15,15)
            pixmap.fill((self.couleur))
            self.colorIcon = pixmap
            self.Color.setIcon(QIcon(self.colorIcon))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    app.exec_()
