import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
import Syracuse_bug

class MyMainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.initUI()


def initUI(self):
    self.setGeometry(300,300,500,300)
    self.setWindowTitle('My Main Window')
    label = QLabel("cliquer pour quitter")
    textbox = QLineEdit()
    textbox.move(20, 20)
    textbox.resize(280,40)
    self.bu = QPushButton("Go...")
    bu.clicked.connect(on_click)
    layout = QVBoxLayout(self)
    layout.addWidget(textbox)
    layout.addWidget(label)
    layout.addWidget(self.bu)
    self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    app.exec_()






@pyqtSlot()
def on_click(self):
    textboxValue = textbox.text()
    Syracuse_bug.calcul( textboxValue)
    textbox.clear();


if __name__ == '__main__':

    app = QApplication(sys.argv)


    w = QWidget()

    w.resize(500, 300)

    # w.move(300, 300)

    w.setWindowTitle('My Main Window')

    textbox = QLineEdit()
    textbox.move(20, 20)
    textbox.resize(280,40)
    # creation des widgets "fils" : un label et un bouton

    label = QLabel("Tapez le nombre que vous voulez")

    bu = QPushButton("Calcul")


    # connection de l'action du bouton sur une action déjà definie (quit)

    bu.clicked.connect(on_click)





    # layout (gestion de geometrie)

    layout = QVBoxLayout(w)

    layout.addWidget(label)
    layout.addWidget(textbox)

    layout.addWidget(bu)

    w.setLayout(layout)


    # affichage

    w.show()


    # lancement de la gestion des evenements

    app.exec_()

