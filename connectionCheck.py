import requests
import threading
from PyQt5.QtCore import pyqtSignal ,QObject 
import subprocess
import time

import socket
class checkNet(QObject):
    serverUpSignal = pyqtSignal()
    serverDownSignal = pyqtSignal()
    def __init__(self,url):
        super().__init__()
        self.url = url


        # self.status()/


    def startCycle(self):
        
        while True:

            IPaddress=socket.gethostbyname(socket.gethostname())

                # Hardware status checking:



            if IPaddress=="127.0.0.1":

                self.serverDownSignal.emit()
            else:

                self.serverUpSignal.emit()
            # time.sleep(3)



# x = checkNet('')
