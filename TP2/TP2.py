import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
os.system('mkdir -p "$XDG_RUNTIME_DIR"');

class MyMainWindow(QWidget):
    count =0;
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        # attributs de la fenetre principale
        self.setGeometry(300,300,800,600)
        self.setMinimumSize(QSize(200,100))
        self.setWindowTitle('My main window')  
        self.rectUtil = self.rect()
        self.onclick = False

        self.initUI()   # appel d'une methode dédiée à la création de l'IHM

    def initUI(self):
        # code pour remplir... n'a pas besoin de rester pour la suite du TP
        w = self.width()
        h = self.height()
        print(str(w)+","+str(h))

    def paintEvent(self, event):
        # ici code ne nécessitant pas de contexte graphique
        self.count =self.count +1 ;


        qp = QPainter()

        # suite à un événement paint il est possible de récupérer l’objet contexte graphique
        qp.begin(self)

        if(self.onclick):
             qp.drawText(QRect(self.x,self.y,250,100), Qt.AlignCenter, "Received Paint event N° : "+ str(self.count))
        else:
             qp.drawText(QRect(0,0,self.width(),self.height()), Qt.AlignCenter, "Received Paint event N° : "+ str(self.count))



         # mettre ici le code qui effectue un tracé graphique
        qp.end()
# fin tracé graphique
    def mouseReleaseEvent(self, event):
        p= event.pos()
# ici, par exemple, on recupere la position du clic en tant que QPoint
        self.x= event.x()
# ou ici en tant que valeur entière
        self.y = event.y()

        if(self.onclick == False):
             self.onclick =True
             self.update();
        else:
            self.update();




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyMainWindow() 
    w.show() 
    app.exec_()    # ou de préférence sys.exit(app.exec_()) si vous êtes sous linux
