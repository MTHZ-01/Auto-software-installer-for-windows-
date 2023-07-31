import requests
from flask import Flask
import threading
import re
import sys
from flask import request, jsonify
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium import webdriver
import json
from PyQt5.QtCore import pyqtSignal ,QObject 

class server(QObject):
    serverDownSignal = pyqtSignal()
    jsonSignal = pyqtSignal(dict)
    def __init__(self,query,site = "sarzamin") -> None:
        super().__init__()
        self.query = query
        self.site = site
        try:
            print("Searching . . .")
            self.jsons = requests.get(f'http://localhost:5000/from{site}?query={query}').text
            print("Found !")

        
            print("this is json")
            print(self.jsons)
            self.jsonDict = json.loads(self.jsons)        
            self.jsonSignal.emit(self.jsonDict)

            print("put success")


            t = threading.Thread(target=self.manualScrapping)
            for i in self.jsonDict:
                if self.jsonDict[i][-1] == "1":
                    print("Trying to activate thread")
                    t.start()
                    break
            
        except :

            print("!!!! HERE !!!!")
            self.serverDownSignal.emit()
            return
        

    def manualScrapping(self):
        print("Updating bin files . . .")
        requests.put(f'http://127.0.0.1:5000/to{self.site}', data={"query": self.query})
