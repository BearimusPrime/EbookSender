import json
import os
import time

def FolderManager(folder):
    home_folder = "/home/misio/ebooks"
    path = os.path.join(home_folder,folder)
    os.mkdir(path)

def FileDownloader(link,folder):
    os.system("megadl "+str(link)+" --path /home/misio/ebooks/"+str(folder))

def FileUploader(folder):
    os.system("rclone move /home/misio/ebooks/"+str(folder)+"/ drop:ebooks/"+str(folder)+"/ -P")

f = open('/home/misio/json.json', encoding='utf-8')
data = json.load(f)

for i in (data):
    FolderManager(str(i['Url'][-5:]))
    FileDownloader(i['MegaUrl'],i['Url'][-5:])
    FileUploader(i['Url'][-5:])
    time.sleep(5)
