#
#   Python:     3.6.6
#
#   Author:     Jordan Richter
#
#   Purpose:    For this drill, you will need to write a script that will check
#               a specific folder on the hard drive, verify whether those files end
#               with a “.txt” file extension and if they do, print those qualifying file
#               names and their corresponding modified time-stamps to the console.



import os

def getPath():
    fPath = 'C:\\GitRepositories\\Bootcamp-Basic-Python-Projects\\page100drill\\FolderA'
    items = os.listdir(fPath)
    itemList = []
    for names in items:
        abPath = os.path.join(fPath, names)
        mTime = os.path.getmtime(abPath)
        if names.endswith(".txt"):
            itemList.append(names)
            print(names,mTime)

    










if __name__ == "__main__":
    getPath()
