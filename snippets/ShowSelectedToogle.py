import maya.cmds as cmds
currentPanel = cmds.getPanel(withFocus=True)
allPannels   = cmds.getPanel(type='modelPanel')

if currentPanel in allPannels:
    state = cmds.isolateSelect ( currentPanel, q=True, state = True)
    if state:
        cmds.isolateSelect ( currentPanel, state = False)

    else:
        cmds.isolateSelect ( currentPanel, state = True)
        cmds.isolateSelect(currentPanel,addSelected=True)
else:
    
    state = cmds.isolateSelect ( allPannels[0], q=True, state = True)
    for eachPanel in allPannels:
        if state:
            cmds.isolateSelect ( eachPanel, state = False)
        else:
            cmds.isolateSelect ( eachPanel, state = True)
            cmds.isolateSelect(eachPanel, addSelected=True)

