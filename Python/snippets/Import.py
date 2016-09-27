import logging
default = "none"
try:
    from PyQt4 import uic
    from PyQt4.QtCore import *
    from PyQt4.QtGui  import * 
    from PyQt4 import QtGui  
    import sip
    default = "pyqt4"
    logging.Logger.manager.loggerDict["PyQt4.uic.uiparser"].setLevel(logging.CRITICAL)
    logging.Logger.manager.loggerDict["PyQt4.uic.properties"].setLevel(logging.CRITICAL)
except: 
    try:
        import xml.etree.ElementTree as xml
        from cStringIO import StringIO
        import pysideuic, shiboken
        from PySide.QtGui  import * 
        from PySide.QtCore import *
        from PySide import QtGui
        default = "pyside"
        logging.Logger.manager.loggerDict["pysideuic.uiparser"].setLevel(logging.CRITICAL)
        logging.Logger.manager.loggerDict["pysideuic.properties"].setLevel(logging.CRITICAL)
    except:
        try:
            import xml.etree.ElementTree as xml
            from cStringIO import StringIO
            import shiboken2 as shiboken
            import pyside2uic as pysideuic
            from PySide2.QtGui     import * 
            from PySide2.QtCore    import *
            from PySide2.QtWidgets import *
            from PySide2 import QtGui
            default = "pyside2"
            logging.Logger.manager.loggerDict["pyside2uic.uiparser"].setLevel(logging.CRITICAL)
            logging.Logger.manager.loggerDict["pyside2uic.properties"].setLevel(logging.CRITICAL)
        except:
            print "PySide(2) and PyQt4 not found"

def loadUiType( uiFile ):
    if default ==  "pyqt4":
        form_class, base_class =  uic.loadUiType( uiFile )
    else:
        parsed = xml.parse( uiFile )
        widget_class = parsed.find( 'widget' ).get( 'class' )
        form_class = parsed.find( 'class' ).text

        with open( uiFile, 'r' ) as f:
            o = StringIO()
            frame = {}

            pysideuic.compileUi( f, o, indent=0 )
            pyc = compile( o.getvalue(), '<string>', 'exec' )
            exec pyc in frame

            form_class = frame[ 'Ui_%s'%form_class ]
            base_class = eval( '%s'%widget_class )
    return form_class, base_class

def wrapinstance( ptr, base=None ):
    if ptr is None:
        return None
    ptr = long( ptr ) 
    if globals().has_key( 'shiboken' ):
        if base is None:
            qObj = shiboken.wrapInstance( long( ptr ), QObject )
            metaObj = qObj.metaObject()
            cls = metaObj.className()
            superCls = metaObj.superClass().className()
            if hasattr( QtGui, cls ):
                base = getattr( QtGui, cls )
            elif hasattr( QtGui, superCls ):
                base = getattr( QtGui, superCls ) 
            else:
                base = QWidget
        return shiboken.wrapInstance( long( ptr ), base )
    elif globals().has_key( 'sip' ):
        base = QObject
        return sip.wrapinstance( long( ptr ), base )
    else:
        return None