# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'itemdialog.ui'
#
# Created: Fri Mar 30 23:13:26 2012
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ItemDialog(object):
    def setupUi(self, ItemDialog):
        ItemDialog.setObjectName(_fromUtf8("ItemDialog"))
        ItemDialog.resize(515, 439)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ItemDialog.sizePolicy().hasHeightForWidth())
        ItemDialog.setSizePolicy(sizePolicy)
        ItemDialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayout_2 = QtGui.QVBoxLayout(ItemDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(ItemDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label = QtGui.QLabel(ItemDialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_id = QtGui.QLabel(ItemDialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lineEdit_id.setFont(font)
        self.lineEdit_id.setObjectName(_fromUtf8("lineEdit_id"))
        self.gridLayout.addWidget(self.lineEdit_id, 0, 1, 1, 1)
        self.lineEdit_title = QtGui.QLineEdit(ItemDialog)
        self.lineEdit_title.setObjectName(_fromUtf8("lineEdit_title"))
        self.gridLayout.addWidget(self.lineEdit_title, 3, 1, 1, 7)
        self.label_5 = QtGui.QLabel(ItemDialog)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 1)
        self.lineEdit_user_login = QtGui.QLabel(ItemDialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lineEdit_user_login.setFont(font)
        self.lineEdit_user_login.setObjectName(_fromUtf8("lineEdit_user_login"))
        self.gridLayout.addWidget(self.lineEdit_user_login, 0, 4, 1, 1)
        self.label_9 = QtGui.QLabel(ItemDialog)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 0, 6, 1, 1)
        self.spinBox_rating = QtGui.QSpinBox(ItemDialog)
        self.spinBox_rating.setMaximum(5)
        self.spinBox_rating.setObjectName(_fromUtf8("spinBox_rating"))
        self.gridLayout.addWidget(self.spinBox_rating, 0, 7, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_3 = QtGui.QLabel(ItemDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.plainTextEdit_notes = QtGui.QPlainTextEdit(ItemDialog)
        self.plainTextEdit_notes.setMinimumSize(QtCore.QSize(0, 46))
        self.plainTextEdit_notes.setObjectName(_fromUtf8("plainTextEdit_notes"))
        self.verticalLayout_4.addWidget(self.plainTextEdit_notes)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_text_edit_fields = QtGui.QVBoxLayout()
        self.verticalLayout_text_edit_fields.setObjectName(_fromUtf8("verticalLayout_text_edit_fields"))
        self.label_7 = QtGui.QLabel(ItemDialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_text_edit_fields.addWidget(self.label_7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_text_edit_fields)
        self.verticalLayout_text_edit_tags = QtGui.QVBoxLayout()
        self.verticalLayout_text_edit_tags.setObjectName(_fromUtf8("verticalLayout_text_edit_tags"))
        self.label_6 = QtGui.QLabel(ItemDialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_text_edit_tags.addWidget(self.label_6)
        self.horizontalLayout_4.addLayout(self.verticalLayout_text_edit_tags)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(ItemDialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.fileAbsPath = QtGui.QLineEdit(ItemDialog)
        self.fileAbsPath.setReadOnly(True)
        self.fileAbsPath.setObjectName(_fromUtf8("fileAbsPath"))
        self.verticalLayout.addWidget(self.fileAbsPath)
        self.label_8 = QtGui.QLabel(ItemDialog)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.fileLocationDirRelPath = QtGui.QLineEdit(ItemDialog)
        self.fileLocationDirRelPath.setReadOnly(True)
        self.fileLocationDirRelPath.setObjectName(_fromUtf8("fileLocationDirRelPath"))
        self.verticalLayout.addWidget(self.fileLocationDirRelPath)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonAddDataRef = QtGui.QPushButton(ItemDialog)
        self.pushButtonAddDataRef.setObjectName(_fromUtf8("pushButtonAddDataRef"))
        self.horizontalLayout.addWidget(self.pushButtonAddDataRef)
        self.pushButtonRemoveDataRef = QtGui.QPushButton(ItemDialog)
        self.pushButtonRemoveDataRef.setObjectName(_fromUtf8("pushButtonRemoveDataRef"))
        self.horizontalLayout.addWidget(self.pushButtonRemoveDataRef)
        self.pushButtonMoveFile = QtGui.QPushButton(ItemDialog)
        self.pushButtonMoveFile.setObjectName(_fromUtf8("pushButtonMoveFile"))
        self.horizontalLayout.addWidget(self.pushButtonMoveFile)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(ItemDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(ItemDialog)
        QtCore.QMetaObject.connectSlotsByName(ItemDialog)

    def retranslateUi(self, ItemDialog):
        ItemDialog.setWindowTitle(QtGui.QApplication.translate("ItemDialog", "Repository item", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ItemDialog", "Title:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ItemDialog", "Id:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_id.setText(QtGui.QApplication.translate("ItemDialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ItemDialog", "User:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_user_login.setText(QtGui.QApplication.translate("ItemDialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ItemDialog", "Rating:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ItemDialog", "Notes:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ItemDialog", "Fields:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ItemDialog", "Tags:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ItemDialog", "Absolute path to referenced File:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ItemDialog", "Location of referenced File in the Repository:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddDataRef.setToolTip(QtGui.QApplication.translate("ItemDialog", "Add Data Reference to this Item", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddDataRef.setText(QtGui.QApplication.translate("ItemDialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonRemoveDataRef.setToolTip(QtGui.QApplication.translate("ItemDialog", "Remove Data Reference from this Item. File will not be deleted.", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonRemoveDataRef.setText(QtGui.QApplication.translate("ItemDialog", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonMoveFile.setToolTip(QtGui.QApplication.translate("ItemDialog", "Move Data Reference File to another location in the same repository.", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonMoveFile.setText(QtGui.QApplication.translate("ItemDialog", "Move File", None, QtGui.QApplication.UnicodeUTF8))

