import sys
import maya.cmds as cmds
import maya.OpenMayaUI as mui
from PySide import QtGui, QtCore
from shiboken import wrapInstance
import maya.mel as mel
import os
from RMPY import RMUncategorized
from RMPY.ui import RMFormVisibilityTool
from RMPY.AutoRig import RMVisibilitySwitch
from RMPY import RMNameConvention
reload(RMVisibilitySwitch)

def getMayaWindow():
    ptr = mui.MQtUtil.mainWindow()
    return wrapInstance(long(ptr), QtGui.QMainWindow)

class Main(QtGui.QDialog):
    def __init__(self, NameConv=None, parent=None):
        super(Main,self).__init__(parent = getMayaWindow())
        self.ui = RMFormVisibilityTool.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('Visibility Switch')
        self.VisSw = RMVisibilitySwitch.RMVisibilitySwitch()
        self.ui.LoadSelectionAsCntrlObjPushBtn.clicked.connect(self.LoadSelectionAsCntrlObjPushBtnClicked)
        self.ui.CreateVisibilitySwitchBtn.clicked.connect(self.CreateVisibilitySwitchBtnPressed)
        self.ui.RemoveFromVisibilityBtn.clicked.connect (self.RemoveSelectedBtnPressed)
        
        self.ui.AddToVisibilitySwitchBtn.clicked.connect(self.AddToVisibilitySwitchBtnPressed)
        self.ui.ObjectSpaceListView.itemClicked.connect(self.UpdateAffectedObjectList)
        
        self.ui.RemoveListSelectedBtn.clicked.connect(self.RemoveListSelectedBtnPressed)
        self.ui.ConstrainedObjectListView.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.ui.RemoveEnumBtn.clicked.connect ( self.RemoveEnumBtnClicked )

    def LoadSelectionAsCntrlObjPushBtnClicked (self):
        Object = cmds.ls(selection=True)[0]
        self.ui.ControllineEdit.setText(Object)
        self.UpdateVisibilitySwitchObjectList()
        
    def UpdateVisibilitySwitchObjectList(self):
        self.ui.ObjectSpaceListView.clear()
        Object = self.ui.ControllineEdit.text()
        EnumList = self.VisSw.GetEnumVisibilityList(Object)
        for eachEnum in EnumList:
            self.ui.ObjectSpaceListView.addItem(eachEnum)
        print len(EnumList) 
        if len(EnumList) >= 1:
            self.ui.ObjectSpaceListView.setCurrentRow(0)
            self.UpdateAffectedObjectList()
        else :
            self.ui.ConstrainedObjectListView.clear()
    def UpdateAffectedObjectList(self):
        controlObject = self.ui.ControllineEdit.text()
        VisibilitySwitch = self.ui.ObjectSpaceListView.selectedItems()[0].text()
        AffectedObjects = self.VisSw.GetAfectedObjectsList ( controlObject, VisibilitySwitch )
        self.ui.ConstrainedObjectListView.clear()
        if AffectedObjects:
            for eachObject in AffectedObjects:
                self.ui.ConstrainedObjectListView.addItem(eachObject)

    def CreateVisibilitySwitchBtnPressed(self):
        VisibilityList = self.VisSw.GetEnumVisibilityList(self.ui.ControllineEdit.text())
        if not self.ui.VisibilityNameTxt.text() in  VisibilityList:
            #self.VisSw.AddEnumParameters( self.ui.ControllineEdit.text,VisibilitySwitch = self.ui.VisibilityNameTxt.text())
            Objects = cmds.ls(selection = True , type ="transform" )
            self.VisSw.ConstraintVisibility(Objects , self.ui.ControllineEdit.text(), VisibilitySwitch = self.ui.VisibilityNameTxt.text())
        self.UpdateVisibilitySwitchObjectList()
        self.UpdateAffectedObjectList()

    def AddToVisibilitySwitchBtnPressed (self):
        SelectedItems = self.ui.ObjectSpaceListView.selectedItems()
        if len(SelectedItems) > 0:
            SelectedItem = SelectedItems[0]
        controlObject = self.ui.ControllineEdit.text()
        Objects = cmds.ls(selection = True , type ="transform" )
        self.VisSw.AddAffectedObject ( controlObject, Objects , VisibilitySwitch = SelectedItem.text() )
        self.UpdateAffectedObjectList()

    def RemoveListSelectedBtnPressed (self):
        selectedItems = self.ui.ConstrainedObjectListView.selectedItems()
        controlObject = self.ui.ControllineEdit.text()
        VisibilitySwitch = self.ui.ObjectSpaceListView.selectedItems()[0].text()
        UnlinkedObjects = []
        for eachItem in selectedItems:
            UnlinkedObjects.append (eachItem.text())

        self.VisSw.RemoveAffectedObject ( controlObject, UnlinkedObjects , VisibilitySwitch = VisibilitySwitch )
        self.UpdateAffectedObjectList()

    def RemoveSelectedBtnPressed (self):
        controlObject = self.ui.ControllineEdit.text()
        VisibilitySwitch = self.ui.ObjectSpaceListView.selectedItems()[0].text()
        Objects = cmds.ls(selection = True , type ="transform" )
        self.VisSw.RemoveAffectedObject ( controlObject, Objects , VisibilitySwitch = VisibilitySwitch )
        self.UpdateAffectedObjectList()
    
    def RemoveEnumBtnClicked (self):
        cmds.deleteAttr ("%s.%s"%(self.ui.ControllineEdit.text() ,self.ui.ObjectSpaceListView.selectedItems()[0].text()))
        self.UpdateVisibilitySwitchObjectList()

if __name__ == '__main__':
    w = Main()
    w.show()