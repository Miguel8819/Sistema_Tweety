# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventasMensuales.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventasMensuales(object):
    def setupUi(self, ventasMensuales):
        ventasMensuales.setObjectName("ventasMensuales")
        ventasMensuales.resize(790, 570)
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
        ventasMensuales.setPalette(palette)
        self.label = QtWidgets.QLabel(ventasMensuales)
        self.label.setGeometry(QtCore.QRect(220, 10, 361, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(ventasMensuales)
        self.tableWidget.setGeometry(QtCore.QRect(300, 80, 191, 391))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.tableWidget.setPalette(palette)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(12)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.volver = QtWidgets.QPushButton(ventasMensuales)
        self.volver.setGeometry(QtCore.QRect(360, 520, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.volver.setFont(font)
        self.volver.setObjectName("volver")

        self.retranslateUi(ventasMensuales)
        QtCore.QMetaObject.connectSlotsByName(ventasMensuales)

    def retranslateUi(self, ventasMensuales):
        _translate = QtCore.QCoreApplication.translate
        ventasMensuales.setWindowTitle(_translate("ventasMensuales", "Form"))
        self.label.setText(_translate("ventasMensuales", "Ventas mensuales"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("ventasMensuales", "ENERO"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("ventasMensuales", "FEBRERO"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("ventasMensuales", "MARZO"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("ventasMensuales", "ABRIL"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("ventasMensuales", "MAYO"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("ventasMensuales", "JUNIO"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("ventasMensuales", "JULIO"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("ventasMensuales", "AGOSTO"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("ventasMensuales", "SEPTIEMBRE"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("ventasMensuales", "OCTUBRE"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("ventasMensuales", "NOVIEMBRE"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("ventasMensuales", "DICIEMBRE"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ventasMensuales", "VENTAS"))
        self.volver.setText(_translate("ventasMensuales", "Volver atras"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventasMensuales = QtWidgets.QWidget()
    ui = Ui_ventasMensuales()
    ui.setupUi(ventasMensuales)
    ventasMensuales.show()
    sys.exit(app.exec_())