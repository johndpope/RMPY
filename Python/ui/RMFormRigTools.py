# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RMINTRigTools.ui'
#
# Created: Thu Aug 04 16:19:50 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(864, 797)
        self.horizontalLayout_4 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.RenameTool = QtGui.QPushButton(Form)
        self.RenameTool.setObjectName("RenameTool")
        self.verticalLayout_4.addWidget(self.RenameTool)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.LabelPoint = QtGui.QLabel(Form)
        self.LabelPoint.setObjectName("LabelPoint")
        self.verticalLayout_5.addWidget(self.LabelPoint)
        self.IKOnSelection = QtGui.QPushButton(Form)
        self.IKOnSelection.setObjectName("IKOnSelection")
        self.verticalLayout_5.addWidget(self.IKOnSelection)
        self.FKOnSelection = QtGui.QPushButton(Form)
        self.FKOnSelection.setObjectName("FKOnSelection")
        self.verticalLayout_5.addWidget(self.FKOnSelection)
        self.JointsOnPoints = QtGui.QPushButton(Form)
        self.JointsOnPoints.setObjectName("JointsOnPoints")
        self.verticalLayout_5.addWidget(self.JointsOnPoints)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.GroupCreationLabel = QtGui.QLabel(Form)
        self.GroupCreationLabel.setObjectName("GroupCreationLabel")
        self.verticalLayout_2.addWidget(self.GroupCreationLabel)
        self.CreateChildGroup = QtGui.QPushButton(Form)
        self.CreateChildGroup.setObjectName("CreateChildGroup")
        self.verticalLayout_2.addWidget(self.CreateChildGroup)
        self.CreateParentGroup = QtGui.QPushButton(Form)
        self.CreateParentGroup.setObjectName("CreateParentGroup")
        self.verticalLayout_2.addWidget(self.CreateParentGroup)
        spacerItem = QtGui.QSpacerItem(10, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.AlignLabel = QtGui.QLabel(Form)
        self.AlignLabel.setObjectName("AlignLabel")
        self.verticalLayout.addWidget(self.AlignLabel)
        self.AlignRotation = QtGui.QPushButton(Form)
        self.AlignRotation.setObjectName("AlignRotation")
        self.verticalLayout.addWidget(self.AlignRotation)
        self.AlignPosition = QtGui.QPushButton(Form)
        self.AlignPosition.setObjectName("AlignPosition")
        self.verticalLayout.addWidget(self.AlignPosition)
        self.AlignAll = QtGui.QPushButton(Form)
        self.AlignAll.setObjectName("AlignAll")
        self.verticalLayout.addWidget(self.AlignAll)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.SkiningToolslabel = QtGui.QLabel(Form)
        self.SkiningToolslabel.setObjectName("SkiningToolslabel")
        self.verticalLayout_3.addWidget(self.SkiningToolslabel)
        self.ListConnectedJoints = QtGui.QPushButton(Form)
        self.ListConnectedJoints.setObjectName("ListConnectedJoints")
        self.verticalLayout_3.addWidget(self.ListConnectedJoints)
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        self.SelectJoints = QtGui.QPushButton(Form)
        self.SelectJoints.setObjectName("SelectJoints")
        self.verticalLayout_3.addWidget(self.SelectJoints)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.labelShapeControls = QtGui.QLabel(Form)
        self.labelShapeControls.setObjectName("labelShapeControls")
        self.verticalLayout_7.addWidget(self.labelShapeControls)
        self.SCCombineButton = QtGui.QPushButton(Form)
        self.SCCombineButton.setObjectName("SCCombineButton")
        self.verticalLayout_7.addWidget(self.SCCombineButton)
        self.ConstShapeLblBtn = QtGui.QPushButton(Form)
        self.ConstShapeLblBtn.setObjectName("ConstShapeLblBtn")
        self.verticalLayout_7.addWidget(self.ConstShapeLblBtn)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Attributeslabel = QtGui.QLabel(Form)
        self.Attributeslabel.setObjectName("Attributeslabel")
        self.verticalLayout_8.addWidget(self.Attributeslabel)
        self.AttributeTransferBtn = QtGui.QPushButton(Form)
        self.AttributeTransferBtn.setToolTip("")
        self.AttributeTransferBtn.setObjectName("AttributeTransferBtn")
        self.verticalLayout_8.addWidget(self.AttributeTransferBtn)
        self.MiscLabel = QtGui.QLabel(Form)
        self.MiscLabel.setObjectName("MiscLabel")
        self.verticalLayout_8.addWidget(self.MiscLabel)
        self.ExtractGeoBtn = QtGui.QPushButton(Form)
        self.ExtractGeoBtn.setObjectName("ExtractGeoBtn")
        self.verticalLayout_8.addWidget(self.ExtractGeoBtn)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.RenameTool.setText(QtGui.QApplication.translate("Form", "Rename Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelPoint.setText(QtGui.QApplication.translate("Form", "Create Based on Points", None, QtGui.QApplication.UnicodeUTF8))
        self.IKOnSelection.setToolTip(QtGui.QApplication.translate("Form", "Select some locators in order to create an FK Control", None, QtGui.QApplication.UnicodeUTF8))
        self.IKOnSelection.setText(QtGui.QApplication.translate("Form", "IK on selection", None, QtGui.QApplication.UnicodeUTF8))
        self.FKOnSelection.setToolTip(QtGui.QApplication.translate("Form", "Select some locators in order to create an FK Control", None, QtGui.QApplication.UnicodeUTF8))
        self.FKOnSelection.setText(QtGui.QApplication.translate("Form", "FK on selection", None, QtGui.QApplication.UnicodeUTF8))
        self.JointsOnPoints.setText(QtGui.QApplication.translate("Form", "CreateJointsOnPoints", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupCreationLabel.setText(QtGui.QApplication.translate("Form", "Group Creation", None, QtGui.QApplication.UnicodeUTF8))
        self.CreateChildGroup.setText(QtGui.QApplication.translate("Form", "Create Child Group", None, QtGui.QApplication.UnicodeUTF8))
        self.CreateParentGroup.setText(QtGui.QApplication.translate("Form", "Create Parent Group", None, QtGui.QApplication.UnicodeUTF8))
        self.AlignLabel.setText(QtGui.QApplication.translate("Form", "Align", None, QtGui.QApplication.UnicodeUTF8))
        self.AlignRotation.setText(QtGui.QApplication.translate("Form", "AlignRotation", None, QtGui.QApplication.UnicodeUTF8))
        self.AlignPosition.setText(QtGui.QApplication.translate("Form", "AlignPosition", None, QtGui.QApplication.UnicodeUTF8))
        self.AlignAll.setText(QtGui.QApplication.translate("Form", "Align Pos & Rot", None, QtGui.QApplication.UnicodeUTF8))
        self.SkiningToolslabel.setText(QtGui.QApplication.translate("Form", "SkiningTools", None, QtGui.QApplication.UnicodeUTF8))
        self.ListConnectedJoints.setText(QtGui.QApplication.translate("Form", "List Skined Joints", None, QtGui.QApplication.UnicodeUTF8))
        self.SelectJoints.setText(QtGui.QApplication.translate("Form", "Select Joints", None, QtGui.QApplication.UnicodeUTF8))
        self.labelShapeControls.setText(QtGui.QApplication.translate("Form", "Shape Controls", None, QtGui.QApplication.UnicodeUTF8))
        self.SCCombineButton.setText(QtGui.QApplication.translate("Form", "Combine", None, QtGui.QApplication.UnicodeUTF8))
        self.ConstShapeLblBtn.setText(QtGui.QApplication.translate("Form", "Const Shape Lbl", None, QtGui.QApplication.UnicodeUTF8))
        self.Attributeslabel.setText(QtGui.QApplication.translate("Form", "Attributes", None, QtGui.QApplication.UnicodeUTF8))
        self.AttributeTransferBtn.setText(QtGui.QApplication.translate("Form", "Move Attributes", None, QtGui.QApplication.UnicodeUTF8))
        self.MiscLabel.setText(QtGui.QApplication.translate("Form", "Misc", None, QtGui.QApplication.UnicodeUTF8))
        self.ExtractGeoBtn.setText(QtGui.QApplication.translate("Form", "ExtractGeometry", None, QtGui.QApplication.UnicodeUTF8))

