import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Database.Connection import connection
from Models.venta import venta

class finalizarVentaController():
    def __init__(self, finalizar_venta):
        self.venta = venta(connection())
        self.finalizar_venta = finalizar_venta

    def finalizarVenta(self,codigo,cantidad,descripcion,precio_unit,descuento,total,stock,finalizarVenta):
        if codigo and cantidad and descripcion and precio_unit and descuento and total and stock:
            self.venta.insertVenta(codigo,cantidad,descripcion,precio_unit,descuento,total,stock)
            finalizarVenta.hide()



    def salir(self, finalizarVenta):
        finalizarVenta.close()