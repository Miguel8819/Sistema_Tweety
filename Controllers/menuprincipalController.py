import sys
import os

from Models.Product import Product
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.Product import Product

class menuprincipalController():

   def __init__(self, menuprincipal):
     self.product = Product(connection())
     self.menuprincipal = menuprincipal
  
   def open(self, Ui_controlstock, Form):
     self.menuprincipal.Form = QtWidgets.QWidget()
     self.menuprincipal.ui = Ui_controlstock()
     self.menuprincipal.ui.setupUi(self.menuprincipal.Form)
     self.menuprincipal.Form.show()
     Form.show()

   def open2(self, Ui_venta, Form):
     self.menuprincipal.Form = QtWidgets.QWidget()
     self.menuprincipal.ui = Ui_venta()
     self.menuprincipal.ui.setupUi(self.menuprincipal.Form)
     self.menuprincipal.Form.show()
     Form.show() 
   
   def open3(self, Ui_proveedores, Form):
     self.menuprincipal.Form = QtWidgets.QWidget()
     self.menuprincipal.ui = Ui_proveedores()
     self.menuprincipal.ui.setupUi(self.menuprincipal.Form)
     self.menuprincipal.Form.show()
     Form.show() 
  
   def open4(self, Ui_informeVentas, Form):
     self.menuprincipal.Form = QtWidgets.QWidget()
     self.menuprincipal.ui = Ui_informeVentas()
     self.menuprincipal.ui.setupUi(self.menuprincipal.Form)
     self.menuprincipal.Form.show()
     Form.show() 