from PyQt5.QtCore import pyqtSignal ,QObject 

from os.path import basename
from unrar import rarfile
from os import mkdir , walk
from shutil import rmtree , move
from subprocess import run
from zipfile import ZipFile
from requests import get
from os import startfile
import time
from os.path import exists
import os

class runner(QObject):
    installSignal = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        self.installSignal.connect(self.openfile)

    
    def openfile(self,listoffilelocation):
        try :
            for i in listoffilelocation :
                if "crack" not in i and "patch" not in i:
                    try :
                        startfile(i)  # Here, we run the first file we found for convenience, but in general, if we have several files, it can be shown to the user to choose.
                    except :
                        pass
        except Exception as e :
            print(e)

