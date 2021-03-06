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
        self.addCancel.clicked.connect(self.cancelar)
        self.show()

    def ed(self, codigo):
        self.addOk.setText("Guardar")
        self.addOk.clicked.disconnect(self.agrega)
        self.addOk.clicked.connect(self.edita)
        producto = bd.get(codigo)
        print producto
        self.textCodigo.setText(producto[0][0])
        self.textCodigo.setReadOnly(True)
        self.textNom.setText(producto[0][1])
        self.textDesc.setText(producto[0][2])
        self.textColor.setText(producto[0][3])
        self.textPrecio.setText(str(producto[0][4]))
        self.textFk2.setText(str(producto[0][5]))

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

    def edita(self):
        codigo = self.textCodigo.text()
        nombre = self.textNom.text()
        descripcion = self.textDesc.text()
        color = self.textColor.text()
        precio = self.textPrecio.text()
        fk = self.textFk2.text()
        exito = bd.guardarCambios(codigo, nombre, descripcion, color, precio, fk)
        print exito
        msgbox = QMessageBox()
        msgbox.setText("Producto Editado")
        msgbox.exec_()
        self.close()

    def cancelar():
        if (self.textCodigo.text() != "" or self.textNom.text() != "" or self.textDesc.text() != "" or self.textColor.text() != "" or self.textPrecio.text() != "" or self.textFk2.text() != ""):
            self.textCodigo.setText("")
            self.textNom.setText("")
            self.texDesc.setText("")
            self.textColor.setText("")
            self.textPrecio.setText("")
            self.textFk2.setText("")
        else:
            self.close()

def run():
    app = QtGui.QApplication(sys.argv)
    form = Agregando()
    form.show()
    app.exec_()

if __name__ == '__main__':
    run()
