# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serializereditdlg.ui'
#
# Created: Fri Dec 09 15:41:49 2011
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SerializerEditDlg(object):
    def setupUi(self, SerializerEditDlg):
        SerializerEditDlg.setObjectName(_fromUtf8("SerializerEditDlg"))
        SerializerEditDlg.resize(216, 206)
        SerializerEditDlg.setWindowTitle(QtWidgets.QApplication.translate("SerializerEditDlg", "Serializer Properties", None, QtWidgets.QApplication.UnicodeUTF8))
        self.verticalLayout_2 = QtGui.QVBoxLayout(SerializerEditDlg)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.enableSerializationCHB = QtGui.QCheckBox(SerializerEditDlg)
        self.enableSerializationCHB.setText(QtWidgets.QApplication.translate("SerializerEditDlg", "Allow Serialization", None, QtWidgets.QApplication.UnicodeUTF8))
        self.enableSerializationCHB.setObjectName(_fromUtf8("enableSerializationCHB"))
        self.verticalLayout_2.addWidget(self.enableSerializationCHB)
        self.outputGB = QtGui.QGroupBox(SerializerEditDlg)
        self.outputGB.setTitle(QtWidgets.QApplication.translate("SerializerEditDlg", "Output Properties", None, QtWidgets.QApplication.UnicodeUTF8))
        self.outputGB.setObjectName(_fromUtf8("outputGB"))
        self.verticalLayout = QtGui.QVBoxLayout(self.outputGB)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.outputGB)
        self.label.setText(QtWidgets.QApplication.translate("SerializerEditDlg", "Output Frequency", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.frequencySB = QtGui.QSpinBox(self.outputGB)
        self.frequencySB.setMaximum(100000000)
        self.frequencySB.setProperty("value", 100)
        self.frequencySB.setObjectName(_fromUtf8("frequencySB"))
        self.gridLayout.addWidget(self.frequencySB, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.outputGB)
        self.label_2.setText(QtWidgets.QApplication.translate("SerializerEditDlg", "File Format", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.fileFormatCB = QtGui.QComboBox(self.outputGB)
        self.fileFormatCB.setObjectName(_fromUtf8("fileFormatCB"))
        self.fileFormatCB.addItem(_fromUtf8(""))
        self.fileFormatCB.setItemText(0, QtWidgets.QApplication.translate("SerializerEditDlg", "text", None, QtWidgets.QApplication.UnicodeUTF8))
        self.fileFormatCB.addItem(_fromUtf8(""))
        self.fileFormatCB.setItemText(1, QtWidgets.QApplication.translate("SerializerEditDlg", "binary", None, QtWidgets.QApplication.UnicodeUTF8))
        self.gridLayout.addWidget(self.fileFormatCB, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.multipleDirCHB = QtGui.QCheckBox(self.outputGB)
        self.multipleDirCHB.setText(QtWidgets.QApplication.translate("SerializerEditDlg", "Allow multiple restart snapshots", None, QtWidgets.QApplication.UnicodeUTF8))
        self.multipleDirCHB.setObjectName(_fromUtf8("multipleDirCHB"))
        self.verticalLayout.addWidget(self.multipleDirCHB)
        self.verticalLayout_2.addWidget(self.outputGB)
        self.enableRestartCHB = QtGui.QCheckBox(SerializerEditDlg)
        self.enableRestartCHB.setText(QtWidgets.QApplication.translate("SerializerEditDlg", "Enable Restart", None, QtWidgets.QApplication.UnicodeUTF8))
        self.enableRestartCHB.setObjectName(_fromUtf8("enableRestartCHB"))
        self.verticalLayout_2.addWidget(self.enableRestartCHB)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.okPB = QtGui.QPushButton(SerializerEditDlg)
        self.okPB.setText(QtWidgets.QApplication.translate("SerializerEditDlg", "OK", None, QtWidgets.QApplication.UnicodeUTF8))
        self.okPB.setObjectName(_fromUtf8("okPB"))
        self.horizontalLayout_2.addWidget(self.okPB)
        self.cancelPB = QtGui.QPushButton(SerializerEditDlg)
        self.cancelPB.setText(QtWidgets.QApplication.translate("SerializerEditDlg", "Cancel", None, QtWidgets.QApplication.UnicodeUTF8))
        self.cancelPB.setObjectName(_fromUtf8("cancelPB"))
        self.horizontalLayout_2.addWidget(self.cancelPB)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SerializerEditDlg)
        QtCore.QObject.connect(self.okPB, QtCore.SIGNAL(_fromUtf8("clicked()")), SerializerEditDlg.accept)
        QtCore.QObject.connect(self.cancelPB, QtCore.SIGNAL(_fromUtf8("clicked()")), SerializerEditDlg.reject)
        QtCore.QObject.connect(self.enableSerializationCHB, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.outputGB.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(SerializerEditDlg)

    def retranslateUi(self, SerializerEditDlg):
        pass

