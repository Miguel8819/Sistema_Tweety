import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets, QtGui
from Database.Connection import connection
from Models.Proveedores import *
from PyQt5.QtWidgets import QMessageBox, QLineEdit
from PyQt5.QtCore import QDate

class CreateProveedorController():
    def __init__(self, create_proveedor):
        self.proveedor = Proveedor(connection())
        self.create_proveedor = create_proveedor

    def createProveedor(self, nombreProveedor, nombreFactura, fechaAlta, calle, numeroCalle, ciudad, codPostal, celular, email, pagWeb, proveedores):
        if nombreProveedor and nombreFactura and fechaAlta and calle and numeroCalle and ciudad and codPostal and celular and email and pagWeb:
            self.proveedor.insertProveedor(nombreProveedor,nombreFactura,fechaAlta,calle, numeroCalle, ciudad, codPostal, celular, email, pagWeb)

        msg = QMessageBox()
        msg.setWindowTitle("Confirmar Nuevo Proveedor")
        msg.setText("¿Desea crear este nuevo Proveedor?")

        msg.setIcon(QMessageBox.Information)

        #msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText("Seleccione aceptar para crear un nuevo proveedor\n\nSeleccione cancelar si desea corregir datos o sino quisiera crear un nuevo proveedor")
        x = msg.exec_()

        input = self.create_proveedor.input_nameProv.clear()
        input = self.create_proveedor.input_nameFact.clear()
        input = self.create_proveedor.input_calle.clear()
        input = self.create_proveedor.input_numCalle.clear()
        input = self.create_proveedor.input_codPostal.clear()
        input = self.create_proveedor.input_tel.clear()
        input = self.create_proveedor.input_email.clear()
        input = self.create_proveedor.input_web.clear()

    def showProveedor(self,nombreProveedor, nameProv, nameFact, fechaAlta_2, calle, numCalle, codPostal, tel, email, web, Ui_proveedores):
        if nombreProveedor:
            result = self.proveedor.getProveedor(nombreProveedor)
            self.create_proveedor.show_nameProv.setText(str(result[1]))
            self.create_proveedor.show_nameFact.setText(str(result[2]))
            self.create_proveedor.show_fechaAlta_2.setDate(QDate.fromString(result[3]))
            self.create_proveedor.show_calle.setText(str(result[4]))
            self.create_proveedor.show_numCalle.setText(str(result[5]))
            #self.create_proveedor.show_ciudad.setText(str(result[6]))
            self.create_proveedor.show_codPostal.setText(str(result[7]))
            self.create_proveedor.show_tel.setText(str(result[8]))
            self.create_proveedor.show_email.setText(str(result[9]))
            self.create_proveedor.show_web.setText(str(result[10]))

    def autoCompleteProv(self):
        edit = QtGui.QLineEdit
        val = self.proveedor.autoComplete()[1]
        completer = QtGui.QCompleter(val, edit)
        edit.setCompleter(completer)
        edit.show()

    