
import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)


from PyQt5 import QtCore, QtGui, QtWidgets

from Controllers.informeVentasController import informeVentasController
from ventasDiarias_ui import Ui_ventasDiarias
from ventasMensuales_ui import Ui_ventasMensuales

class Ui_informeVentas(object):
    def __init__(self):
        self.informeVentasController = informeVentasController(self)
   
   
    
    def setupUi(self, informeVentas):
        informeVentas.setObjectName("informeVentas")
        informeVentas.resize(448, 320)
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
        informeVentas.setPalette(palette)
        self.volver = QtWidgets.QPushButton(informeVentas)
        self.volver.setGeometry(QtCore.QRect(270, 260, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.volver.setFont(font)
        self.volver.setObjectName("volver")
        self.label = QtWidgets.QLabel(informeVentas)
        self.label.setGeometry(QtCore.QRect(50, 10, 351, 45))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btn_ventasDiarias = QtWidgets.QPushButton(informeVentas)
        self.btn_ventasDiarias.setGeometry(QtCore.QRect(50, 110, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_ventasDiarias.setFont(font)
        self.btn_ventasDiarias.setObjectName("btn_ventasDiarias")
        self.btn_ventasMensuales = QtWidgets.QPushButton(informeVentas)
        self.btn_ventasMensuales.setGeometry(QtCore.QRect(250, 110, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_ventasMensuales.setFont(font)
        self.btn_ventasMensuales.setObjectName("btn_ventasMensuales")
        self.label.raise_()
        self.volver.raise_()
        self.btn_ventasDiarias.raise_()
        self.btn_ventasMensuales.raise_()

        self.retranslateUi(informeVentas)
        QtCore.QMetaObject.connectSlotsByName(informeVentas)

        self.p = self.volver.clicked.connect(lambda:self.informeVentasController.volver(informeVentas))
        self.a = self.btn_ventasDiarias.clicked.connect(lambda:self.informeVentasController.Vdiarias(Ui_ventasDiarias, informeVentas))
        self.a = self.btn_ventasMensuales.clicked.connect(lambda:self.informeVentasController.Vmensuales(Ui_ventasMensuales, informeVentas))

    def retranslateUi(self, informeVentas):
        _translate = QtCore.QCoreApplication.translate
        informeVentas.setWindowTitle(_translate("informeVentas", "Form"))
        self.volver.setText(_translate("informeVentas", "Volver atras"))
        self.label.setText(_translate("informeVentas", "Informe de Ventas"))
        self.btn_ventasDiarias.setText(_translate("informeVentas", "Ventas diarias"))
        self.btn_ventasMensuales.setText(_translate("informeVentas", "Ventas mensuales"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    informeVentas = QtWidgets.QWidget()
    ui = Ui_informeVentas()
    ui.setupUi(informeVentas)
    informeVentas.show()
    sys.exit(app.exec_())
