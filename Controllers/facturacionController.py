import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Database.Connection import connection
from Models.Product import Product

class facturacionController():
    def __init__(self, create_product):
        self.product = Product(connection())
        self.create_product = create_product

    def createProduct(self,cod,name,cantidad,price,category,CreateProduct):
        if cod and name and price and category:
            self.product.insertProduct(cod,name,cantidad,price,category)
            CreateProduct.hide()

    def borrar(self):
        input = self.create_product.input_cant.clear()
        input = self.create_product.input_name.clear()
        input = self.create_product.input_price.clear()
        input = self.create_product.input_category.clear()

    def salir(self, CreateProduct):
        CreateProduct.close()