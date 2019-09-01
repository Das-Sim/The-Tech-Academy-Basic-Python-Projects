#Python Drill Pg. 100
#Author: David A. Simar



# import the os module
import os
from datetime import datetime

# define directory
fPath = 'C:\\Users\spuns\Desktop\Drill100\\'

# itterate through Dir
fList = os.listdir(fPath)

def list():
    for file in os.listdir(fPath):
        if file.endswith(".txt"):
            tList = os.path.join(fPath, file)
            fTime = datetime.fromtimestamp(os.path.getmtime(tList))
            print('{} {}'.format(tList, fTime))




if __name__ == '__main__':
    list()

