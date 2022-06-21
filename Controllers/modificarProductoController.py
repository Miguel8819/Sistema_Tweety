import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.Product import Product

class modificarProductoController():

    def __init__(self, modificar):
        self.product = Product(connection())
        self.modificar = modificar

    def borrar(self):
        input = self.modificar.input_cant.clear()
        input = self.modificar.input_name.clear()
        input = self.modificar.input_price.clear()
        input = self.modificar.input_category.clear()

    def modificarProducto(self, cod, ModificarProducto):
        self.product.modificarProduct(cod,self.modificar.input_name.text(),
        int(self.modificar.input_cant.text()),self.modificar.input_price.text(),
        self.modificar.input_category.text())
        ModificarProducto.close()

    def salir(self, ModificarProducto):
        ModificarProducto.close()