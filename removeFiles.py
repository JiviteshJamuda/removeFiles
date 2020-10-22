import time 
import os 
import shutil 

def main():
    deletedFolders = 0
    deletedFiles = 0
    path = "/pathToDelete"
    days = 30
    seconds = time.time()-(days * 24 * 60 * 60)
    if os.path.exists(path) :
        for rootFolder, folders, files in os.walk(path):
            if seconds >= getFolderAge(rootFolder):
                removeFolder(rootFolder)
                deletedFolders = deletedFolders + 1
                break
            else :
                for folder in folders :
                    folderPath = os.path.join(rootFolder, folder)
                    if seconds >= getFolderAge(folderPath):
                        removeFolder(folderPath)
                        deletedFolders = deletedFolders + 1
                for file in files :
                    filePath = os.path.join(rootFolder, file)
                    if seconds >= getFolderAge(filePath):
                        removeFile(filePath)
                        deletedFiles = deletedFiles + 1
        else: 
            if seconds >= getFolderAge(path):
                removeFile(path)
                deletedFiles = deletedFiles + 1
    else:
        print("File not found")
    print(f"total folders deleted : {deletedFolders} ")                        
    print(f"total files deleted : {deletedFiles} ")                        
                    
def removeFolder(path):
    if not shutil.rmtree(path):
        print("folder is removed successfull")
    else :
        print("unable to delete the folder")

def removeFile(path):
    if not os.remove(path):
        print("file is removed successfull")
    else :
        print("unable to delete the file")

def getFolderAge(path):
    ctime = os.stat(path).st_ctime
    return ctime

if __name__ == "__main__":
    main()