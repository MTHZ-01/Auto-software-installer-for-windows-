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


class downloader(QObject):

    extractReadySignal = pyqtSignal(list)
    percenageSignal = pyqtSignal(int)
    downloadPauseSignal = pyqtSignal()
    downloadResumeSignal = pyqtSignal()
    downloadCancleSignal = pyqtSignal()
    def __init__(self, *url):
        super().__init__()
        self.url = url
        self.pause = False

        self.downloadPauseSignal.connect(self.pauseEvent)
        self.downloadResumeSignal.connect(self.resumeEvent)
        self.cancle = False
        self.downloadCancleSignal.connect(self.cancleEvent)
    
    def cancleEvent(self):
        self.cancle = True
        print("cancled from root")
        print(self.cancle)
    
    def download_file(self):
        while not self.cancle:
            url = self.url
            try :
                if len(url) == 1 :
                    
                    ###### 1 download a file in rar or zip or exe and save to downloads directory with a new name 
                    url = url[0]
                    firstdirectory = "Downloads\\"
                    filename = ""
                    data_types = [".rar" , ".zip" , ".exe"]
                    for i in data_types :
                        try :
                            filename = url[url.rfind('/')+1:url.find(f"{i}")+4]
                            break
                        except :
                            pass
                    if filename == "" :
                        try :
                            filename = basename(url.split('?')[0])
                        except:
                            pass

                    total_directory = firstdirectory +  filename
                    print("Please wait, the file is being downloaded ... ")

                    r = get(url  , stream = True)
                    with open(total_directory, "wb") as f:
                        f.write(r.content)
                        file_size = (f"{(int(r.headers.get('content-length', 0)))/(1024*1024):.2f}") 
                        print(file_size) # print total size of our file
                        bytes_written = 0
                        start = time.time()

                        for i, chunk in enumerate(r.iter_content(chunk_size=1024)):
                            while self.pause:
                                time.sleep(.1)
                            f.write(chunk)
                            bytes_written += len(chunk)

                            downloaded_size = format(bytes_written / (1024*1024) ,  ".2f") 
                            # print(f"{downloaded_size}/{file_size}")  # print size of download in particular time

                            downloaded_percent = (i)*1024
                            percent_complete = (downloaded_percent / len(r.content)) * 100
                            # print(f"{int(percent_complete)}")  # print percentage of download
                            self.percenageSignal.emit(int(percent_complete))


                            if time.time() == start:
                                speed = 0
                            else:
                                speed = bytes_written / (time.time() - start) / 1024 / 1024
                                
                            # print(format(speed  ,  ".2f")) # print speed of download

                            file_size_2 = int(r.headers.get('Content-Length', 0))
                            if (time.time() - start) != 0 :

                                speed = (bytes_written / 1024) / (time.time() - start)
                                remaining_size = float(file_size_2) - bytes_written
                                remaining_time = remaining_size / (speed * 1024) if speed > 0 else 0
                                remaining_size = file_size_2 - bytes_written
                                # print(format(remaining_time , ".2f")) # print time remaining


                    print("The download was done successfully")


                    All_directory = total_directory

                    self.extractReadySignal.emit([All_directory])



            except Exception as e:
                print(e)
            break
        print('done')

    def pauseEvent(self):
        self.pause = True

    def resumeEvent(self):
        self.pause = False

    