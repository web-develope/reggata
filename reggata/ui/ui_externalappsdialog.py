# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\externalappsdialog.ui'
#
# Created: Tue Oct 29 20:36:08 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ExternalAppsDialog(object):
    def setupUi(self, ExternalAppsDialog):
        ExternalAppsDialog.setObjectName(_fromUtf8("ExternalAppsDialog"))
        ExternalAppsDialog.resize(650, 255)
        self.verticalLayout = QtGui.QVBoxLayout(ExternalAppsDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(ExternalAppsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 8, 1, 1, 1)
        self.comboBoxCategory = QtGui.QComboBox(ExternalAppsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxCategory.sizePolicy().hasHeightForWidth())
        self.comboBoxCategory.setSizePolicy(sizePolicy)
        self.comboBoxCategory.setObjectName(_fromUtf8("comboBoxCategory"))
        self.gridLayout.addWidget(self.comboBoxCategory, 1, 2, 1, 1)
        self.buttonNewCategory = QtGui.QPushButton(ExternalAppsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonNewCategory.sizePolicy().hasHeightForWidth())
        self.buttonNewCategory.setSizePolicy(sizePolicy)
        self.buttonNewCategory.setObjectName(_fromUtf8("buttonNewCategory"))
        self.gridLayout.addWidget(self.buttonNewCategory, 1, 3, 1, 1)
        self.buttonDeleteCategory = QtGui.QPushButton(ExternalAppsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonDeleteCategory.sizePolicy().hasHeightForWidth())
        self.buttonDeleteCategory.setSizePolicy(sizePolicy)
        self.buttonDeleteCategory.setObjectName(_fromUtf8("buttonDeleteCategory"))
        self.gridLayout.addWidget(self.buttonDeleteCategory, 1, 4, 1, 1)
        self.label_2 = QtGui.QLabel(ExternalAppsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.lineEditAppCmd = QtGui.QLineEdit(ExternalAppsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditAppCmd.sizePolicy().hasHeightForWidth())
        self.lineEditAppCmd.setSizePolicy(sizePolicy)
        self.lineEditAppCmd.setReadOnly(False)
        self.lineEditAppCmd.setObjectName(_fromUtf8("lineEditAppCmd"))
        self.gridLayout.addWidget(self.lineEditAppCmd, 2, 2, 1, 2)
        self.buttonSelectApp = QtGui.QPushButton(ExternalAppsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSelectApp.sizePolicy().hasHeightForWidth())
        self.buttonSelectApp.setSizePolicy(sizePolicy)
        self.buttonSelectApp.setObjectName(_fromUtf8("buttonSelectApp"))
        self.gridLayout.addWidget(self.buttonSelectApp, 2, 4, 1, 1)
        self.label_3 = QtGui.QLabel(ExternalAppsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.lineEditFileExtensions = QtGui.QLineEdit(ExternalAppsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditFileExtensions.sizePolicy().hasHeightForWidth())
        self.lineEditFileExtensions.setSizePolicy(sizePolicy)
        self.lineEditFileExtensions.setObjectName(_fromUtf8("lineEditFileExtensions"))
        self.gridLayout.addWidget(self.lineEditFileExtensions, 3, 2, 1, 2)
        self.groupBox = QtGui.QGroupBox(ExternalAppsDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 5)
        spacerItem1 = QtGui.QSpacerItem(12, 0, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(ExternalAppsDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout.addWidget(self.groupBox_2, 5, 0, 1, 5)
        self.label_4 = QtGui.QLabel(ExternalAppsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 6, 1, 1, 1)
        self.lineEditExtFileBrowserCmd = QtGui.QLineEdit(ExternalAppsDialog)
        self.lineEditExtFileBrowserCmd.setObjectName(_fromUtf8("lineEditExtFileBrowserCmd"))
        self.gridLayout.addWidget(self.lineEditExtFileBrowserCmd, 6, 2, 1, 2)
        self.buttonSelectFileBrowser = QtGui.QPushButton(ExternalAppsDialog)
        self.buttonSelectFileBrowser.setObjectName(_fromUtf8("buttonSelectFileBrowser"))
        self.gridLayout.addWidget(self.buttonSelectFileBrowser, 6, 4, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(0, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 7, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(ExternalAppsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ExternalAppsDialog)
        QtCore.QMetaObject.connectSlotsByName(ExternalAppsDialog)

    def retranslateUi(self, ExternalAppsDialog):
        ExternalAppsDialog.setWindowTitle(_translate("ExternalAppsDialog", "Preferred External Applications", None))
        self.label.setText(_translate("ExternalAppsDialog", "Category of files:", None))
        self.buttonNewCategory.setText(_translate("ExternalAppsDialog", "New", None))
        self.buttonDeleteCategory.setText(_translate("ExternalAppsDialog", "Delete", None))
        self.label_2.setText(_translate("ExternalAppsDialog", "Executable:", None))
        self.lineEditAppCmd.setToolTip(_translate("ExternalAppsDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Syntax: </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &lt;path to executable&gt; &lt;replacement fields&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Replacement fields could be:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">%f - will be replaced with file name;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">%d - will be replaced with containing directory of the file.</span></p></body></html>", None))
        self.buttonSelectApp.setText(_translate("ExternalAppsDialog", "Select", None))
        self.label_3.setText(_translate("ExternalAppsDialog", "File extensions:", None))
        self.lineEditFileExtensions.setToolTip(_translate("ExternalAppsDialog", "File extentions, separated with spaces, e.g. \".txt .doc .csv\"", None))
        self.groupBox.setTitle(_translate("ExternalAppsDialog", "External Applications For Different Types Of Files", None))
        self.groupBox_2.setTitle(_translate("ExternalAppsDialog", "External File Browser", None))
        self.label_4.setText(_translate("ExternalAppsDialog", "Executable:", None))
        self.buttonSelectFileBrowser.setText(_translate("ExternalAppsDialog", "Select", None))

