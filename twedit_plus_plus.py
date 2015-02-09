#!/usr/bin/env python
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *
from PyQt5.Qsci import *

import time

import sys



from CQt.CQApplication import CQApplication
from EditorWindow import EditorWindow
import dummy_application # used to switch away followed by switch to tweedit to ensure that menubar shows on some OSX systems on twedit startup

from DataSocketCommunicators import FileNameSender

import sys, os, errno, tempfile

from Messaging import stdMsg, dbgMsg, errMsg, setDebugging
# this globally enables/disables debug statements
setDebugging(0)


from windowsUtils import *

class Twedit(object):
    def __init__(self):
   
        import sys
        self.lockfile = os.path.normpath(tempfile.gettempdir() + '/' + os.path.basename(__file__) + '.lock')
        if sys.platform == 'win32':
            try:
                # file already exists, we try to remove (in case previous execution was interrupted)
                if(os.path.exists(self.lockfile)):
                    os.unlink(self.lockfile)
                self.fd =  os.open(self.lockfile, os.O_CREAT|os.O_EXCL|os.O_RDWR)
            except OSError, e:
                if e.errno == 13:
                    dbgMsg("Another instance is already running, quitting.")
                    raise
                    
                dbgMsg(e.errno)
                raise
        else: # non Windows
            import fcntl, sys
            
            try:
                self.fp = open(self.lockfile, 'w')
                fcntl.lockf(self.fp, fcntl.LOCK_EX | fcntl.LOCK_NB)                
            except IOError:
                dbgMsg("NON-WINDOWS PLATFORM Another instance is already running, quitting.")                
                raise OSError
    
    def __del__(self):
        import sys
        if sys.platform == 'win32':
            if hasattr(self, 'fd'):
                os.close(self.fd)
                os.unlink(self.lockfile)


    
    def main(self,argv):
        print 'INSIDE MAIN TWEDIT'

        #global mainWindow
        app = CQApplication(argv)
        
        qtVersion=str(QT_VERSION_STR).split('.') 
        import platform
        
        if platform.mac_ver()[0]!='' and qtVersion[1]>=2: # style sheets may not work properly for qt < 4.2
            app.setStyleSheet( "QDockWidget::close-button, QDockWidget::float-button { padding: 0px;icon-size: 24px;}")
        
        pixmap = QPixmap("icons/lizard-at-a-computer-small.png")
        print "pixmap=",pixmap
        splash = QSplashScreen(pixmap)
        splash.showMessage("Please wait.\nLoading Twedit++ ...",Qt.AlignLeft,  Qt.black)
        splash.show()        

        app.processEvents()
        
        #app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
        self.mainWindow = EditorWindow()
        self.mainWindow.setArgv(argv) # passing command line to the code

        self.mainWindow.show()
        
        splash.finish(self.mainWindow)

        app.postEvent(self.mainWindow, QFocusEvent(QEvent.FocusOut))

        self.mainWindow.processCommandLine()


#         self.mainWindow.menuBar().setNativeMenuBar(False)
        


        self.mainWindow.raise_() # to make sure on OSX window is in the foreground
        self.mainWindow.setFocus(False)
#         time.sleep(2)

        
#         self.mainWindow.menuBar().setNativeMenuBar(True)                
#         self.mainWindow.menuBar().setHidden(True)
        if sys.platform.startswith('win'):    
            import win32process
            self.mainWindow.setProcessId(win32process.GetCurrentProcessId())
            
#         self.mainWindow.minimize() # to make sure on OSX window is in the foreground
#         self.mainWindow.setFocus(False) # to make sure on OSX window is in the foreground
#         self.mainWindow.setFocus(True) # to make sure on OSX window is in the foreground
#         QTimer.singleShot(60, self.mainWindow, self.mainWindow.createMenus);

        # on some Mac, to ensure that menu bar is activated at startup we need to launch
        # anothr app that steals focus from twedit and immediately close it to return focus to twedit
        # this switch away and switch to operation restores proper Mac style menu bar. This is most likely a bug in PyQt5.4 
        # but untill this is resolved we need to do this "trick"
        if platform.mac_ver()[0] != '':             
            QTimer.singleShot(60,self.startDummyApp);

        app.exec_()

    def startDummyApp(self):

        import subprocess
        subprocess.call(['python','dummy_application.py'])        

        


if __name__ == '__main__':

    try:
        twedit=Twedit()
    except OSError,e:
        dbgMsg("GOT OS ERROR")
        
           
        # argvSendSocket=QUdpSocket()
        for fileName in sys.argv[1:]: 
            datagram=fileName
            # argvSendSocket.writeDatagram(datagram,QHostAddress.LocalHost,47405)        
            fileSender=FileNameSender(datagram)  
            fileSender.send()
            
        if sys.platform.startswith('win'):    
            showTweditWindowInForeground()
        else:
            # notice, on linux you may have to change "focus stealing prevention level" setting to None in window behavior settings , to enable bringing windo to foreground 
            dbgMsg("NON-WINDOWS PLATFORM - TRY TO ACTIVATE WINDOW")
        
            
        sys.exit()    

    
    twedit.main(sys.argv[1:])
    
    