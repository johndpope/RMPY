import RMNameConvention
NameConv  = RMNameConvention.RMNameConvention()
reload (RMNameConvention)
selection = cmds.ls(selection=True)
for i in selection:
	#NameConv.RMRenameNameInFormat(i, Side = "RH", System = "TorsoBelts")
	cmds.rename(i, "%s%s"%("ButterflyGirl_",i))
	#NameConv.RMRenameSetFromName( i , "RH","Side")
	NameConv.RMRenameSetFromName( i , "MD","Side")


