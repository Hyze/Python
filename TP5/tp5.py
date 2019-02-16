import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QUrl
from PyQt5.QtQml import QQmlApplicationEngine

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = QQmlApplicationEngine()
    view.load(QUrl("tp5/tp5.qml"))
    sys.exit(app.exec_())

