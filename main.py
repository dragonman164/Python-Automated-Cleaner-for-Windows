import os
import getpass
import glob
import time

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName,files):
    for file in files:
        os.replace(file,f"{folderName}/{file}")

def emptyfolder(pathtofile):
    files=glob.glob(pathtofile)
    for file in files:
        try:
            os.remove(file)
        except:
            print("Some Folders can't be deleted. This is because they are maybe in use or try deleting them manually")
        

choice=3
print("##################################################################################")
print("Welcome to Windows Automatic Cleaner Script and maintainer by dragonman164",end='\n\n')
print("Please select one option to continue:")
print("1. Cleanup Up Windows temporary files to speed up your computer.")
print("2. Maintain the contents of a folder category wise.")
print("Please select your choice(1 or 2):")
choice=int(input())
print(end='\n\n')
if choice==1:
    print("####### Cleaning your Windows Have Patience ###############")
    time.sleep(4)
    windows_drive = os.environ['SYSTEMDRIVE'][0]
    emptyfolder(f"{windows_drive}:\\Users\\{getpass.getuser()}\\Appdata\\Local\\temp\\*")
    emptyfolder(f"{windows_drive}:\\Windows\\Prefetch\\*")
    print("########## Successfully cleaned your Windows Exiting....##############",end='\n\n')
elif choice==2:
    print("##### Welcome to Folder Maintainer #########")
    print("Please make sure to place the script in the folder you want to maintain otherwise script will not work")
    print("##### Maintaining your files please wait...... ######",end='\n\n')
    time.sleep(3)
    files = os.listdir()
    files.remove("main.py")
    createIfNotExist('Images')
    createIfNotExist('Docs')
    createIfNotExist('Media')
    createIfNotExist('Others')
    imgExts = [".png",".jpg",".jpeg"]
    docExts = [".txt",".docx",".doc",".pdf",".pptx"]
    mediaExts = [".mp4",".mp3",".flv"]
    others=[]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if(ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
            others.append(file)
    move("Media",medias)
    move("Images",images)
    move("Docs",docs)
    move("Others",others)
    print("############### Completed , Now Exiting......... ##########")

else :
    print("You have entered the wrong choice please try agian....., Exiting")
    





        

