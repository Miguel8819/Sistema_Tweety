# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controlstock.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_controlstock(object):
    def setupUi(self, controlstock):
        controlstock.setObjectName("controlstock")
        controlstock.resize(800, 600)
        self.pushButton = QtWidgets.QPushButton(controlstock)
        self.pushButton.setGeometry(QtCore.QRect(670, 550, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(controlstock)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Imagenes/tweety.jpg"))
        self.label_2.setObjectName("label_2")
        self.table_product = QtWidgets.QTableWidget(controlstock)
        self.table_product.setGeometry(QtCore.QRect(140, 130, 531, 331))
        self.table_product.setRowCount(10)
        self.table_product.setObjectName("table_product")
        self.table_product.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(4, item)
        self.btn_delete = QtWidgets.QPushButton(controlstock)
        self.btn_delete.setGeometry(QtCore.QRect(557, 480, 75, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delete.setFont(font)
        self.btn_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_actualizar = QtWidgets.QPushButton(controlstock)
        self.btn_actualizar.setGeometry(QtCore.QRect(170, 480, 111, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_actualizar.setFont(font)
        self.btn_actualizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_actualizar.setObjectName("btn_actualizar")
        self.btn_modificar = QtWidgets.QPushButton(controlstock)
        self.btn_modificar.setGeometry(QtCore.QRect(439, 480, 83, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_modificar.setFont(font)
        self.btn_modificar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_modificar.setObjectName("btn_modificar")
        self.btn_create = QtWidgets.QPushButton(controlstock)
        self.btn_create.setGeometry(QtCore.QRect(320, 480, 75, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_create.setFont(font)
        self.btn_create.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_create.setObjectName("btn_create")
        self.label = QtWidgets.QLabel(controlstock)
        self.label.setGeometry(QtCore.QRect(240, 57, 307, 45))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2.raise_()
        self.btn_create.raise_()
        self.btn_delete.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.table_product.raise_()
        self.btn_modificar.raise_()
        self.btn_actualizar.raise_()

        self.retranslateUi(controlstock)
        QtCore.QMetaObject.connectSlotsByName(controlstock)

    def retranslateUi(self, controlstock):
        _translate = QtCore.QCoreApplication.translate
        controlstock.setWindowTitle(_translate("controlstock", "Form"))
        self.pushButton.setText(_translate("controlstock", "Volver al menú"))
        item = self.table_product.horizontalHeaderItem(0)
        item.setText(_translate("controlstock", "CODIGO"))
        item = self.table_product.horizontalHeaderItem(1)
        item.setText(_translate("controlstock", "NOMBRE"))
        item = self.table_product.horizontalHeaderItem(2)
        item.setText(_translate("controlstock", "CANTIDAD"))
        item = self.table_product.horizontalHeaderItem(3)
        item.setText(_translate("controlstock", "PRECIO"))
        item = self.table_product.horizontalHeaderItem(4)
        item.setText(_translate("controlstock", "CATEGORIA"))
        self.btn_delete.setText(_translate("controlstock", "Eliminar"))
        self.btn_actualizar.setText(_translate("controlstock", "Actualizar"))
        self.btn_modificar.setText(_translate("controlstock", "Modificar"))
        self.btn_create.setText(_translate("controlstock", "Crear"))
        self.label.setText(_translate("controlstock", "Control de Stock"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controlstock = QtWidgets.QWidget()
    ui = Ui_controlstock()
    ui.setupUi(controlstock)
    controlstock.show()
    sys.exit(app.exec_())