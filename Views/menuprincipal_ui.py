
import sys
import os



myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from Controllers.menuprincipalController import menuprincipalController
from venta_ui import Ui_venta
from controlstock_ui import Ui_controlstock
from proveedores_ui import Ui_proveedores


class Ui_menuprincipal(object):
     def __init__(self):
        self.menuprincipalController = menuprincipalController(self)
     def setupUi(self, menuprincipal):
        menuprincipal.setObjectName("menuprincipal")
        menuprincipal.resize(800, 600)
        self.pushButton_3 = QtWidgets.QPushButton(menuprincipal)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 430, 171, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(menuprincipal)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 340, 171, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.btn_stock = QtWidgets.QPushButton(menuprincipal)
        self.btn_stock.setGeometry(QtCore.QRect(180, 250, 171, 51))
        self.btn_stock.setObjectName("btn_stock")
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
        self.label.raise_()
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.btn_stock.raise_()
        self.label_2.raise_()

        self.retranslateUi(menuprincipal)
        QtCore.QMetaObject.connectSlotsByName(menuprincipal)

         #--------------------Events--------------------------------------
        self.c = self.btn_stock.clicked.connect(lambda:self.menuprincipalController.open(Ui_controlstock, menuprincipal))
        self.c = self.pushButton_2.clicked.connect(lambda:self.menuprincipalController.open2(Ui_venta, menuprincipal))
        self.c = self.pushButton_3.clicked.connect(lambda:self.menuprincipalController.open3(Ui_proveedores, menuprincipal))
        #--------------------End Events---------------------------------

     def retranslateUi(self, menuprincipal):
        _translate = QtCore.QCoreApplication.translate
        menuprincipal.setWindowTitle(_translate("menuprincipal", "Form"))
        self.pushButton_3.setText(_translate("menuprincipal", "LISTA DE PROVEEDORES"))
        self.pushButton_2.setText(_translate("menuprincipal", "FACTURACION"))
        self.btn_stock.setText(_translate("menuprincipal", "CONTROL DE STOCK"))
        self.label_2.setText(_translate("menuprincipal", "Menu Principal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menuprincipal = QtWidgets.QWidget()
    ui = Ui_menuprincipal()
    ui.setupUi(menuprincipal)
    menuprincipal.show()
    sys.exit(app.exec_())
