from itertools import product
import sys
import os

from Models.venta import venta

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

  

    
    def aceptar(self, Ui_venta, cod): 
     
        table = self.venta.table_venta        
       
        product = self.product.getProduct(cod)
        
        if table.rowCount()==20: 
            rowCount=0
            table.setRowCount(1)
        else:
            rowCount=table.rowCount()
            table.setRowCount(table.rowCount() + 1 )
           
            
        print(table.rowCount())
        print(rowCount)    

        table.setItem(rowCount,0, QtWidgets.QTableWidgetItem(product[0])) #cod
        table.setItem(rowCount,1, QtWidgets.QTableWidgetItem('1')) #cant
        table.setItem(rowCount,2, QtWidgets.QTableWidgetItem(product[1])) #name
        table.setItem(rowCount,3, QtWidgets.QTableWidgetItem(product[3])) #price
        table.setItem(rowCount,4, QtWidgets.QTableWidgetItem('0')) #descuento
        table.setItem(rowCount,5, QtWidgets.QTableWidgetItem('0')) #total
        table.setItem(rowCount,6, QtWidgets.QTableWidgetItem(product[2])) #stock

        self.venta.input_codprod.clear()

       

        
       

        
    

    def salir(self, Ui_venta):
        Ui_venta.close()
