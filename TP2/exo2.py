import sys
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
os.system('mkdir -p "$XDG_RUNTIME_DIR"');

class MyMainWindow(QWidget):

    count =0;
    sendLetter = pyqtSignal(str)
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        # attributs de la fenetre principale
        self.setGeometry(300,300,600,300)
        self.setMinimumSize(QSize(200,100))
        self.setWindowTitle('My main window')
        self.rectUtil = self.rect()
        self.tab=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.nom1 = QPushButton(str(self.tab[1]), self)
        self.nom1.clicked.connect(self.getLetterFromClick())
        self.nom2 = QPushButton(str(self.tab[2]), self)
        self.nom2.clicked.connect(self.getLetterFromClick())
        self.nom3 = QPushButton(str(self.tab[3]), self)
        self.nom3.clicked.connect(self.getLetterFromClick())
        self.nom4 = QPushButton(str(self.tab[4]), self)
        self.nom4.clicked.connect(self.getLetterFromClick())
        self.nom5 = QPushButton(str(self.tab[5]), self)
        self.nom5.clicked.connect(self.getLetterFromClick())
        self.nom6 = QPushButton(str(self.tab[6]), self)
        self.nom6.clicked.connect(self.getLetterFromClick())
        self.nom7 = QPushButton(str(self.tab[7]), self)
        self.nom7.clicked.connect(self.getLetterFromClick())
        self.nom8 = QPushButton(str(self.tab[8]), self)
        self.nom8.clicked.connect(self.getLetterFromClick())
        self.nom9 = QPushButton(str(self.tab[9]), self)
        self.nom9.clicked.connect(self.getLetterFromClick())
        self.nom10 = QPushButton(str(self.tab[10]), self)
        self.nom10.clicked.connect(self.getLetterFromClick())
        self.nom11 = QPushButton(str(self.tab[11]), self)
        self.nom11.clicked.connect(self.getLetterFromClick())
        self.nom12 = QPushButton(str(self.tab[12]), self)
        self.nom12.clicked.connect(self.getLetterFromClick())
        self.nom13 = QPushButton(str(self.tab[13]), self)
        self.nom13.clicked.connect(self.getLetterFromClick())
        self.nom14 = QPushButton(str(self.tab[14]), self)
        self.nom14.clicked.connect(self.getLetterFromClick())
        self.nom15 = QPushButton(str(self.tab[15]), self)
        self.nom15.clicked.connect(self.getLetterFromClick())
        self.nom16= QPushButton(str(self.tab[16]), self)
        self.nom16.clicked.connect(self.getLetterFromClick())
        self.nom17 = QPushButton(str(self.tab[17]), self)
        self.nom17.clicked.connect(self.getLetterFromClick())
        self.nom18 = QPushButton(str(self.tab[18]), self)
        self.nom18.clicked.connect(self.getLetterFromClick())
        self.nom19 = QPushButton(str(self.tab[19]), self)
        self.nom19.clicked.connect(self.getLetterFromClick())
        self.nom20 = QPushButton(str(self.tab[20]), self)
        self.nom20.clicked.connect(self.getLetterFromClick())
        self.nom21 = QPushButton(str(self.tab[21]), self)
        self.nom21.clicked.connect(self.getLetterFromClick())
        self.nom22 = QPushButton(str(self.tab[22]), self)
        self.nom23.clicked.connect(self.getLetterFromClick())
        self.nom23 = QPushButton(str(self.tab[23]), self)
        self.nom24.clicked.connect(self.getLetterFromClick())
        self.nom24 = QPushButton(str(self.tab[24]), self)
        self.nom24.clicked.connect(self.getLetterFromClick())
        self.nom25 = QPushButton(str(self.tab[25]), self)
        self.nom25.clicked.connect(self.getLetterFromClick())
        self.nom26 = QPushButton(str(self.tab[26]), self)
        self.nom26.clicked.connect(self.getLetterFromClick(self))

        self.initUI()   # appel d'une methode dédiée à la création de l'IHM

    def initUI(self):
        # code pour remplir... n'a pas besoin de rester pour la suite du TP
        w = self.width()
        h = self.height()
        #self.Dessine = QPushButton("Dessine", self)
        #self.Dessine.move(20,20)
        #self.Efface = QPushButton("Efface", self)
        #self.Efface.move(20,50)
        #self.Dessine.clicked.connect(self.dessine)
        #self.Efface.clicked.connect(self.efface)
        self.grid = QGridLayout()

        #for i in range(0,25):
         #   self.nom = str("l"+str(i))
           # self.nom= QPushButton(self.tab[i], self)

            #self.grid.addWidget(self.nom)


        self.doPaint = False

        print(str(w)+","+str(h))
    def dessine(self):
        if(self.doPaint == False):
            self.doPaint=True
            self.update()
        else:
            self.update()

    def efface(self):
          if(self.doPaint == True):
            self.doPaint=False
            self.update()
          else:
            self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_D:
            self.dessine()
            self.update()

        if event.key() == Qt.Key_E:
            self.efface()
            self.update()


    # code si la touche est D (majuscule ou minuscule)
    def mouseReleaseEvent(self, event):
        p= event.pos()
# ici, par exemple, on recupere la position du clic en tant que QPoint
        self.x= event.x()
# ou ici en tant que valeur entière
        self.y = event.y()

        if(self.y >self.height()/2):
            for i in range(0,13):
                if(self.x <= (self.width()/13 *i )and self.x >= (self.width()/13 *(i-1))):
                    val= i +13
                    self.sendLetter.emit(str(self.tab[val-1]))
        else:
            for i in range(0,13):
                if(self.x <= (self.width()/13 *i )and self.x >= (self.width()/13 *(i-1))):
                    val= i
                    self.sendLetter.emit(str(self.tab[val-1]))
        self.update()


    def paintEvent(self, event):
        # ici code ne nécessitant pas de contexte graphique
        self.count =self.count +1 ;
        qp = QPainter()
        # suite à un événement paint il est possible de récupérer l’objet contexte graphique
        qp.begin(self)
        if(self.doPaint == True):
            qp.drawLine(0,self.height()/2,self.width(),self.height()/2)
            for i in range(0,13):
                qp.drawLine(self.width()/13*i,self.height(),self.width()/13*i,0)
                qp.drawText(QRect(self.width()/13*i,self.height()/-4,self.width()/13,self.height()), Qt.AlignCenter, str(self.tab[i]))
                qp.drawText(QRect(self.width()/13*i,self.height()/4,self.width()/13,self.height()), Qt.AlignCenter, str(self.tab[i+13]))

         # mettre ici le code qui effectue un tracé graphique
        qp.end()
# fin tracé graphique

class MyBrowser(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setGeometry(300,300,600,300)
        self.setMinimumSize(QSize(200,100))
        self.setWindowTitle('WEB')
        self.MyWebEngineView = QtWebEngineWidgets.QWebEngineView()
        self.url = "https://www.pokepedia.fr/Liste_des_Pokémon_par_ordre_alphabétique"
        self.MyWebEngineView.load(QUrl(self.url))
        layout= QVBoxLayout(self)
        layout.addWidget(self.MyWebEngineView)
        self.setLayout(layout)



    def changeLetter(self,letter):
        newurl = self.url + '#' + letter
        self.MyWebEngineView.load(QUrl(newurl))






if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = MyBrowser()
    w = MyMainWindow()
    w.sendLetter.connect(b.changeLetter)
    w.show()
    b.show()
    app.exec_()    # ou de préférence sys.exit(app.exec_()) si vous êtes sous linux
