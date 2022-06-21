from itertools import product
import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets

from Database.Connection import connection
from Models.Product import Product


class ventaController():

    def __init__(self, venta):
        self.product = Product(connection())
        self.venta = venta
        

    def open2(self, Ui_venta):
        self.venta.Form = QtWidgets.QWidget()
        self.venta.ui = Ui_venta()
        self.venta.ui.setupUi(self.venta.Form)
        self.venta.Form.show()


    
    def aceptar(self, Ui_venta): 
      
        table = self.venta.table_venta        
        product = self.product.getProduct(2)
        
        
           
        table.setItem(0,0, QtWidgets.QTableWidgetItem(product[0])) #cod
        table.setItem(0,1, QtWidgets.QTableWidgetItem('0'))
        table.setItem(0,2, QtWidgets.QTableWidgetItem(product[1])) #name
        table.setItem(0,3, QtWidgets.QTableWidgetItem(product[3])) #price
        table.setItem(0,4, QtWidgets.QTableWidgetItem('0'))
        table.setItem(0,5, QtWidgets.QTableWidgetItem('0'))
        table.setItem(0,6, QtWidgets.QTableWidgetItem(product[2])) #stock


        
    

    def salir(self, Ui_venta):
        Ui_venta.close()
