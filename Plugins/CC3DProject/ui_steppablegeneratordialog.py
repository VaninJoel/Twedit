# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SteppableGeneratorDialog.ui'
#
# Created: Mon Aug 13 14:43:57 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SteppableGenerator(object):
    def setupUi(self, SteppableGenerator):
        SteppableGenerator.setObjectName(_fromUtf8("SteppableGenerator"))
        SteppableGenerator.resize(421, 323)
        SteppableGenerator.setWindowTitle(QtWidgets.QApplication.translate("SteppableGenerator", "Generate Steppable", None, QtWidgets.QApplication.UnicodeUTF8))
        self.verticalLayout_2 = QtGui.QVBoxLayout(SteppableGenerator)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(SteppableGenerator)
        self.label_2.setText(QtWidgets.QApplication.translate("SteppableGenerator", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Steppeble Will be registered in :</span></p></body></html>", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.mainScriptLB = QtGui.QLabel(SteppableGenerator)
        self.mainScriptLB.setText(QtWidgets.QApplication.translate("SteppableGenerator", "TextLabel", None, QtWidgets.QApplication.UnicodeUTF8))
        self.mainScriptLB.setObjectName(_fromUtf8("mainScriptLB"))
        self.verticalLayout.addWidget(self.mainScriptLB)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(SteppableGenerator)
        self.label.setText(QtWidgets.QApplication.translate("SteppableGenerator", "SteppableName", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.steppebleNameLE = QtGui.QLineEdit(SteppableGenerator)
        self.steppebleNameLE.setObjectName(_fromUtf8("steppebleNameLE"))
        self.gridLayout.addWidget(self.steppebleNameLE, 0, 1, 1, 2)
        self.label_3 = QtGui.QLabel(SteppableGenerator)
        self.label_3.setText(QtWidgets.QApplication.translate("SteppableGenerator", "Call Frequency", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.freqSB = QtGui.QSpinBox(SteppableGenerator)
        self.freqSB.setMinimum(1)
        self.freqSB.setMaximum(10000)
        self.freqSB.setSingleStep(1)
        self.freqSB.setProperty("value", 1)
        self.freqSB.setObjectName(_fromUtf8("freqSB"))
        self.gridLayout.addWidget(self.freqSB, 1, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.groupBox = QtGui.QGroupBox(SteppableGenerator)
        self.groupBox.setTitle(QtWidgets.QApplication.translate("SteppableGenerator", "Steppable Type", None, QtWidgets.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.genericLB = QtGui.QRadioButton(self.groupBox)
        self.genericLB.setText(QtWidgets.QApplication.translate("SteppableGenerator", "Generic", None, QtWidgets.QApplication.UnicodeUTF8))
        self.genericLB.setChecked(True)
        self.genericLB.setObjectName(_fromUtf8("genericLB"))
        self.horizontalLayout.addWidget(self.genericLB)
        self.mitosisRB = QtGui.QRadioButton(self.groupBox)
        self.mitosisRB.setText(QtWidgets.QApplication.translate("SteppableGenerator", "Mitosis", None, QtWidgets.QApplication.UnicodeUTF8))
        self.mitosisRB.setObjectName(_fromUtf8("mitosisRB"))
        self.horizontalLayout.addWidget(self.mitosisRB)
        self.clusterMitosisRB = QtGui.QRadioButton(self.groupBox)
        self.clusterMitosisRB.setText(QtWidgets.QApplication.translate("SteppableGenerator", "Cluster Mitosis", None, QtWidgets.QApplication.UnicodeUTF8))
        self.clusterMitosisRB.setObjectName(_fromUtf8("clusterMitosisRB"))
        self.horizontalLayout.addWidget(self.clusterMitosisRB)
        self.runBeforeMCSRB = QtGui.QRadioButton(self.groupBox)
        self.runBeforeMCSRB.setText(QtWidgets.QApplication.translate("SteppableGenerator", "Run Before MCS (secretion)", None, QtWidgets.QApplication.UnicodeUTF8))
        self.runBeforeMCSRB.setObjectName(_fromUtf8("runBeforeMCSRB"))
        self.horizontalLayout.addWidget(self.runBeforeMCSRB)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(SteppableGenerator)
        self.groupBox_2.setToolTip(QtWidgets.QApplication.translate("SteppableGenerator", "You can add extra visualization fields here.\n"
"The fields will be managed from Python", None, QtWidgets.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("SteppableGenerator", "Extra Visualization Fields", None, QtWidgets.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.vectorCB = QtGui.QCheckBox(self.groupBox_2)
        self.vectorCB.setText(QtWidgets.QApplication.translate("SteppableGenerator", "Vector", None, QtWidgets.QApplication.UnicodeUTF8))
        self.vectorCB.setObjectName(_fromUtf8("vectorCB"))
        self.horizontalLayout_2.addWidget(self.vectorCB)
        self.scalarCB = QtGui.QCheckBox(self.groupBox_2)
        self.scalarCB.setText(QtWidgets.QApplication.translate("SteppableGenerator", "Scalar", None, QtWidgets.QApplication.UnicodeUTF8))
        self.scalarCB.setObjectName(_fromUtf8("scalarCB"))
        self.horizontalLayout_2.addWidget(self.scalarCB)
        self.scalarCellLevelCB = QtGui.QCheckBox(self.groupBox_2)
        self.scalarCellLevelCB.setText(QtWidgets.QApplication.translate("SteppableGenerator", "Scalar Cell Level", None, QtWidgets.QApplication.UnicodeUTF8))
        self.scalarCellLevelCB.setObjectName(_fromUtf8("scalarCellLevelCB"))
        self.horizontalLayout_2.addWidget(self.scalarCellLevelCB)
        self.vectorCellLevelCB = QtGui.QCheckBox(self.groupBox_2)
        self.vectorCellLevelCB.setText(QtWidgets.QApplication.translate("SteppableGenerator", "Vector Cell Level", None, QtWidgets.QApplication.UnicodeUTF8))
        self.vectorCellLevelCB.setObjectName(_fromUtf8("vectorCellLevelCB"))
        self.horizontalLayout_2.addWidget(self.vectorCellLevelCB)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.okPB = QtGui.QPushButton(SteppableGenerator)
        self.okPB.setText(QtWidgets.QApplication.translate("SteppableGenerator", "OK", None, QtWidgets.QApplication.UnicodeUTF8))
        self.okPB.setObjectName(_fromUtf8("okPB"))
        self.horizontalLayout_3.addWidget(self.okPB)
        self.cancelPB = QtGui.QPushButton(SteppableGenerator)
        self.cancelPB.setText(QtWidgets.QApplication.translate("SteppableGenerator", "Cancel", None, QtWidgets.QApplication.UnicodeUTF8))
        self.cancelPB.setObjectName(_fromUtf8("cancelPB"))
        self.horizontalLayout_3.addWidget(self.cancelPB)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(SteppableGenerator)
        QtCore.QObject.connect(self.cancelPB, QtCore.SIGNAL(_fromUtf8("clicked()")), SteppableGenerator.reject)
        QtCore.QMetaObject.connectSlotsByName(SteppableGenerator)

    def retranslateUi(self, SteppableGenerator):
        pass

