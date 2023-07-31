import pickle
from PyQt5.QtCore import pyqtSignal ,QObject
import os

class saveProgress:
    def __init__(self,obj):
        print("Saving . . .")
        try:

            File = open("downloadResults.bin" ,"rb") 
            d = pickle.load(File)
            for i in obj:
                d[i] = obj[i]
            File.close()
                

            File = open("downloadResults.bin" ,"wb") 
            pickle.dump(d,File)

        except:
            with open("downloadResults.bin" ,"wb") as File:

                
                pickle.dump(obj, File)

        print("finall object has been successfully saved!")

class openProgress(QObject):
    fileOpenedSignal = pyqtSignal(dict)
    fileProblemSignal = pyqtSignal()
    def __init__(self):
        super().__init__()
        

    def OpenFile(self):
        print("Openning . . .")
        try:

            File = open("downloadResults.bin" ,"rb") 
            d = pickle.load(File)

            File.close()
            self.fileOpenedSignal.emit(d)

            print("file has been successfully fetched!")


        except Exception as e:
            print(f"didn't open: {e}")
            self.fileProblemSignal.emit()

class remover(QObject):
    def __init__(self,dictKey, pathToExe, pathToRar):
        super().__init__()
        try:
            
            os.remove(pathToExe)
            os.remove(pathToRar)
        except Exception as e:
            print(e)
            


        File = open("downloadResults.bin" ,"rb") 
        j = pickle.load(File)
        out = j.copy()
        for i in j:
            if i == dictKey:
                del out[i]

        File.close()
            

        File = open("downloadResults.bin" ,"wb") 
        pickle.dump(out, File)

        print("finall object has been successfully saved!")
                

