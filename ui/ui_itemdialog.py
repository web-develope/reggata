# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'itemdialog.ui'
#
# Created: Sun Oct 17 10:44:23 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ItemDialog(object):
    def setupUi(self, ItemDialog):
        ItemDialog.setObjectName("ItemDialog")
        ItemDialog.resize(587, 544)
        self.verticalLayout_5 = QtGui.QVBoxLayout(ItemDialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtGui.QLabel(ItemDialog)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit_id = QtGui.QLineEdit(ItemDialog)
        self.lineEdit_id.setReadOnly(True)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.horizontalLayout_3.addWidget(self.lineEdit_id)
        self.label_5 = QtGui.QLabel(ItemDialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lineEdit_user_login = QtGui.QLineEdit(ItemDialog)
        self.lineEdit_user_login.setReadOnly(True)
        self.lineEdit_user_login.setObjectName("lineEdit_user_login")
        self.horizontalLayout_3.addWidget(self.lineEdit_user_login)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(ItemDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_title = QtGui.QLineEdit(ItemDialog)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.horizontalLayout_2.addWidget(self.lineEdit_title)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtGui.QLabel(ItemDialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.plainTextEdit_notes = QtGui.QPlainTextEdit(ItemDialog)
        self.plainTextEdit_notes.setObjectName("plainTextEdit_notes")
        self.verticalLayout_4.addWidget(self.plainTextEdit_notes)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtGui.QLabel(ItemDialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.listWidget_data_refs = QtGui.QListWidget(ItemDialog)
        self.listWidget_data_refs.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_data_refs.setObjectName("listWidget_data_refs")
        self.verticalLayout.addWidget(self.listWidget_data_refs)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_add_files = QtGui.QPushButton(ItemDialog)
        self.pushButton_add_files.setObjectName("pushButton_add_files")
        self.verticalLayout_2.addWidget(self.pushButton_add_files)
        self.pushButton_add_URL = QtGui.QPushButton(ItemDialog)
        self.pushButton_add_URL.setObjectName("pushButton_add_URL")
        self.verticalLayout_2.addWidget(self.pushButton_add_URL)
        self.pushButton_remove = QtGui.QPushButton(ItemDialog)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.verticalLayout_2.addWidget(self.pushButton_remove)
        self.pushButton_move_up = QtGui.QPushButton(ItemDialog)
        self.pushButton_move_up.setObjectName("pushButton_move_up")
        self.verticalLayout_2.addWidget(self.pushButton_move_up)
        self.pushButton_move_down = QtGui.QPushButton(ItemDialog)
        self.pushButton_move_down.setObjectName("pushButton_move_down")
        self.verticalLayout_2.addWidget(self.pushButton_move_down)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtGui.QLabel(ItemDialog)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.plainTextEdit_fields = QtGui.QPlainTextEdit(ItemDialog)
        self.plainTextEdit_fields.setObjectName("plainTextEdit_fields")
        self.verticalLayout_7.addWidget(self.plainTextEdit_fields)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtGui.QLabel(ItemDialog)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.plainTextEdit_tags = QtGui.QPlainTextEdit(ItemDialog)
        self.plainTextEdit_tags.setObjectName("plainTextEdit_tags")
        self.verticalLayout_8.addWidget(self.plainTextEdit_tags)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.buttonBox = QtGui.QDialogButtonBox(ItemDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_5.addWidget(self.buttonBox)

        self.retranslateUi(ItemDialog)
        QtCore.QMetaObject.connectSlotsByName(ItemDialog)

    def retranslateUi(self, ItemDialog):
        ItemDialog.setWindowTitle(QtGui.QApplication.translate("ItemDialog", "Элемент хранилища", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ItemDialog", "id:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ItemDialog", "Пользователь:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ItemDialog", "Название:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ItemDialog", "Описание:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ItemDialog", "Связанные объекты:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_add_files.setText(QtGui.QApplication.translate("ItemDialog", "Добавить файлы", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_add_URL.setText(QtGui.QApplication.translate("ItemDialog", "Добавить URL", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_remove.setText(QtGui.QApplication.translate("ItemDialog", "Убрать", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_move_up.setText(QtGui.QApplication.translate("ItemDialog", "Вверх", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_move_down.setText(QtGui.QApplication.translate("ItemDialog", "Вниз", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ItemDialog", "Поля:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ItemDialog", "Теги:", None, QtGui.QApplication.UnicodeUTF8))

