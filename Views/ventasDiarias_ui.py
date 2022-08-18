


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventasDiarias(object):
    def setupUi(self, ventasDiarias):
        ventasDiarias.setObjectName("ventasDiarias")
        ventasDiarias.resize(1002, 600)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        ventasDiarias.setPalette(palette)
        self.pushButton = QtWidgets.QPushButton(ventasDiarias)
        self.pushButton.setGeometry(QtCore.QRect(850, 550, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.table_product = QtWidgets.QTableWidget(ventasDiarias)
        self.table_product.setGeometry(QtCore.QRect(30, 130, 931, 331))
        self.table_product.setRowCount(10)
        self.table_product.setObjectName("table_product")
        self.table_product.setColumnCount(9)
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
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(8, item)
        self.btn_delete = QtWidgets.QPushButton(ventasDiarias)
        self.btn_delete.setGeometry(QtCore.QRect(657, 490, 75, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delete.setFont(font)
        self.btn_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_actualizar = QtWidgets.QPushButton(ventasDiarias)
        self.btn_actualizar.setGeometry(QtCore.QRect(270, 490, 111, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_actualizar.setFont(font)
        self.btn_actualizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_actualizar.setObjectName("btn_actualizar")
        self.btn_modificar = QtWidgets.QPushButton(ventasDiarias)
        self.btn_modificar.setGeometry(QtCore.QRect(539, 490, 83, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_modificar.setFont(font)
        self.btn_modificar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_modificar.setObjectName("btn_modificar")
        self.btn_create = QtWidgets.QPushButton(ventasDiarias)
        self.btn_create.setGeometry(QtCore.QRect(420, 490, 75, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_create.setFont(font)
        self.btn_create.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_create.setObjectName("btn_create")
        self.label = QtWidgets.QLabel(ventasDiarias)
        self.label.setGeometry(QtCore.QRect(330, 50, 307, 45))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btn_create.raise_()
        self.btn_delete.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.table_product.raise_()
        self.btn_modificar.raise_()
        self.btn_actualizar.raise_()

        self.retranslateUi(ventasDiarias)
        QtCore.QMetaObject.connectSlotsByName(ventasDiarias)

        

    def retranslateUi(self, ventasDiarias):
        _translate = QtCore.QCoreApplication.translate
        ventasDiarias.setWindowTitle(_translate("ventasDiarias", "Form"))
        self.pushButton.setText(_translate("ventasDiarias", "Volver atras"))
        item = self.table_product.horizontalHeaderItem(0)
        item.setText(_translate("ventasDiarias", "FECHA"))
        item = self.table_product.horizontalHeaderItem(1)
        item.setText(_translate("ventasDiarias", "HORA"))
        item = self.table_product.horizontalHeaderItem(2)
        item.setText(_translate("ventasDiarias", "CODIGO"))
        item = self.table_product.horizontalHeaderItem(3)
        item.setText(_translate("ventasDiarias", "CANTIDAD"))
        item = self.table_product.horizontalHeaderItem(4)
        item.setText(_translate("ventasDiarias", "DESCRIPCION"))
        item = self.table_product.horizontalHeaderItem(5)
        item.setText(_translate("ventasDiarias", "PRECIO UNIT"))
        item = self.table_product.horizontalHeaderItem(6)
        item.setText(_translate("ventasDiarias", "DESCUENTO"))
        item = self.table_product.horizontalHeaderItem(7)
        item.setText(_translate("ventasDiarias", "TOTAL"))
        item = self.table_product.horizontalHeaderItem(8)
        item.setText(_translate("ventasDiarias", "STOCK"))
        self.btn_delete.setText(_translate("ventasDiarias", "Eliminar"))
        self.btn_actualizar.setText(_translate("ventasDiarias", "Actualizar"))
        self.btn_modificar.setText(_translate("ventasDiarias", "Modificar"))
        self.btn_create.setText(_translate("ventasDiarias", "Crear"))
        self.label.setText(_translate("ventasDiarias", "Ventas Diarias"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventasDiarias = QtWidgets.QWidget()
    ui = Ui_ventasDiarias()
    ui.setupUi(ventasDiarias)
    ventasDiarias.show()
    sys.exit(app.exec_())
