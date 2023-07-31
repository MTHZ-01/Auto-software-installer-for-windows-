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

class extractor(QObject):
    extractionComplete_directorySignal = pyqtSignal(list)
    startExtractSignal = pyqtSignal(list)

    def __init__(self,siteName):
        super().__init__()
        
        self.directory = None
        self.siteName = siteName
        self.startExtractSignal.connect(self.extract)


    def extract(self ,listofpath):

        sitename = self.siteName
        print("extractor: operation started . . .")
        print(listofpath)
        print(sitename)
        if len(listofpath) == 1 :
            total_directory = listofpath[0]
            ####### 2 creat a folder in Downloads directory and remove the last (not so important)
            flag = True
            i = 0
            while flag :
                path = f'.\\{total_directory[:-4]}_{i}'
                if exists(path) :
                    flag = True
                    i += 1
                else :
                    mkdir(path)
                    flag = False

            ####### 3 Extract files

            suffix = total_directory[-3:]
            try :
                if sitename == "yasdl" :  # in this part we can add another password we want
                    password = "www.yasdl.com"
                elif sitename == "sarzmindownload" :
                    password = "www.sarzamindownload.com"
                elif sitename == "www.p30download.ir" :
                    password = "www.p30download.com"
                elif sitename == "www.soft98.ir" :
                    password = "soft98.ir"
                if suffix == "exe" :
                    move(total_directory , path)            
                elif suffix == "rar" :
                    with rarfile.RarFile(total_directory , "r" , pwd=password) as rf:
                        files = rf.namelist()
                        rf.extractall(f"{path}")
                elif suffix == "zip" :
                    with ZipFile(total_directory , 'r') as zip:
                        zip.extractall(f"{path}" , pwd= bytes(password , 'utf-8'))
            except Exception as a :
                print(a)


            ####### 4 find the .exe and .msi file

            dir_path = path
            res = []
            for (dir_path, dir_names, file_names) in walk(dir_path):
                res += [[file_names , dir_path]]
            q = []
            for i in res :
                for j in i[0] :
                    x = j
                    if j[-3:].lower() == "exe" or j[-3:].lower() == "msi" :
                        k = i[1]
                        q += [f"{k}\\{j}"]
            print("extractor: Extraction has been completed successfully")
            self.extractionComplete_directorySignal.emit(q)    



        else :

            ####### 2 creat a folder in Downloads directory and remove the last (not so important)

            total_directory = listofpath[0]
            All_directory = listofpath.copy()
            if "part" in total_directory :
                parts = total_directory.rsplit("part", 1)
                total_directory = parts[0]
                flag = True

                while flag :
                    if total_directory[-1] == "_" or total_directory[-1] == "-" :
                        total_directory = total_directory[:-1]
                        if total_directory[-1] == "_" or total_directory[-1] == "-" :
                            flag = True
                    else :
                        flag = False
            else :
                common_chars = ""
                for chars in zip(*All_directory):
                    if all(char == chars[0] for char in chars):
                        common_chars += chars[0]
                    else:
                        break
                total_directory = common_chars

            flag = True
            i = 0
            while flag :
                path = f'.\\{total_directory}_{i}'
                if exists(path) :
                    flag = True
                    i += 1
                else :
                    mkdir(path)
                    flag = False

            # ####### 3 Extract files

            if sitename == "yasdl.com" :  # in this part we can add another password we want
                password = "www.yasdl.com"
            elif sitename == "sarzamindownload.com" :
                password = "www.sarzamindownload.com"
            elif sitename == "p30download.ir" :
                password = "www.p30download.com"
            elif sitename == "soft98.ir" :
                password = "soft98.ir"
            
            file_path = min(All_directory)
            with rarfile.RarFile(file_path, "r" , pwd=password) as rf:
                rf.extractall(path)
            # print("extractor: Extraction compelete!")
            ####### 4 find the .exe and .msi file

            dir_path = path
            res = []
            for (dir_path, dir_names, file_names) in walk(dir_path):
                res += [[file_names , dir_path]]
            q = []
            for i in res :
                for j in i[0] :
                    x = j
                    if j[-3:].lower() == "exe" or j[-3:].lower() == "msi" :
                        k = i[1]
                        q += [f"{k}\\{j}"]
            print("extractor: Extraction has been completed successfully")
            self.extractionComplete_directorySignal.emit(q)    


