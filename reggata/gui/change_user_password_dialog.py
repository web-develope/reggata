'''
Created on 20.07.2012

@author: vlkv
'''

import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
from reggata.ui.ui_changeuserpassword import Ui_ChangeUserPasswordDialog
from reggata.data.db_schema import *
from reggata.helpers import *
from reggata.errors import *
from reggata.data.repo_mgr import *


class ChangeUserPasswordDialog(QtGui.QDialog):

    def __init__(self, parent, user):
        super(ChangeUserPasswordDialog, self).__init__(parent)

        self.ui = Ui_ChangeUserPasswordDialog()
        self.ui.setupUi(self)

        assert user is not None
        self.__user = user

        self.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.buttonOk)
        self.connect(self.ui.buttonBox, QtCore.SIGNAL("rejected()"), self.buttonCancel)

        self.read()


    def read(self):
        self.ui.lineEdit_user_login.setText(self.__user.login)

    def write(self):
        self.__currentPasswordHash = computePasswordHash(self.ui.lineEdit_current_password.text())
        self.__newPassword1Hash = computePasswordHash(self.ui.lineEdit_new_password1.text())
        self.__newPassword2Hash = computePasswordHash(self.ui.lineEdit_new_password2.text())
        self.newPasswordHash = self.__newPassword1Hash

    def checkThatCurrentPasswordIsCorrect(self):
        if self.__user.password != self.__currentPasswordHash:
            raise MsgException("Current password is wrong.")

    def checkThatTwoNewPasswordsAreTheSame(self):
        if self.__newPassword1Hash != self.__newPassword2Hash:
            raise MsgException("Entered new passwords do not match.")

    def buttonOk(self):
        try:
            self.write()
            self.checkThatCurrentPasswordIsCorrect()
            self.checkThatTwoNewPasswordsAreTheSame()
            self.accept()

        except Exception as ex:
            show_exc_info(self, ex)

    def buttonCancel(self):
        self.reject()
