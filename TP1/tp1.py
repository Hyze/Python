import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyMainWindow(QWidget):

    def closeEvent(self,event):
        reply = QMessageBox.question(self, 'Message', "Voulez vous quitter ??", QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def syracuse(self,val):

        n = int(val)
        if(n > 1):
            maxi = n
            values = []
            values.append(n)
            self.b.insertPlainText(""+str(n)+"\n")
            count = 1
            while (n > 1):
                if (n % 2 == 0):
                    n = n / 2
                    values.append(n)
                    self.b.insertPlainText(""+str(n)+"\n")
                else:
                    n = 3*n + 1
                    values.append(n)
                    self.b.insertPlainText(""+str(n)+"\n")

                count = count + 1
            print(values)
            maxi = max(values)
            if (n > maxi):
                maxi = n
            print("nombre de termes dans la suite :" + str(count))
            print("valeur max de la suite :" + str(maxi))


            self.px.fill(QColor(200, 200, 200))   # RAZ de la zone graphique, elle est remplie avec une couleur RGB de votre choix
            painter = QPainter(self.px)           # récupération de l’objet QPainter de la pixmap
            pas = 300/count
            echelle = 300/maxi
            
            for i in range(len(values)-1):                      # parcours dans les termes de la suite
                h = values[i]*echelle
                h2 = values[i+1]*echelle
                x1 = pas*i
                x2 = pas*(i+1)

                #painter.drawpoint(values[i],h)           # tracé d’un point
                painter.drawLine(x1,h,x2,h2)    # ou bien tracé d’un trait
                self.lb.setPixmap(self.px) 
 

    def lance(self):
        self.b.clear()
        self.syracuse(self.textbox.text())

    def DisplayMessage(self):
        self.label.setText("Hello")

    def __init__(self, parent=None):

        QWidget.__init__(self, parent=parent)
        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,500,300)
        self.setWindowTitle("My Main Window")

        self.textbox = QLineEdit(self)
        self.onlyInt = QIntValidator(1,99)
        self.textbox.setValidator(self.onlyInt)

        self.label = QLabel("cliquer pour quitter")
        self.bu = QPushButton("Go...")

        self.b = QPlainTextEdit(self)
        self.b.insertPlainText("You can write text here.\n")

        #bu.clicked.connect(QApplication.instance().quit)

        #self.bu.clicked.connect(self.DisplayMessage)

        self.bu.clicked.connect(self.lance)

        self.lb = QLabel()
        self.lb.setFixedWidth(300)
        self.lb.setFixedHeight(300)
        self.lb.setFrameShape(QFrame.Panel)   # pour dessiner un contour autour de la zone
        self.px = QPixmap(300,300)

        layout = QVBoxLayout(self)
        layout.addWidget(self.textbox)
        layout.addWidget(self.label)
        layout.addWidget(self.bu)
        layout.addWidget(self.b)
        layout.addWidget(self.lb)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    app.exec_()