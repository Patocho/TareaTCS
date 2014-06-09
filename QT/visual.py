#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
from PySide.QtGui import *
import Taller
import bd
import agregar
import agregando


class Principal(QtGui.QWidget, Taller.Ui_Dialog, agregar.Ui_AddP):

    def __init__(self,parent=None):
        super(Principal, self).__init__(parent)
        self.setupUi(self)
        self.filtro = "0"
        self.fk = ""
        self.main_layout = QtGui.QVBoxLayout(self)
        self.render_table()
        self.load(self.filtro)
        self.show()
        self.index = self.comboBox.activated.connect(self.filtrar)
        self.NewP.clicked.connect(self.agrega)
        self.Edit.clicked.connect(self.editar)
        self.Del.clicked.connect(self.eliminar)
        self.lineEdit.textEdited.connect(self.load_line)

    def agrega(self):
        app = agregando.Agregando()
        app.exec_()
        print "agregar" #aca va el metodo que abre la ventana agregar.ui

    def editar(self):
        print "editar" #aca va el metodo que captura la linea a editar

    def eliminar(self): #aca va el metodo que selecciona la linea a eliminar
        model = self.table.model()
        index = self.table.currentIndex()
        if index.row() == -1:
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            #Obtenemos el codigo que es la primary key en la tabla Producto
            codigo = model.index(index.row(), 0, QtCore.QModelIndex()).data()
            if (bd.eliminar(codigo)):
                self.load("0")
                msgBox = QtGui.QMessageBox()
                msgBox.setText("EL registro fue eliminado.")
                msgBox.exec_()
                return True
            else:
                self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                self.ui.errorMessageDialog.showMessage("Error al eliminar")
                return False

    def render_table(self):
        self.table = self.tableView
        self.table.setFixedWidth(750)
        self.table.setFixedHeight(300)
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table.setAlternatingRowColors(True)
        self.table.setSortingEnabled(True)
        self.main_layout.addWidget(self.table)

    def filtrar(self,index):
        #metodo que se inicia al usar el combobox, capturando el index
        a = str(index)
        self.filtro = a
        self.load(self.filtro)


    def buscar(self):
        texto = self.lineEdit.text()
        self.load_line(texto)


    def load(self,filtro):
        productos = bd.obtener(filtro)
        self.model = QtGui.QStandardItemModel(len(productos), 6)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Codigo"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Descrp"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Color"))
        self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Precio"))
        self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Fk"))
        r = 0
        for row in productos:
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, row['Codigo'])
            index = self.model.index(r, 1, QtCore.QModelIndex())
            self.model.setData(index, row['Nombre'])
            index = self.model.index(r, 2, QtCore.QModelIndex())
            self.model.setData(index, row['Descripcion'])
            index = self.model.index(r, 3, QtCore.QModelIndex())
            self.model.setData(index, row['Color'])
            index = self.model.index(r, 4, QtCore.QModelIndex())
            self.model.setData(index, row['Precio'])
            index = self.model.index(r, 5, QtCore.QModelIndex())
            self.model.setData(index, row['Fk_id_marca'])
            r = r + 1
        self.table.setModel(self.model)


    def load_line(self, palabra):
        print palabra
        productos = bd.consultar_nombre(palabra)
        self.model = QtGui.QStandardItemModel(len(productos), 6)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Codigo"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Descrp"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Color"))
        self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Precio"))
        self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Fk"))
        r = 0
        for row in productos:
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, row['Codigo'])
            index = self.model.index(r, 1, QtCore.QModelIndex())
            self.model.setData(index, row['Nombre'])
            index = self.model.index(r, 2, QtCore.QModelIndex())
            self.model.setData(index, row['Descripcion'])
            index = self.model.index(r, 3, QtCore.QModelIndex())
            self.model.setData(index, row['Color'])
            index = self.model.index(r, 4, QtCore.QModelIndex())
            self.model.setData(index, row['Precio'])
            index = self.model.index(r, 5, QtCore.QModelIndex())
            self.model.setData(index, row['Fk_id_marca'])
            r = r + 1
        self.table.setModel(self.model)




def run():
    app= QtGui.QApplication(sys.argv)
    form=Principal()
    form.show()
    app.exec_()

if __name__ == '__main__':
    run()