#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
from PySide.QtGui import *
import agregar
import bd

class Agregando(QtGui.QDialog, agregar.Ui_AddP):

    def __init__(self, parent=None):
        super(Agregando, self).__init__(parent)
        self.setupUi(self)
        self.main_layout = QtGui.QVBoxLayout(self)
        self.addOk.clicked.connect(self.agrega)
        self.show()

    def agrega(self):
        codigo = self.textCodigo.text()
        nombre = self.textNom.text()
        descripcion = self.textDesc.text()
        color = self.textColor.text()
        precio = self.textPrecio.text()
        fk = self.textFk2.text()
        exito = bd.insertar(codigo, nombre, descripcion, color, precio, fk)
        print exito
        msgbox = QMessageBox()
        msgbox.setText("Producto agregado")
        msgbox.exec_()
        self.close()


def run():
    app = QtGui.QApplication(sys.argv)
    form = Agregando()
    form.show()
    app.exec_()

if __name__ == '__main__':
    run()