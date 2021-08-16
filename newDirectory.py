import subprocess
import os

from os import walk
from os import listdir
from os.path import isfile, join

from tkinter import Tk, ttk, messagebox
from tkinter import filedialog as fd

#mypath = fd.askdirectory()



# This function searches the current directory, keeps track of what folders already exist and then makes a new folder with the updated weekly reporting number
def make_new_directory(mypath,weekRange):
    f = [] 
    for (dirpath, dirnames, filenames) in walk(mypath):
        f.extend(dirnames)
        break
    for i in f:
        print(i)

    f.sort(reverse=True)
    #for i in f:
     #   print(i)

    #print('highest',f[0])

    try:
            
        lead = f[0]
        #print(lead)
        lead = lead[1:3]
        #print(lead)
        new_num = int(lead) + 1
        #print(new_num)

        #weekRange = "July 11-17"
        newFolderName = "#" + str(new_num)+ " " + weekRange
        #print(newFolderName)

        #onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

        #print(onlyfiles)
        parent_directory = mypath
        path = os.path.join(parent_directory,newFolderName)
        print(path)

        os.mkdir(path)
        return path 
    except:
        print('Error, directory not created')

    





#make_new_directory(mypath)