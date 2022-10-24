
import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets

from Database.Connection import connection

from Models.Product import Product



class informeVentasController():

    def __init__(self, informeVentas):
        self.product = Product(connection())
        self.informeVentas = informeVentas
    
    def Vdiarias(self, Ui_ventasDiarias, Form):
     self.informeVentas.Form = QtWidgets.QWidget()
     self.informeVentas.ui = Ui_ventasDiarias()
     self.informeVentas.ui.setupUi(self.informeVentas.Form)
     self.informeVentas.Form.show()
     Form.show()
    
    def Vmensuales(self, Ui_ventasMensuales, Form):
     self.informeVentas.Form = QtWidgets.QWidget()
     self.informeVentas.ui = Ui_ventasMensuales()
     self.informeVentas.ui.setupUi(self.informeVentas.Form)
     self.informeVentas.Form.show()
     Form.show()

    def volver(self, Ui_informeVentas):
        Ui_informeVentas.close()
