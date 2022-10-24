import sys
import os



myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from Controllers.menuprincipalController import menuprincipalController
from venta_ui import Ui_venta
from controlstock_ui import Ui_controlstock
from proveedores_ui import Ui_proveedores
from informeVentas_ui import Ui_informeVentas



class Ui_menuprincipal(object):
    def __init__(self):
        self.menuprincipalController = menuprincipalController(self)
   
    def setupUi(self, menuprincipal):
        menuprincipal.setObjectName("menuprincipal")
        menuprincipal.resize(800, 600)
        self.pushButton_3 = QtWidgets.QPushButton(menuprincipal)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 410, 171, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.btn_facturacion = QtWidgets.QPushButton(menuprincipal)
        self.btn_facturacion.setGeometry(QtCore.QRect(180, 290, 171, 51))
        self.btn_facturacion.setObjectName("btn_facturacion")
        self.btn_infVentas = QtWidgets.QPushButton(menuprincipal)
        self.btn_infVentas.setGeometry(QtCore.QRect(180, 350, 171, 51))
        self.btn_infVentas.setObjectName("btn_infVentas")
        self.label = QtWidgets.QLabel(menuprincipal)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Imagenes/tweety.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(menuprincipal)
        self.label_2.setGeometry(QtCore.QRect(190, 60, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn_clientes = QtWidgets.QPushButton(menuprincipal)
        self.btn_clientes.setGeometry(QtCore.QRect(180, 470, 171, 51))
        self.btn_clientes.setObjectName("btn_clientes")
        self.btn_stock = QtWidgets.QPushButton(menuprincipal)
        self.btn_stock.setGeometry(QtCore.QRect(180, 230, 171, 51))
        self.btn_stock.setObjectName("btn_stock")
        self.label.raise_()
        self.pushButton_3.raise_()
        self.btn_facturacion.raise_()
        self.btn_infVentas.raise_()
        self.label_2.raise_()
        self.btn_clientes.raise_()
        self.btn_stock.raise_()

        self.retranslateUi(menuprincipal)
        QtCore.QMetaObject.connectSlotsByName(menuprincipal)

        self.c = self.btn_stock.clicked.connect(lambda:self.menuprincipalController.open(Ui_controlstock, menuprincipal))
        self.c = self.btn_facturacion.clicked.connect(lambda:self.menuprincipalController.open2(Ui_venta, menuprincipal))
        self.c = self.pushButton_3.clicked.connect(lambda:self.menuprincipalController.open3(Ui_proveedores, menuprincipal))

        self.c = self.btn_infVentas.clicked.connect(lambda:self.menuprincipalController.open4(Ui_informeVentas, menuprincipal))

    def retranslateUi(self, menuprincipal):
        _translate = QtCore.QCoreApplication.translate
        menuprincipal.setWindowTitle(_translate("menuprincipal", "Form"))
        self.pushButton_3.setText(_translate("menuprincipal", "LISTA DE PROVEEDORES"))
        self.btn_facturacion.setText(_translate("menuprincipal", "FACTURACION"))
        self.btn_infVentas.setText(_translate("menuprincipal", "INFORME DE VENTAS"))
        self.label_2.setText(_translate("menuprincipal", "Menu Principal"))
        self.btn_clientes.setText(_translate("menuprincipal", "CLIENTES"))
        self.btn_stock.setText(_translate("menuprincipal", "CONTROL DE STOCK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menuprincipal = QtWidgets.QWidget()
    ui = Ui_menuprincipal()
    ui.setupUi(menuprincipal)
    menuprincipal.show()
    sys.exit(app.exec_())
