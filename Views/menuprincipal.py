# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuprincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menuprincipal(object):
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
        self.label.setPixmap(QtGui.QPixmap("../Imagenes/tweety.jpg"))
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
