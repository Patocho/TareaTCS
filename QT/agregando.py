#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
from PySide.QtGui import *
import agregar

class Agregando(QtGui.QDialog, agregar.Ui_AddP):

    def __init__(self, parent=None):
        super(Agregando, self).__init__(parent)
        self.setupUi(self)
        self.main_layout = QtGui.QVBoxLayout(self)
        self.show()

def run():
    app= QtGui.QApplication(sys.argv)
    form=Agregando()
    form.show()
    app.exec_()

if __name__ == '__main__':
    run()