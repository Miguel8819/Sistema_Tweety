# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificarProducto2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from Controllers.modificarProductoController import modificarProductoController
from PyQt5 import QtCore, QtGui, QtWidgets
from Models.Product import Product
from Database.Connection import connection

class Ui_ModificarProducto(object):
    def __init__(self, cod):
        self.product = Product(connection())
        self.modificarProducto = modificarProductoController(self)
        self.cod = cod

    def setupUi(self, ModificarProducto):
        ModificarProducto.setObjectName("ModificarProducto")
        ModificarProducto.resize(400, 300)
        self.label_6 = QtWidgets.QLabel(ModificarProducto)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("Imagenes/tweety2.jpg"))
        self.label_6.setObjectName("label_6")
        self.layoutWidget = QtWidgets.QWidget(ModificarProducto)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 20, 302, 258))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.input_name = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_name.setFont(font)
        self.input_name.setObjectName("input_name")
        self.gridLayout.addWidget(self.input_name, 2, 1, 1, 1)
        self.input_price = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_price.setFont(font)
        self.input_price.setObjectName("input_price")
        self.gridLayout.addWidget(self.input_price, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.input_category = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_category.setFont(font)
        self.input_category.setObjectName("input_category")
        self.gridLayout.addWidget(self.input_category, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.btn_modify = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_modify.setFont(font)
        self.btn_modify.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_modify.setObjectName("btn_modify")
        self.gridLayout.addWidget(self.btn_modify, 5, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.input_cant = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_cant.setFont(font)
        self.input_cant.setObjectName("input_cant")
        self.gridLayout.addWidget(self.input_cant, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.btn_cancel = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout.addWidget(self.btn_cancel, 6, 0, 1, 2)
        self.btn_exit = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setObjectName("btn_exit")
        self.gridLayout.addWidget(self.btn_exit, 7, 0, 1, 2)

        self.retranslateUi(ModificarProducto)
        QtCore.QMetaObject.connectSlotsByName(ModificarProducto)
        
        product = self.product.getProduct(self.cod)
        self.input_cant.setText(str(product[2]))
        self.input_name.setText(product[1])
        self.input_price.setText(product[3])
        self.input_category.setText(product[4])
        
        #--------------------Events--------------------------------------
        self.l = self.btn_modify.clicked.connect(lambda:self.modificarProducto.modificarProducto(self.cod, ModificarProducto))
        self.c = self.btn_cancel.clicked.connect(lambda:self.modificarProducto.borrar())
        self.e = self.btn_exit.clicked.connect(lambda:self.modificarProducto.salir(ModificarProducto))
        #--------------------End Events---------------------------------

    def retranslateUi(self, ModificarProducto):
        _translate = QtCore.QCoreApplication.translate
        ModificarProducto.setWindowTitle(_translate("ModificarProducto", "Form"))
        self.input_name.setPlaceholderText(_translate("ModificarProducto", "nombre"))
        self.input_price.setPlaceholderText(_translate("ModificarProducto", "precio"))
        self.label_5.setText(_translate("ModificarProducto", "Categoría:"))
        self.input_category.setPlaceholderText(_translate("ModificarProducto", "categoría"))
        self.label_4.setText(_translate("ModificarProducto", "Precio:"))
        self.label.setText(_translate("ModificarProducto", "Modificar Producto"))
        self.btn_modify.setText(_translate("ModificarProducto", "Modificar"))
        self.label_2.setText(_translate("ModificarProducto", "Cantidad:"))
        self.input_cant.setPlaceholderText(_translate("ModificarProducto", "cantidad"))
        self.label_3.setText(_translate("ModificarProducto", "Nombre:"))
        self.btn_cancel.setText(_translate("ModificarProducto", "Cancelar"))
        self.btn_exit.setText(_translate("ModificarProducto", "Salir"))
        