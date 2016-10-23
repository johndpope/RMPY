# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RMFormLaces.ui'
#
# Created: Wed Oct 19 13:43:49 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(349, 299)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.LacesGrpBx = QtGui.QGroupBox(Form)
        self.LacesGrpBx.setObjectName("LacesGrpBx")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.LacesGrpBx)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.LoadShapeBtn = QtGui.QPushButton(self.LacesGrpBx)
        self.LoadShapeBtn.setObjectName("LoadShapeBtn")
        self.verticalLayout_2.addWidget(self.LoadShapeBtn)
        self.CurrentShapeLbl = QtGui.QLabel(self.LacesGrpBx)
        self.CurrentShapeLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentShapeLbl.setObjectName("CurrentShapeLbl")
        self.verticalLayout_2.addWidget(self.CurrentShapeLbl)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.JointsOnCurve = QtGui.QLabel(self.LacesGrpBx)
        self.JointsOnCurve.setObjectName("JointsOnCurve")
        self.horizontalLayout.addWidget(self.JointsOnCurve)
        self.NumberOfJoints = QtGui.QSpinBox(self.LacesGrpBx)
        self.NumberOfJoints.setMinimumSize(QtCore.QSize(50, 0))
        self.NumberOfJoints.setMaximumSize(QtCore.QSize(50, 16777215))
        self.NumberOfJoints.setMinimum(2)
        self.NumberOfJoints.setProperty("value", 2)
        self.NumberOfJoints.setObjectName("NumberOfJoints")
        self.horizontalLayout.addWidget(self.NumberOfJoints)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.Mode = QtGui.QCheckBox(self.LacesGrpBx)
        self.Mode.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Mode.setCheckable(True)
        self.Mode.setChecked(False)
        self.Mode.setObjectName("Mode")
        self.verticalLayout_2.addWidget(self.Mode)
        self.CreateControlsBtn = QtGui.QPushButton(self.LacesGrpBx)
        self.CreateControlsBtn.setObjectName("CreateControlsBtn")
        self.verticalLayout_2.addWidget(self.CreateControlsBtn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.RebuildGrp = QtGui.QGroupBox(self.LacesGrpBx)
        self.RebuildGrp.setObjectName("RebuildGrp")
        self.verticalLayout = QtGui.QVBoxLayout(self.RebuildGrp)
        self.verticalLayout.setObjectName("verticalLayout")
        self.RebuildCurveChk = QtGui.QCheckBox(self.RebuildGrp)
        self.RebuildCurveChk.setObjectName("RebuildCurveChk")
        self.verticalLayout.addWidget(self.RebuildCurveChk)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.NumberofSpansLabel = QtGui.QLabel(self.RebuildGrp)
        self.NumberofSpansLabel.setObjectName("NumberofSpansLabel")
        self.horizontalLayout_6.addWidget(self.NumberofSpansLabel)
        self.NumberOfSpansSpnBx = QtGui.QSpinBox(self.RebuildGrp)
        self.NumberOfSpansSpnBx.setMinimumSize(QtCore.QSize(50, 0))
        self.NumberOfSpansSpnBx.setMaximumSize(QtCore.QSize(50, 16777215))
        self.NumberOfSpansSpnBx.setMinimum(4)
        self.NumberOfSpansSpnBx.setObjectName("NumberOfSpansSpnBx")
        self.horizontalLayout_6.addWidget(self.NumberOfSpansSpnBx)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.CurrentShapeControlsLbl = QtGui.QLabel(self.RebuildGrp)
        self.CurrentShapeControlsLbl.setText("")
        self.CurrentShapeControlsLbl.setObjectName("CurrentShapeControlsLbl")
        self.verticalLayout.addWidget(self.CurrentShapeControlsLbl)
        self.horizontalLayout_2.addWidget(self.RebuildGrp)
        self.verticalLayout_3.addWidget(self.LacesGrpBx)
        self.progresivePathGrpBx = QtGui.QGroupBox(Form)
        self.progresivePathGrpBx.setObjectName("progresivePathGrpBx")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.progresivePathGrpBx)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.PathCurveBtn = QtGui.QPushButton(self.progresivePathGrpBx)
        self.PathCurveBtn.setObjectName("PathCurveBtn")
        self.horizontalLayout_4.addWidget(self.PathCurveBtn)
        self.PathCurveLbl = QtGui.QLabel(self.progresivePathGrpBx)
        self.PathCurveLbl.setText("")
        self.PathCurveLbl.setObjectName("PathCurveLbl")
        self.horizontalLayout_4.addWidget(self.PathCurveLbl)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ControlCurveBtn = QtGui.QPushButton(self.progresivePathGrpBx)
        self.ControlCurveBtn.setObjectName("ControlCurveBtn")
        self.horizontalLayout_5.addWidget(self.ControlCurveBtn)
        self.ControlCurveLbl = QtGui.QLabel(self.progresivePathGrpBx)
        self.ControlCurveLbl.setText("")
        self.ControlCurveLbl.setObjectName("ControlCurveLbl")
        self.horizontalLayout_5.addWidget(self.ControlCurveLbl)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.pushButton = QtGui.QPushButton(self.progresivePathGrpBx)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_3.addWidget(self.progresivePathGrpBx)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.LacesGrpBx.setTitle(QtGui.QApplication.translate("Form", "Lace creation", None, QtGui.QApplication.UnicodeUTF8))
        self.LoadShapeBtn.setText(QtGui.QApplication.translate("Form", "Load Selected Shape", None, QtGui.QApplication.UnicodeUTF8))
        self.CurrentShapeLbl.setText(QtGui.QApplication.translate("Form", "No Shape Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.JointsOnCurve.setText(QtGui.QApplication.translate("Form", "Joints On curve", None, QtGui.QApplication.UnicodeUTF8))
        self.Mode.setText(QtGui.QApplication.translate("Form", "Single orient object", None, QtGui.QApplication.UnicodeUTF8))
        self.CreateControlsBtn.setText(QtGui.QApplication.translate("Form", "Create Controls", None, QtGui.QApplication.UnicodeUTF8))
        self.RebuildGrp.setTitle(QtGui.QApplication.translate("Form", "Rebuild curve", None, QtGui.QApplication.UnicodeUTF8))
        self.RebuildCurveChk.setText(QtGui.QApplication.translate("Form", "rebuild curve", None, QtGui.QApplication.UnicodeUTF8))
        self.NumberofSpansLabel.setText(QtGui.QApplication.translate("Form", "number of Controls", None, QtGui.QApplication.UnicodeUTF8))
        self.progresivePathGrpBx.setTitle(QtGui.QApplication.translate("Form", "Progresive Path", None, QtGui.QApplication.UnicodeUTF8))
        self.PathCurveBtn.setText(QtGui.QApplication.translate("Form", "Load Path Curve :", None, QtGui.QApplication.UnicodeUTF8))
        self.ControlCurveBtn.setText(QtGui.QApplication.translate("Form", "Load Control Curve:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Progresive link to Path", None, QtGui.QApplication.UnicodeUTF8))

