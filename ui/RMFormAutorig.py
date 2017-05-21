# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Autorig.ui'
#
# Created: Mon Oct 31 15:31:43 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(234, 172)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.AutoRigTab = QtGui.QTabWidget(Form)
        self.AutoRigTab.setObjectName("AutoRigTab")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.heightLabel = QtGui.QLabel(self.tab)
        self.heightLabel.setMinimumSize(QtCore.QSize(20, 0))
        self.heightLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.heightLabel.setTextFormat(QtCore.Qt.PlainText)
        self.heightLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.heightLabel.setObjectName("heightLabel")
        self.horizontalLayout.addWidget(self.heightLabel)
        self.HeightSpnBox = QtGui.QDoubleSpinBox(self.tab)
        self.HeightSpnBox.setMaximum(1000000.0)
        self.HeightSpnBox.setProperty("value", 75.0)
        self.HeightSpnBox.setObjectName("HeightSpnBox")
        self.horizontalLayout.addWidget(self.HeightSpnBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.CreateReferencePointsBtn = QtGui.QPushButton(self.tab)
        self.CreateReferencePointsBtn.setObjectName("CreateReferencePointsBtn")
        self.verticalLayout.addWidget(self.CreateReferencePointsBtn)
        self.MirrorSelectionBtn = QtGui.QPushButton(self.tab)
        self.MirrorSelectionBtn.setObjectName("MirrorSelectionBtn")
        self.verticalLayout.addWidget(self.MirrorSelectionBtn)
        self.CreateRigBtn = QtGui.QPushButton(self.tab)
        self.CreateRigBtn.setObjectName("CreateRigBtn")
        self.verticalLayout.addWidget(self.CreateRigBtn)
        self.AutoRigTab.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SkeletonHandsBtn = QtGui.QPushButton(self.tab_2)
        self.SkeletonHandsBtn.setObjectName("SkeletonHandsBtn")
        self.verticalLayout_2.addWidget(self.SkeletonHandsBtn)
        self.supportScaleRigBtn = QtGui.QPushButton(self.tab_2)
        self.supportScaleRigBtn.setObjectName("supportScaleRigBtn")
        self.verticalLayout_2.addWidget(self.supportScaleRigBtn)
        self.feetOrientationBtn = QtGui.QPushButton(self.tab_2)
        self.feetOrientationBtn.setObjectName("feetOrientationBtn")
        self.verticalLayout_2.addWidget(self.feetOrientationBtn)
        self.AutoRigTab.addTab(self.tab_2, "")
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ClavicleSpaceSwitchBtn = QtGui.QPushButton(self.tab_5)
        self.ClavicleSpaceSwitchBtn.setObjectName("ClavicleSpaceSwitchBtn")
        self.verticalLayout_4.addWidget(self.ClavicleSpaceSwitchBtn)
        self.PoleVectorBtn = QtGui.QPushButton(self.tab_5)
        self.PoleVectorBtn.setObjectName("PoleVectorBtn")
        self.verticalLayout_4.addWidget(self.PoleVectorBtn)
        self.label = QtGui.QLabel(self.tab_5)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.AutoRigTab.addTab(self.tab_5, "")
        self.verticalLayout_3.addWidget(self.AutoRigTab)

        self.retranslateUi(Form)
        self.AutoRigTab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.heightLabel.setText(QtGui.QApplication.translate("Form", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.CreateReferencePointsBtn.setText(QtGui.QApplication.translate("Form", "Create Reference Points", None, QtGui.QApplication.UnicodeUTF8))
        self.MirrorSelectionBtn.setText(QtGui.QApplication.translate("Form", "Mirror Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.CreateRigBtn.setText(QtGui.QApplication.translate("Form", "CreateRig", None, QtGui.QApplication.UnicodeUTF8))
        self.AutoRigTab.setTabText(self.AutoRigTab.indexOf(self.tab), QtGui.QApplication.translate("Form", "AutoRig", None, QtGui.QApplication.UnicodeUTF8))
        self.SkeletonHandsBtn.setText(QtGui.QApplication.translate("Form", "Skeleton Hands", None, QtGui.QApplication.UnicodeUTF8))
        self.supportScaleRigBtn.setText(QtGui.QApplication.translate("Form", "Support Scale Rig", None, QtGui.QApplication.UnicodeUTF8))
        self.feetOrientationBtn.setText(QtGui.QApplication.translate("Form", "Correct Feet Orientation", None, QtGui.QApplication.UnicodeUTF8))
        self.AutoRigTab.setTabText(self.AutoRigTab.indexOf(self.tab_2), QtGui.QApplication.translate("Form", "Snipets", None, QtGui.QApplication.UnicodeUTF8))
        self.ClavicleSpaceSwitchBtn.setText(QtGui.QApplication.translate("Form", "Clavicle Space Switch", None, QtGui.QApplication.UnicodeUTF8))
        self.PoleVectorBtn.setText(QtGui.QApplication.translate("Form", "Correct P Vector Orient", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "All deprecated snippets are all ready\n"
" included on the autorig default creation", None, QtGui.QApplication.UnicodeUTF8))
        self.AutoRigTab.setTabText(self.AutoRigTab.indexOf(self.tab_5), QtGui.QApplication.translate("Form", "Deprecated", None, QtGui.QApplication.UnicodeUTF8))
