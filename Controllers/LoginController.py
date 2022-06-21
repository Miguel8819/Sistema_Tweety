import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.User import User

class LoginController():

    def __init__(self, log_in):
        self.user = User(connection())
        self.log_in = log_in

    def logIn(self,user,password, ControlStock, LogIn):
        if user and password:
            user = self.user.getUser(user,password)
            if user:
                self.log_in.Form = QtWidgets.QMainWindow()
                self.log_in.ui = ControlStock()
                self.log_in.ui.setupUi(self.log_in.Form)
                self.log_in.Form.show()
                print('Estas logeado')
                LogIn.close()
            else:
                print('No estas logeado')

    def salir():
        sys.exit()