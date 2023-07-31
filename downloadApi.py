from api import getLinkAndForget
from PyQt5.QtCore import pyqtSignal ,QObject 
import json
import PyQt5

class scrapper(PyQt5.QtCore.QObject):
    finishedSignal = pyqtSignal()



    def __init__(self) -> None:

        super().__init__()

        # self.finishedSignal.connect(self.pr)


    def getJson(self,query):
        out = getLinkAndForget(query)

        return out
        self.finishedSignal.emit()
        

    
    def pr(self):
        print(self.json)



s = scrapper()
l = s.getJson("vlc")
print(l)