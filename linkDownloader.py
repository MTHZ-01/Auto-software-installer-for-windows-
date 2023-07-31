from urllib.request import urlretrieve
from os.path import basename
from unrar import rarfile
from os import mkdir , walk
from shutil import rmtree , move
from subprocess import run
from zipfile import ZipFile

def download_file(url,sitename):
    try :
        ###### 1 download a file in rar or zip or exe and save to downloads directory with a new name 

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
            except :
                pass
        try :
            total_directory = firstdirectory +  filename
            print("Please wait, the file is being downloaded ... ")
            urlretrieve(url, total_directory)
            print("The download was done successfully")
        except Exception as p :
            print(p)
            print("Your link has expired or There is a problem with your internet Please try again later")

        ####### 2 creat a folder in Downloads directory and remove the last (not so important)

        try :
            rmtree(f'{total_directory[:-3]}')
        except :
            pass
        path = f'.\\{total_directory[:-3]}'
        mkdir(path)

        ####### 3 Extract files

        suffix = total_directory[-3:]
        try :
            if sitename == "yasdl" :  # in this part we can add another password we want
                password = "www.yasdl.com"
            elif sitename == "sarzamindownload" :
                password = "www.sarzamindownload.com"
            if suffix == "exe" :
                move(total_directory , path)            
            elif suffix == "rar" :
                with rarfile.RarFile(total_directory , "r" , pwd=password) as rf:
                    files = rf.namelist()
                    rf.extractall(f"{path}")
            elif suffix == "zip" :
                with ZipFile(total_directory , 'r') as zip:
                    zip.extractall(f"{path}" , pwd= bytes(password , 'utf-8'))
        except :
            print("there is some problem to extract")


        ####### 4 find the .exe file and run it

        dir_path = path
        res = []
        for (dir_path, dir_names, file_names) in walk(dir_path):
            res += [[file_names , dir_path]]
        q = []
        for i in res :
            for j in i[0] :
                x = j
                if j[-3:].lower() == "exe" :
                    k = i[1]
                    q += [f"{k}\\{j}"]
        try :
            run(q[0] , shell=True)  # Here, we run the first file we found for convenience, but in general, if we have several files, it can be shown to the user to choose.
            for i in q:
                print(i)

        except :
            print("there is a problem to run the file please turn of your Antivirus")
    except Exception as a :
        print("there is a problem :" , a)
    




# download_file("https://dl.yasdl.com/2022/Software/Rufus.4.1.2045.Final_YasDL.com.rar?a", "yasdl")