#!/usr/bin/env python

from PyQt5.QtCore import (QTimer)
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QMainWindow,
        QMessageBox, QTextEdit)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()



if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    mainWin.raise_()
    QTimer.singleShot(0,app.quit)
    sys.exit(app.exec_())
